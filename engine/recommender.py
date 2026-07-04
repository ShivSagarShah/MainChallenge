"""
engine/recommender.py
─────────────────────────────────────────────────────────────────────────────
Own recommendation algorithm — no external API required.

Scores each destination on 5 dimensions:
  1. Interest alignment     (35 pts)
  2. Budget compatibility   (20 pts)
  3. Season fit             (15 pts)
  4. Hidden gem preference  (20 pts)
  5. Traveller type match   (10 pts)
Total: 0–100 per destination.
"""

from __future__ import annotations
from typing import Any
from data.destinations import DESTINATIONS

# Public API
__all__ = ["score_destination", "recommend", "discover_hidden_gems", "build_heritage_trail"]


# ─────────────────────────────────────────────────────────────────────────────
# Core scoring function
# ─────────────────────────────────────────────────────────────────────────────

def score_destination(dest: dict[str, Any], prefs: dict[str, Any]) -> float:
    """
    Compute a 0–100 relevance score for *dest* given *prefs*.

    Scoring breakdown
    -----------------
    1. Interest alignment     35 pts  Jaccard-style overlap of interest tags.
    2. Budget compatibility   20 pts  Penalises cost/budget mismatch by 8 pts per level.
    3. Season fit             15 pts  Full score if travel month in best_months, partial if adjacent.
    4. Hidden-gem preference  20 pts  gem_score rewarded when user wants off-beaten-path.
    5. Traveller type match   10 pts  Exact type in dest[best_for] scores full; 'culture' partial.

    Parameters
    ----------
    dest  : Destination dict from the database.
    prefs : User preference dict with keys: interests, budget_level, month,
            wants_hidden_gems, traveller_type.

    Returns
    -------
    float
        Score in [0, 100].
    """
    score = 0.0

    # 1 · Interest alignment (35 pts)
    user_interests = set(prefs.get("interests", []))
    dest_interests = set(dest.get("interests", []))
    if user_interests:
        overlap = len(user_interests & dest_interests)
        score += (overlap / len(user_interests)) * 35
    else:
        score += 17.5  # neutral when no interests selected

    # 2 · Budget compatibility (20 pts)
    # cost_level 1–4, budget_level 1–4
    cost   = dest.get("cost_level", 2)
    budget = prefs.get("budget_level", 2)
    diff   = abs(cost - budget)
    score += max(0.0, 20.0 - diff * 8.0)

    # 3 · Season fit (15 pts)
    month       = prefs.get("month", 6)
    best_months = dest.get("best_months", list(range(1, 13)))
    if month in best_months:
        score += 15.0
    elif any(abs(month - m) <= 1 for m in best_months):
        score += 8.0

    # 4 · Hidden gem preference (20 pts)
    gem = dest.get("gem_score", 0.5)
    if prefs.get("wants_hidden_gems", False):
        score += gem * 20.0
    else:
        score += (1.0 - gem) * 14.0  # mild preference for known destinations

    # 5 · Traveller type match (10 pts)
    traveller = prefs.get("traveller_type", "solo")
    if traveller in dest.get("best_for", []):
        score += 10.0
    elif "culture" in dest.get("best_for", []):
        score += 5.0  # partial credit for culturally-rich destinations

    return round(score, 2)


# ─────────────────────────────────────────────────────────────────────────────
# Ranked recommendations
# ─────────────────────────────────────────────────────────────────────────────

def recommend(prefs: dict[str, Any], n: int = 5) -> list[dict[str, Any]]:
    """
    Return the top-*n* destinations ranked by score.

    Each result is augmented with:
    - ``score``              : float 0–100
    - ``match_pct``          : int capped at 100
    - ``matched_interests``  : list[str] shared tags
    - ``why``                : human-readable reason string

    Parameters
    ----------
    prefs : User preference dict.
    n     : Number of results to return (default 5).
    """
    scored = []
    for dest in DESTINATIONS:
        s = score_destination(dest, prefs)
        matched = list(set(prefs.get("interests", [])) & set(dest["interests"]))
        scored.append({
            **dest,
            "score":              s,
            "match_pct":          min(int(s), 100),
            "matched_interests":  matched,
            "why":                _build_why(dest, prefs, matched),
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:n]


def discover_hidden_gems(prefs: dict[str, Any], n: int = 3) -> list[dict[str, Any]]:
    """
    Return up to *n* hidden-gem destinations.

    Algorithm
    ---------
    Only considers destinations with ``gem_score >= 0.55``.
    Relevance = gem_score * 0.5 + interest_overlap * 0.4 + budget_fit * 0.1

    Parameters
    ----------
    prefs : User preference dict.
    n     : Number of gems to return (default 3).
    """
    results = []
    user_interests = set(prefs.get("interests", []))

    for dest in DESTINATIONS:
        gem = dest.get("gem_score", 0.5)
        if gem < 0.55:
            continue  # not a hidden gem
        overlap = len(user_interests & set(dest["interests"])) / max(len(user_interests), 1)
        budget_penalty = max(0, dest["cost_level"] - prefs.get("budget_level", 2)) * 0.2
        gem_score = gem * 0.5 + overlap * 0.4 + max(0, 0.1 - budget_penalty)
        results.append({**dest, "gem_relevance": round(gem_score, 3)})

    results.sort(key=lambda x: x["gem_relevance"], reverse=True)
    return results[:n]


# ─────────────────────────────────────────────────────────────────────────────
# Heritage trail builder
# ─────────────────────────────────────────────────────────────────────────────

def build_heritage_trail(dest: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Sequence heritage sites into a logical day-by-day trail.

    Slots: Morning → Midday → Afternoon → Evening → Cultural moment.
    The final entry is drawn from the destination's local events list.

    Parameters
    ----------
    dest : Destination dict.

    Returns
    -------
    list[dict]
        Each item has keys: slot, site, era, significance, tip.
    """
    sites  = dest.get("heritage_sites", [])
    events = dest.get("local_events", [])

    trail = []
    for i, site in enumerate(sites):
        slot = ["Morning visit", "Midday exploration", "Afternoon deep-dive", "Evening context"][i % 4]
        trail.append({
            "slot":        slot,
            "site":        site["name"],
            "era":         site.get("era", ""),
            "significance": site.get("significance", ""),
            "tip":         _heritage_tip(site, dest),
        })

    # Append a relevant event if one matches the user's implied season
    if events:
        ev = events[0]
        trail.append({
            "slot":         "Cultural moment",
            "site":         ev["name"],
            "era":          f"Held in month {ev['month']}",
            "significance": ev.get("description", ""),
            "tip":          f"Type: {ev.get('type','').capitalize()} event",
        })

    return trail


# ─────────────────────────────────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────────────────────────────────

def _build_why(dest: dict[str, Any], prefs: dict[str, Any], matched: list[str]) -> str:
    """Build a short human-readable reason string for a recommendation."""
    parts = []
    if matched:
        parts.append(f"Matches your interest in {', '.join(matched[:3])}")
    if dest["cost_level"] <= prefs.get("budget_level", 2):
        parts.append("fits your budget")
    if dest.get("gem_score", 0) > 0.6 and prefs.get("wants_hidden_gems"):
        parts.append("off the beaten path")
    if prefs.get("traveller_type") in dest.get("best_for", []):
        parts.append(f"ideal for {prefs['traveller_type']} travellers")
    return " · ".join(parts) if parts else "A culturally rich destination"


def _heritage_tip(site: dict[str, Any], dest: dict[str, Any]) -> str:
    """Generate a one-line visitor tip for a heritage site."""
    name = site.get("name", "")
    era  = site.get("era", "")
    if era:
        return f"Built {era} — arrive early to experience it without crowds"
    return f"One of {dest['name']}'s most significant cultural landmarks"
