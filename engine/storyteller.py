"""
engine/storyteller.py
─────────────────────────────────────────────────────────────────────────────
Immersive storytelling engine — works in two modes:

  1. Algorithm mode (no API key): pulls from the rich curated narrative
     database and personalises it based on user preferences.

  2. AI-enhanced mode (Gemini key provided): uses the curated content as
     grounding context and asks Gemini to generate a fully personalised,
     travel-magazine-quality narrative.
"""

from __future__ import annotations
import os

# ─────────────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────────────

def generate_story(dest: dict, prefs: dict, api_key: str = "") -> tuple[str, str]:
    """
    Return (story_text, mode) where mode is 'ai' or 'algorithm'.
    """
    if api_key and api_key.strip():
        try:
            story = _ai_story(dest, prefs, api_key.strip())
            return story, "ai"
        except Exception:
            pass  # fall through to algorithm mode

    return _algorithm_story(dest, prefs), "algorithm"


def generate_cultural_intro(dest: dict) -> str:
    """Single-paragraph cultural context for the destination overview."""
    parts = dest.get("storytelling", {})
    return parts.get("culture", dest.get("overview", ""))


# ─────────────────────────────────────────────────────────────────────────────
# ALGORITHM MODE — no API needed
# ─────────────────────────────────────────────────────────────────────────────

def _algorithm_story(dest: dict, prefs: dict) -> str:
    stories = dest.get("storytelling", {})
    name    = dest["name"]
    parts   = []

    # Opening — always dawn
    parts.append(stories.get("dawn", f"The city of {name} wakes slowly, each morning reaffirming a culture built over centuries."))

    # Cultural core
    parts.append(stories.get("culture", f"{name} is a city whose culture runs deeper than its surface."))

    # Interest-specific paragraphs
    for interest in prefs.get("interests", [])[:2]:
        para = stories.get(interest)
        if para:
            parts.append(para)

    # Hidden layer if requested
    if prefs.get("wants_hidden_gems", False):
        hidden = stories.get("hidden")
        if hidden:
            parts.append(hidden)

    # Closing — always dusk
    parts.append(stories.get("dusk", f"As the day ends in {name}, you understand why travellers return — something here resists explanation and rewards presence."))

    # Personalise the traveller type in the closing sentence
    traveller = prefs.get("traveller_type", "")
    if traveller == "solo":
        parts.append(f"For the solo traveller, {name} is a city that reveals itself one conversation at a time.")
    elif traveller == "couple":
        parts.append(f"For two people willing to wander without a plan, {name} offers the rare gift of shared discovery.")
    elif traveller == "backpacker":
        parts.append(f"For travellers on a limited budget, {name} is proof that the world's deepest experiences are rarely its most expensive.")
    elif traveller == "luxury":
        parts.append(f"For those who believe that luxury is about depth of experience rather than thread-count, {name} is unmatched.")

    return "\n\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# AI-ENHANCED MODE — Gemini
# ─────────────────────────────────────────────────────────────────────────────

def _ai_story(dest: dict, prefs: dict, api_key: str) -> str:
    from google import genai
    from google.genai import types

    # Use curated content as grounding so AI stays accurate
    curated = dest.get("storytelling", {})
    grounding = "\n".join([
        f"DAWN: {curated.get('dawn','')}",
        f"CULTURE: {curated.get('culture','')}",
        f"HIDDEN: {curated.get('hidden','')}",
        f"DUSK: {curated.get('dusk','')}",
    ])

    prompt = f"""You are a world-class travel writer for a luxury magazine.
Write an immersive, poetic 5-paragraph narrative about {dest['name']}, {dest['country']},
personalised for a {prefs.get('traveller_type','solo')} traveller interested in {', '.join(prefs.get('interests',[])[:4])}.

Use these verified facts as your grounding — do not invent details:
{grounding}

Additional context:
- Heritage highlights: {', '.join(s['name'] for s in dest.get('heritage_sites',[])[:3])}
- Best local experiences: {', '.join(e['name'] for e in dest.get('cultural_experiences',[])[:3])}
- Hidden gems to mention: {', '.join(g['name'] for g in dest.get('hidden_gems',[])[:2])}
- Month of travel: month {prefs.get('month', 6)}
- {'Include off-the-beaten-path discoveries' if prefs.get('wants_hidden_gems') else 'Focus on iconic cultural moments'}

Write with sensory detail — smell, sound, light, texture. Each paragraph should have a distinct
time of day or thematic focus. Make the reader feel they are already there."""

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.8, max_output_tokens=1200),
    )
    return response.text
