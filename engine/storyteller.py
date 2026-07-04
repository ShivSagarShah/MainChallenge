"""
engine/storyteller.py
─────────────────────────────────────────────────────────────────────────────
Immersive storytelling engine — two modes:

1. **Algorithm mode** (no API key): personalises curated narrative templates
   from the destination database based on user preferences.

2. **AI-enhanced mode** (Gemini key provided): uses curated content as
   grounding context and asks Gemini 2.0 Flash to generate a fully
   personalised, travel-magazine-quality narrative.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)

__all__ = ["generate_story", "generate_cultural_intro"]

_TRAVELLER_CLOSINGS: dict[str, str] = {
    "solo":       "For the solo traveller, {name} is a city that reveals itself one conversation at a time.",
    "couple":     "For two people willing to wander without a plan, {name} offers the rare gift of shared discovery.",
    "backpacker": "For travellers on a limited budget, {name} is proof that the world's deepest experiences are rarely its most expensive.",
    "luxury":     "For those who believe that luxury is about depth of experience rather than thread-count, {name} is unmatched.",
}


# ─────────────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────────────

def generate_story(
    dest: dict[str, Any],
    prefs: dict[str, Any],
    api_key: str = "",
) -> tuple[str, str]:
    """
    Generate an immersive destination story.

    Parameters
    ----------
    dest    : Destination dict from the database.
    prefs   : User preference dict.
    api_key : Optional Gemini API key. Falls back to algorithm mode if empty
              or if the API call fails.

    Returns
    -------
    tuple[str, str]
        ``(story_text, mode)`` where *mode* is ``"ai"`` or ``"algorithm"``.
    """
    if api_key and api_key.strip():
        try:
            story = _ai_story(dest, prefs, api_key.strip())
            return story, "ai"
        except Exception:  # noqa: BLE001
            logger.warning("Gemini call failed — falling back to algorithm mode.")

    return _algorithm_story(dest, prefs), "algorithm"


def generate_cultural_intro(dest: dict[str, Any]) -> str:
    """
    Return a single-paragraph cultural context summary for *dest*.

    Parameters
    ----------
    dest : Destination dict from the database.

    Returns
    -------
    str
        One paragraph of cultural context.
    """
    parts: dict[str, str] = dest.get("storytelling", {})
    return str(parts.get("culture", dest.get("overview", "")))


# ─────────────────────────────────────────────────────────────────────────────
# ALGORITHM MODE
# ─────────────────────────────────────────────────────────────────────────────

def _algorithm_story(dest: dict[str, Any], prefs: dict[str, Any]) -> str:
    """
    Build an immersive multi-paragraph story from curated templates.

    Paragraph order: dawn → culture → interest-specific (up to 2)
    → hidden layer (if requested) → dusk → traveller-type closing.
    """
    stories: dict[str, str] = dest.get("storytelling", {})
    name: str = dest.get("name", "this destination")
    parts: list[str] = []

    parts.append(stories.get(
        "dawn",
        f"The city of {name} wakes slowly, each morning reaffirming a culture built over centuries.",
    ))
    parts.append(stories.get(
        "culture", f"{name} is a city whose culture runs deeper than its surface."
    ))

    for interest in prefs.get("interests", [])[:2]:
        para = stories.get(interest)
        if para:
            parts.append(para)

    if prefs.get("wants_hidden_gems", False):
        hidden = stories.get("hidden")
        if hidden:
            parts.append(hidden)

    parts.append(stories.get(
        "dusk",
        f"As the day ends in {name}, you understand why travellers return — "
        "something here resists explanation and rewards presence.",
    ))

    closing_template = _TRAVELLER_CLOSINGS.get(prefs.get("traveller_type", ""))
    if closing_template:
        parts.append(closing_template.format(name=name))

    return "\n\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# AI-ENHANCED MODE — Gemini
# ─────────────────────────────────────────────────────────────────────────────

def _build_ai_prompt(dest: dict[str, Any], prefs: dict[str, Any]) -> str:
    """
    Construct a grounded Gemini prompt for immersive destination storytelling.

    Embeds verified destination facts to prevent hallucination.
    """
    curated: dict[str, str] = dest.get("storytelling", {})
    grounding = "\n".join([
        f"DAWN: {curated.get('dawn', '')}",
        f"CULTURE: {curated.get('culture', '')}",
        f"HIDDEN: {curated.get('hidden', '')}",
        f"DUSK: {curated.get('dusk', '')}",
    ])
    heritage    = ", ".join(s["name"] for s in dest.get("heritage_sites", [])[:3])
    experiences = ", ".join(e["name"] for e in dest.get("cultural_experiences", [])[:3])
    gems        = ", ".join(g["name"] for g in dest.get("hidden_gems", [])[:2])
    interests   = ", ".join(prefs.get("interests", [])[:4])
    instruction = (
        "Include off-the-beaten-path discoveries"
        if prefs.get("wants_hidden_gems")
        else "Focus on iconic cultural moments"
    )
    return (
        f"You are a world-class travel writer for a luxury magazine.\n"
        f"Write an immersive, poetic 5-paragraph narrative about "
        f"{dest.get('name', '')}, {dest.get('country', '')}, "
        f"personalised for a {prefs.get('traveller_type', 'solo')} traveller "
        f"interested in {interests}.\n\n"
        f"Use these verified facts as grounding — do not invent details:\n{grounding}\n\n"
        f"Additional context:\n"
        f"- Heritage highlights: {heritage}\n"
        f"- Best local experiences: {experiences}\n"
        f"- Hidden gems to mention: {gems}\n"
        f"- Month of travel: month {prefs.get('month', 6)}\n"
        f"- {instruction}\n\n"
        "Write with sensory detail — smell, sound, light, texture. "
        "Each paragraph should have a distinct time of day or thematic focus."
    )


def _ai_story(dest: dict[str, Any], prefs: dict[str, Any], api_key: str) -> str:
    """
    Call Gemini 2.0 Flash to generate a personalised travel narrative.

    Parameters
    ----------
    dest    : Destination dict.
    prefs   : User preference dict.
    api_key : Validated Gemini API key.

    Returns
    -------
    str
        AI-generated travel narrative.

    Raises
    ------
    Exception
        Any API or network error — caller catches and falls back to algorithm mode.
    """
    from google import genai  # type: ignore[import]
    from google.genai import types  # type: ignore[import]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=_build_ai_prompt(dest, prefs),
        config=types.GenerateContentConfig(temperature=0.8, max_output_tokens=1200),
    )
    return str(response.text)
