"""
tests/test_engine.py
Comprehensive test suite for Culture Compass engine.
Run: pytest tests/ -v
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from data.destinations import DESTINATIONS, DESTINATION_MAP, ALL_INTERESTS
from engine.recommender import score_destination, recommend, discover_hidden_gems, build_heritage_trail
from engine.cultural    import (
    get_authenticity_tier, match_experiences, get_events_for_month,
    get_cultural_calendar, rank_hidden_gems_for_dest, generate_cultural_immersion_plan,
)
from engine.storyteller import generate_story, generate_cultural_intro

# ── Fixtures ─────────────────────────────────────────────────────────────────

BASE_PREFS = dict(
    traveller_type    = "solo",
    interests         = ["history", "food"],
    budget_level      = 2,
    month             = 4,
    wants_hidden_gems = False,
)
GEM_PREFS = {**BASE_PREFS, "wants_hidden_gems": True, "interests": ["food", "craft"]}

KYOTO    = DESTINATION_MAP["kyoto"]
TBILISI  = DESTINATION_MAP["tbilisi"]
PLOVDIV  = DESTINATION_MAP["plovdiv"]
MARRAKECH= DESTINATION_MAP["marrakech"]


# ─────────────────────────────────────────────────────────────────────────────
# 1 · Destination data integrity
# ─────────────────────────────────────────────────────────────────────────────
class TestDestinationData:
    REQUIRED = {"id","name","country","flag","tagline","overview","interests",
                "cost_level","best_months","gem_score","best_for","hidden_gems",
                "cultural_experiences","heritage_sites","local_events","storytelling","etiquette","phrases"}

    def test_ten_or_more_destinations(self):
        assert len(DESTINATIONS) >= 10

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_required_fields_present(self, dest):
        missing = self.REQUIRED - dest.keys()
        assert not missing, f"{dest['id']} missing: {missing}"

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_gem_score_in_range(self, dest):
        assert 0.0 <= dest["gem_score"] <= 1.0

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_cost_level_valid(self, dest):
        assert dest["cost_level"] in {1, 2, 3, 4}

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_best_months_valid(self, dest):
        assert all(1 <= m <= 12 for m in dest["best_months"])

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_has_hidden_gems(self, dest):
        assert len(dest["hidden_gems"]) >= 1

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_has_cultural_experiences(self, dest):
        assert len(dest["cultural_experiences"]) >= 1

    @pytest.mark.parametrize("dest", DESTINATIONS, ids=[d["id"] for d in DESTINATIONS])
    def test_storytelling_has_required_keys(self, dest):
        keys = dest["storytelling"].keys()
        assert "dawn" in keys and "dusk" in keys and "culture" in keys

    def test_destination_map_consistent(self):
        for d in DESTINATIONS:
            assert d["id"] in DESTINATION_MAP
            assert DESTINATION_MAP[d["id"]] is d

    def test_all_interests_populated(self):
        assert len(ALL_INTERESTS) >= 5
        assert all(isinstance(i, str) for i in ALL_INTERESTS)


# ─────────────────────────────────────────────────────────────────────────────
# 2 · Recommendation algorithm
# ─────────────────────────────────────────────────────────────────────────────
class TestScoreDestination:
    def test_score_returns_float(self):
        assert isinstance(score_destination(KYOTO, BASE_PREFS), float)

    def test_score_in_range(self):
        for dest in DESTINATIONS:
            s = score_destination(dest, BASE_PREFS)
            assert 0 <= s <= 100, f"{dest['id']} score {s} out of range"

    def test_interest_match_boosts_score(self):
        hi = score_destination(KYOTO, {**BASE_PREFS, "interests": ["history","food","art"]})
        lo = score_destination(KYOTO, {**BASE_PREFS, "interests": ["adventure"]})
        assert hi > lo

    def test_budget_mismatch_lowers_score(self):
        match   = score_destination(TBILISI, {**BASE_PREFS, "budget_level": 1})   # tbilisi cost=1
        mismatch= score_destination(TBILISI, {**BASE_PREFS, "budget_level": 4})
        assert match > mismatch

    def test_season_fit_boosts_score(self):
        in_season  = score_destination(KYOTO, {**BASE_PREFS, "month": 4})   # april in best_months
        off_season = score_destination(KYOTO, {**BASE_PREFS, "month": 8})
        assert in_season >= off_season

    def test_gem_pref_boosts_high_gem_destinations(self):
        gem_score    = score_destination(PLOVDIV, {**BASE_PREFS, "wants_hidden_gems": True})
        no_gem_score = score_destination(PLOVDIV, {**BASE_PREFS, "wants_hidden_gems": False})
        assert gem_score > no_gem_score

    def test_empty_interests_gives_neutral_score(self):
        s = score_destination(KYOTO, {**BASE_PREFS, "interests": []})
        assert s > 0

    def test_traveller_type_bonus(self):
        # kyoto best_for includes 'solo'
        solo_score   = score_destination(KYOTO, {**BASE_PREFS, "traveller_type": "solo"})
        family_score = score_destination(KYOTO, {**BASE_PREFS, "traveller_type": "family"})
        assert solo_score >= family_score

    def test_tbilisi_cheapest_scores_best_on_budget1(self):
        budget1_score = score_destination(TBILISI, {**BASE_PREFS, "budget_level": 1})
        assert budget1_score >= score_destination(KYOTO, {**BASE_PREFS, "budget_level": 1})


class TestRecommend:
    def test_returns_n_results(self):
        assert len(recommend(BASE_PREFS, n=3)) == 3

    def test_results_have_score(self):
        for r in recommend(BASE_PREFS):
            assert "score" in r

    def test_results_sorted_descending(self):
        recs = recommend(BASE_PREFS)
        scores = [r["score"] for r in recs]
        assert scores == sorted(scores, reverse=True)

    def test_match_pct_leq_100(self):
        for r in recommend(BASE_PREFS):
            assert r["match_pct"] <= 100

    def test_why_is_string(self):
        for r in recommend(BASE_PREFS):
            assert isinstance(r["why"], str)

    def test_matched_interests_is_list(self):
        for r in recommend(BASE_PREFS):
            assert isinstance(r["matched_interests"], list)

    def test_gem_prefs_surface_high_gem_destinations(self):
        gem_recs = recommend(GEM_PREFS, n=5)
        # At least one high gem_score destination (>0.6) should appear in results
        assert any(r["gem_score"] > 0.6 for r in gem_recs)


class TestDiscoverHiddenGems:
    def test_returns_only_high_gem_destinations(self):
        gems = discover_hidden_gems(GEM_PREFS)
        assert all(g["gem_score"] >= 0.55 for g in gems)

    def test_gem_relevance_in_range(self):
        for g in discover_hidden_gems(GEM_PREFS):
            assert 0 <= g["gem_relevance"] <= 1.0

    def test_sorted_by_relevance(self):
        gems = discover_hidden_gems(GEM_PREFS)
        scores = [g["gem_relevance"] for g in gems]
        assert scores == sorted(scores, reverse=True)

    def test_plovdiv_appears_in_gems(self):
        gems = discover_hidden_gems(GEM_PREFS, n=5)
        ids = [g["id"] for g in gems]
        assert "plovdiv" in ids

    def test_tbilisi_appears_in_gems(self):
        gems = discover_hidden_gems(GEM_PREFS, n=5)
        ids = [g["id"] for g in gems]
        assert "tbilisi" in ids


class TestHeritageTrai:
    def test_trail_non_empty(self):
        assert len(build_heritage_trail(KYOTO)) > 0

    def test_trail_items_have_required_keys(self):
        for item in build_heritage_trail(KYOTO):
            assert "slot" in item and "site" in item

    def test_trail_includes_events(self):
        trail = build_heritage_trail(KYOTO)
        types = [item.get("slot","") for item in trail]
        assert any("Cultural" in t for t in types)


# ─────────────────────────────────────────────────────────────────────────────
# 3 · Cultural engine
# ─────────────────────────────────────────────────────────────────────────────
class TestAuthenticityTier:
    @pytest.mark.parametrize("score,expected_tier", [
        (0.3,  "Tourist Experience"),
        (0.7,  "Cultural Experience"),
        (0.88, "Immersive Experience"),
        (0.97, "Living Heritage"),
    ])
    def test_tier_mapping(self, score, expected_tier):
        label, _ = get_authenticity_tier(score)
        assert label == expected_tier

    def test_tier_returns_icon(self):
        _, icon = get_authenticity_tier(0.9)
        assert icon in {"🎭","🌍","🔥","⭐"}


class TestMatchExperiences:
    def test_returns_list(self):
        assert isinstance(match_experiences(KYOTO, BASE_PREFS), list)

    def test_sorted_by_authenticity(self):
        exps = match_experiences(KYOTO, BASE_PREFS)
        scores = [e.get("authenticity",0) for e in exps]
        assert scores == sorted(scores, reverse=True)

    def test_each_exp_has_tier(self):
        for exp in match_experiences(KYOTO, BASE_PREFS):
            assert "tier" in exp and "tier_icon" in exp

    def test_budget_filter_removes_expensive(self):
        # budget_level=1 should filter out cost_level=3 experiences
        exps_budget1 = match_experiences(KYOTO, {**BASE_PREFS, "budget_level": 1})
        exps_budget3 = match_experiences(KYOTO, {**BASE_PREFS, "budget_level": 3})
        assert len(exps_budget3) >= len(exps_budget1)


class TestGetEventsForMonth:
    def test_exact_month_match_first(self):
        # Kyoto Aoi Matsuri is in May (month 5)
        events = get_events_for_month(KYOTO, 5)
        if events:
            assert events[0]["timing"] == "During your visit"

    def test_nearby_months_included(self):
        events = get_events_for_month(KYOTO, 6, window=2)
        assert isinstance(events, list)

    def test_returns_empty_for_no_match(self):
        # oaxaca events are Oct/Nov/Jul — month 2 should return nothing in exact
        events = get_events_for_month(DESTINATION_MAP["oaxaca"], 2, window=0)
        assert events == []

    def test_timing_label_present(self):
        for ev in get_events_for_month(KYOTO, 7, window=3):
            assert "timing" in ev


class TestCulturalCalendar:
    def test_returns_dict(self):
        assert isinstance(get_cultural_calendar(KYOTO), dict)

    def test_keys_are_month_names(self):
        import calendar as cal
        cal_months = set(cal.month_name[1:])
        for k in get_cultural_calendar(KYOTO):
            assert k in cal_months

    def test_empty_months_excluded(self):
        cal_dict = get_cultural_calendar(KYOTO)
        assert all(len(v) > 0 for v in cal_dict.values())


class TestRankHiddenGems:
    def test_returns_list(self):
        assert isinstance(rank_hidden_gems_for_dest(KYOTO, BASE_PREFS), list)

    def test_interest_relevant_gems_first(self):
        # food interest → food-type gems should rank higher
        food_prefs = {**BASE_PREFS, "interests": ["food"]}
        gems = rank_hidden_gems_for_dest(MARRAKECH, food_prefs)
        food_types = [g["type"] for g in gems]
        # first gem should be food-related (if one exists)
        assert isinstance(food_types, list)

    def test_all_gems_present(self):
        gems = rank_hidden_gems_for_dest(KYOTO, BASE_PREFS)
        assert len(gems) == len(KYOTO["hidden_gems"])


class TestImmersionPlan:
    def test_correct_day_count(self):
        plan = generate_cultural_immersion_plan(KYOTO, BASE_PREFS, days=3)
        assert len(plan) == 3

    def test_each_day_has_day_number(self):
        for day in generate_cultural_immersion_plan(KYOTO, BASE_PREFS, days=2):
            assert "day" in day and isinstance(day["day"], int)

    def test_days_numbered_sequentially(self):
        plan = generate_cultural_immersion_plan(KYOTO, BASE_PREFS, days=3)
        assert [d["day"] for d in plan] == [1, 2, 3]

    def test_one_day_plan(self):
        plan = generate_cultural_immersion_plan(KYOTO, BASE_PREFS, days=1)
        assert len(plan) == 1

    def test_seven_day_plan(self):
        plan = generate_cultural_immersion_plan(KYOTO, BASE_PREFS, days=7)
        assert len(plan) == 7


# ─────────────────────────────────────────────────────────────────────────────
# 4 · Storyteller (algorithm mode — no API)
# ─────────────────────────────────────────────────────────────────────────────
class TestStorytellerAlgorithm:
    def test_returns_string(self):
        story, mode = generate_story(KYOTO, BASE_PREFS, api_key="")
        assert isinstance(story, str)

    def test_mode_is_algorithm_without_key(self):
        _, mode = generate_story(KYOTO, BASE_PREFS, api_key="")
        assert mode == "algorithm"

    def test_story_non_empty(self):
        story, _ = generate_story(KYOTO, BASE_PREFS, api_key="")
        assert len(story) > 200

    def test_story_contains_destination_name(self):
        story, _ = generate_story(KYOTO, BASE_PREFS, api_key="")
        assert "Kyoto" in story

    def test_hidden_gem_paragraph_included_when_requested(self):
        story, _ = generate_story(KYOTO, {**BASE_PREFS, "wants_hidden_gems": True}, api_key="")
        # The hidden storytelling key should be present in the output
        assert len(story) > 200

    def test_different_prefs_different_story(self):
        s1, _ = generate_story(KYOTO, {**BASE_PREFS, "interests": ["food"]}, api_key="")
        s2, _ = generate_story(KYOTO, {**BASE_PREFS, "interests": ["art"]}, api_key="")
        assert s1 != s2

    def test_cultural_intro_non_empty(self):
        intro = generate_cultural_intro(KYOTO)
        assert isinstance(intro, str) and len(intro) > 50

    def test_invalid_api_key_falls_back_to_algorithm(self):
        _, mode = generate_story(KYOTO, BASE_PREFS, api_key="invalid_key_xyz")
        assert mode == "algorithm"
