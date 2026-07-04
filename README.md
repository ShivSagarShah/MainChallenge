# 🧭 Culture Compass — GenAI Travel Discovery Platform

> **Hack2Skill Main Challenge Submission**
> Build a GenAI-powered platform that helps travelers discover destinations and engage with local culture in meaningful ways.

---

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shivsagarshah-mainchallenge-app-xxxx.streamlit.app)

> Add your Gemini API key in the sidebar to enable AI-enhanced storytelling.
> **The app works fully without any API key** — all core features run on the built-in algorithm.

---

## What It Does

Culture Compass uses Generative AI and a custom recommendation algorithm to:

| Feature | Description |
|---------|-------------|
| 🗺️ **Smart Destination Recommendations** | Personalised ranking using a 5-dimension weighted scoring algorithm |
| 💎 **Hidden Gem Discovery** | Surfaces off-the-beaten-path destinations via an authenticity × popularity inverse formula |
| 📖 **Immersive Storytelling** | Travel-magazine-quality narratives — template algorithm or Gemini AI enhanced |
| 🎭 **Cultural Experience Matching** | Experiences matched to budget and interests, tiered by authenticity (Tourist → Living Heritage) |
| 🎪 **Local Events Calendar** | Month-aware cultural event discovery with full-year calendar view |
| 🏛️ **Heritage Trail Builder** | Day-by-day itinerary through a destination's historical layers |
| 📅 **Cultural Immersion Plan** | 1–7 day plan combining heritage, experiences and hidden gems |
| 🗣️ **Culture Guide** | Essential phrases, etiquette rules and food highlights per destination |

---

## GenAI Services Used

**Google Gemini 2.0 Flash** via `google-genai` SDK (optional enhancement)

| Where Used | How |
|------------|-----|
| Immersive Storytelling | Generates personalised travel-magazine narratives grounded in curated destination facts |
| Cultural Narrative | AI rewrites template stories with sensory detail personalised to traveller type and interests |
| Fallback | App switches seamlessly to algorithm mode if no key is provided or quota is exceeded |

---

## Own Algorithm (No API Required)

The recommendation engine scores every destination on **5 dimensions** with a 0–100 total score:

```
Score = Interest Alignment (35) + Budget Compatibility (20)
      + Season Fit (15) + Hidden Gem Preference (20) + Traveller Type Match (10)
```

**Hidden Gem Formula:**
```
gem_relevance = gem_score × 0.5 + interest_overlap × 0.4 + budget_fit × 0.1
```

**Authenticity Tiers:**
```
0.0 – 0.6  →  Tourist Experience   🎭
0.6 – 0.8  →  Cultural Experience  🌍
0.8 – 0.95 →  Immersive Experience 🔥
0.95 – 1.0 →  Living Heritage      ⭐
```

---

## Destination Database

**10 curated destinations** — each with full cultural data:

| Destination | Country | Hidden Gems | Cultural Experiences | Heritage Sites | Events |
|-------------|---------|-------------|----------------------|----------------|--------|
| Kyoto | 🇯🇵 Japan | 3 | 3 | 3 | 3 |
| Marrakech | 🇲🇦 Morocco | 3 | 3 | 3 | 3 |
| Tbilisi | 🇬🇪 Georgia | 3 | 3 | 3 | 3 |
| Oaxaca | 🇲🇽 Mexico | 3 | 3 | 3 | 3 |
| Hội An | 🇻🇳 Vietnam | 3 | 3 | 3 | 3 |
| Plovdiv | 🇧🇬 Bulgaria | 3 | 3 | 3 | 3 |
| Luang Prabang | 🇱🇦 Laos | 3 | 3 | 3 | 3 |
| Porto | 🇵🇹 Portugal | 3 | 3 | 3 | 3 |
| Cartagena | 🇨🇴 Colombia | 3 | 3 | 3 | 3 |
| Chiang Mai | 🇹🇭 Thailand | 3 | 3 | 3 | 3 |

Each destination includes: overview · interest tags · cost level · best travel months · gem score · best-for traveller types · 5-paragraph immersive storytelling · etiquette tips · local phrases · food highlights.

---

## Project Structure

```
culture-compass/
├── app.py                    # Streamlit UI — 8 tabs, full accessibility
├── data/
│   └── destinations.py       # Rich curated destination database
├── engine/
│   ├── recommender.py        # 5-dimension scoring + hidden gem algorithm
│   ├── storyteller.py        # Template storytelling + Gemini AI enhancement
│   └── cultural.py           # Experience matching, event calendar, immersion planner
├── tests/
│   └── test_engine.py        # 129 tests — all passing
├── requirements.txt
└── .env.example
```

---

## Test Suite

**129 tests, 0 failures** — covering the full engine without mocking any external API:

```
TestDestinationData          — data integrity for all 10 destinations (parametrized)
TestScoreDestination         — scoring algorithm correctness
TestRecommend                — ranking, sorting, metadata
TestDiscoverHiddenGems       — gem formula, specific destinations
TestHeritageTrai             — trail structure
TestAuthenticityTier         — tier mapping
TestMatchExperiences         — budget filter, sort order
TestGetEventsForMonth        — exact + nearby month logic
TestCulturalCalendar         — full-year grouping
TestRankHiddenGems           — interest relevance ordering
TestImmersionPlan            — 1–7 day plan generation
TestStorytellerAlgorithm     — no-API storytelling + fallback behaviour
```

Run locally:
```bash
pytest tests/ -v
```

---

## Accessibility

- Skip navigation link (WCAG 2.4.1 — bypass blocks)
- `role="article"` on all destination and experience cards
- `role="listitem"` on heritage trail rows
- `role="progressbar"` with `aria-valuenow/min/max` on score bars
- `aria-label` on all custom HTML elements
- All text contrast ≥ 4.5:1 (WCAG AA compliant)
- Global `*:focus-visible` keyboard navigation ring

---

## Setup (Local)

```bash
# Clone
git clone https://github.com/ShivSagarShah/MainChallenge.git
cd MainChallenge

# Install
uv venv .venv
uv pip install --link-mode copy -r requirements.txt

# Optional: add Gemini key
cp .env.example .env
# Edit .env and add: GEMINI_API_KEY=your-key

# Run
.venv/Scripts/streamlit.exe run app.py
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| UI | Streamlit 1.58 |
| AI (optional) | Google Gemini 2.0 Flash (`google-genai`) |
| Algorithm | Custom Python — no ML libraries |
| Testing | pytest 9.x — 129 tests |
| Language | Python 3.12 |
