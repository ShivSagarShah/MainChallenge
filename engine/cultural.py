"""
engine/cultural.py
─────────────────────────────────────────────────────────────────────────────
Cultural experience matching and event discovery — own algorithm.
"""

from __future__ import annotations
import calendar
from typing import Any

__all__ = [
    "get_authenticity_tier", "match_experiences", "get_events_for_month",
    "get_cultural_calendar", "rank_hidden_gems_for_dest", "generate_cultural_immersion_plan",
]

MONTH_NAMES: dict[int, str] = {i: calendar.month_name[i] for i in range(1, 13)}

# Authenticity tiers
TIER_LABELS = {
    (0.0, 0.6):  ("Tourist Experience", "🎭"),
    (0.6, 0.8):  ("Cultural Experience", "🌍"),
    (0.8, 0.95): ("Immersive Experience", "🔥"),
    (0.95, 1.01):("Living Heritage", "⭐"),
}


def get_authenticity_tier(score: float) -> tuple[str, str]:
    """
    Map an authenticity score (0–1) to a human-readable tier label and icon.

    Tiers
    -----
    0.00–0.60  Tourist Experience   🎭
    0.60–0.80  Cultural Experience  🌍
    0.80–0.95  Immersive Experience 🔥
    0.95–1.00  Living Heritage      ⭐
    """
    for (lo, hi), label in TIER_LABELS.items():
        if lo <= score < hi:
            return label
    return ("Cultural Experience", "🌍")


def match_experiences(dest: dict, prefs: dict) -> list[dict]:
    """
    Filter and rank cultural experiences based on user interests and budget.
    Returns experiences annotated with tier label.
    """
    experiences = dest.get("cultural_experiences", [])
    user_interests = set(prefs.get("interests", []))
    budget_level   = prefs.get("budget_level", 2)

    results = []
    for exp in experiences:
        if exp.get("cost_level", 1) > budget_level + 1:
            continue  # too expensive
        tier, icon = get_authenticity_tier(exp.get("authenticity", 0.7))
        results.append({**exp, "tier": tier, "tier_icon": icon})

    # Sort by authenticity descending
    results.sort(key=lambda x: x.get("authenticity", 0), reverse=True)
    return results


def get_events_for_month(
    dest: dict[str, Any], month: int, window: int = 2
) -> list[dict[str, Any]]:
    """
    Return events within *window* months of *month*.

    Events in the exact month are returned first with timing="During your visit".
    Nearby events include a relative timing label.

    Parameters
    ----------
    dest   : Destination dict.
    month  : 1–12 integer representing the travel month.
    window : How many months either side to include (default 2).
    """
    events = dest.get("local_events", [])
    exact, nearby = [], []

    for ev in events:
        ev_month = ev.get("month", 0)
        if ev_month == month:
            exact.append({**ev, "timing": "During your visit"})
        elif abs(ev_month - month) <= window:
            diff = ev_month - month
            label = f"{abs(diff)} month{'s' if abs(diff)>1 else ''} {'after' if diff>0 else 'before'} your visit"
            nearby.append({**ev, "timing": label})

    return exact + nearby


def get_cultural_calendar(dest: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """Return all events grouped by month name, excluding months with no events."""
    calendar_map: dict = {i: [] for i in range(1, 13)}
    for ev in dest.get("local_events", []):
        m = ev.get("month")
        if m and 1 <= m <= 12:
            calendar_map[m].append(ev)
    return {MONTH_NAMES[k]: v for k, v in calendar_map.items() if v}


def rank_hidden_gems_for_dest(
    dest: dict[str, Any], prefs: dict[str, Any]
) -> list[dict[str, Any]]:
    """
    Rank hidden gems within *dest* by relevance to user interests.

    Uses a loose type→interest mapping to score each gem.
    Gems whose type maps to a user interest score 1.0; others score 0.5.
    """
    gems   = dest.get("hidden_gems", [])
    interests = set(prefs.get("interests", []))

    def _score(gem):
        t = gem.get("type", "")
        # loose type→interest mapping
        type_map = {
            "food": "food", "craft": "craft", "spiritual": "spirituality",
            "heritage": "history", "art": "art", "nature": "nature",
            "architecture": "architecture", "culture": "art", "wellness": "nature",
            "exploration": "adventure",
        }
        mapped = type_map.get(t, "")
        return 1.0 if mapped in interests else 0.5

    return sorted(gems, key=_score, reverse=True)


def generate_cultural_immersion_plan(
    dest: dict[str, Any], prefs: dict[str, Any], days: int = 3
) -> list[dict[str, Any]]:
    """
    Build a day-by-day cultural immersion itinerary.

    Each day contains up to three slots (morning / afternoon / evening)
    drawing from heritage sites, cultural experiences and hidden gems
    in round-robin order.

    Parameters
    ----------
    dest  : Destination dict.
    prefs : User preference dict.
    days  : Number of days to plan (1–7).

    Returns
    -------
    list[dict]
        One entry per day with keys: day, morning, afternoon, evening.
    """
    experiences = match_experiences(dest, prefs)
    gems        = rank_hidden_gems_for_dest(dest, prefs)
    heritage    = dest.get("heritage_sites", [])
    plan        = []

    for day in range(1, days + 1):
        morning = heritage[(day - 1) % len(heritage)] if heritage else None
        afternoon_exp = experiences[(day - 1) % len(experiences)] if experiences else None
        evening_gem   = gems[(day - 1) % len(gems)] if gems else None

        day_plan: dict[str, Any] = {"day": day, "morning": None, "afternoon": None, "evening": None}

        if morning:
            day_plan["morning"] = {
                "activity": f"Visit {morning['name']}",
                "context":  morning.get("significance", ""),
                "type":     "heritage",
            }
        if afternoon_exp:
            day_plan["afternoon"] = {
                "activity":    afternoon_exp["name"],
                "context":     afternoon_exp.get("description", ""),
                "duration":    afternoon_exp.get("duration", ""),
                "type":        "cultural_experience",
                "tier":        afternoon_exp.get("tier", ""),
            }
        if evening_gem:
            day_plan["evening"] = {
                "activity": f"Discover: {evening_gem['name']}",
                "context":  evening_gem.get("tip", ""),
                "type":     "hidden_gem",
            }
        plan.append(day_plan)

    return plan
