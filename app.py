"""
Culture Compass — GenAI Travel Discovery Platform
Works fully without an API key (own algorithm mode).
Add a Gemini key for AI-enhanced immersive storytelling.
"""
import os
import sys
import calendar

# Add project root to path so sub-packages resolve
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from dotenv import load_dotenv

from data.destinations import DESTINATIONS, ALL_INTERESTS
from engine.recommender import recommend, discover_hidden_gems, build_heritage_trail
from engine.storyteller  import generate_story, generate_cultural_intro
from engine.cultural     import (
    match_experiences, get_events_for_month,
    get_cultural_calendar, rank_hidden_gems_for_dest,
    generate_cultural_immersion_plan,
)

load_dotenv()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Culture Compass — AI Travel Discovery",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* skip nav */
.skip-nav{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;}
.skip-nav:focus{position:fixed;top:8px;left:8px;width:auto;height:auto;padding:8px 16px;
  background:#f59e0b;color:#000;font-weight:700;border-radius:6px;z-index:9999;text-decoration:none;}

[data-testid="stSidebar"]          { background:#0d1117; }
[data-testid="stAppViewContainer"] { background:#080c14; }

/* hero */
.hero{background:linear-gradient(135deg,#1a0a2e 0%,#0f1e3d 50%,#0a2818 100%);
  border-radius:18px;padding:32px 36px;margin-bottom:28px;border:1px solid #1e3050;
  position:relative;overflow:hidden;}
.hero::before{content:"🌍";position:absolute;right:32px;top:16px;font-size:5em;opacity:0.15;}
.hero-title{font-size:2em;font-weight:900;color:#fff;margin:0 0 8px;}
.hero-sub{color:#b0c8e0;font-size:1em;margin:0;max-width:700px;}
.hero-badge{display:inline-block;background:#0f3020;color:#4ecca3;border:1px solid #2a6a4a;
  border-radius:20px;padding:3px 12px;font-size:0.78em;font-weight:700;margin-top:12px;}

/* dest card */
.dest-card{background:linear-gradient(145deg,#101828 0%,#162030 100%);
  border:1px solid #1e3050;border-radius:14px;padding:20px;margin:8px 0;}
.dest-card:hover{border-color:#f59e0b;}
.dest-name{font-size:1.3em;font-weight:800;color:#f0f8ff;}
.dest-tagline{color:#90a8c0;font-size:0.88em;margin:4px 0 12px;}
.score-bar-wrap{background:#0a1428;border-radius:99px;height:8px;width:100%;margin:6px 0;}
.score-bar{background:linear-gradient(90deg,#f59e0b,#10b981);border-radius:99px;height:8px;}

/* badges */
.badge{display:inline-block;border-radius:20px;padding:3px 11px;
  font-size:0.76em;font-weight:700;margin:2px;}
.b-green{background:#0d2e22;color:#4ecca3;border:1px solid #4ecca3;}
.b-amber{background:#2e1d00;color:#f59e0b;border:1px solid #f59e0b;}
.b-blue {background:#0a1e3c;color:#60a5fa;border:1px solid #2563eb;}
.b-red  {background:#2e0f12;color:#f87171;border:1px solid #dc2626;}
.b-purple{background:#1e0f2e;color:#c084fc;border:1px solid #7c3aed;}

/* gem card */
.gem-card{background:#0d1a24;border:1px solid #1e4a2e;border-radius:12px;padding:16px;margin:6px 0;}
.gem-title{font-size:1.05em;font-weight:700;color:#4ecca3;}
.gem-tip{color:#b0d0c0;font-size:0.88em;margin-top:6px;font-style:italic;}

/* story */
.story-para{color:#c8d8f0;line-height:1.85;font-size:0.96em;margin-bottom:1.2em;}
.story-mode{font-size:0.78em;color:#60a5fa;font-weight:600;margin-bottom:12px;}

/* timeline */
.trail-row{display:flex;gap:14px;padding:10px 0;border-bottom:1px solid #1a2a3a;align-items:flex-start;}
.trail-slot{min-width:90px;color:#f59e0b;font-weight:700;font-size:0.88em;}
.trail-body{flex:1;color:#c0d0e0;font-size:0.9em;}
.trail-era{color:#607080;font-size:0.8em;}

/* experience card */
.exp-card{background:#0d1e18;border:1px solid #1e4030;border-radius:10px;padding:14px;margin:6px 0;}
.exp-name{font-weight:700;color:#e0f0e8;}
.exp-desc{color:#90b0a0;font-size:0.86em;margin-top:4px;}
.exp-meta{color:#607870;font-size:0.8em;margin-top:6px;}

/* etiquette */
.etiq-item{padding:7px 0;border-bottom:1px solid #1a2030;color:#b0c4d8;font-size:0.9em;}

/* plan day */
.plan-card{background:#0d1624;border:1px solid #1e2e44;border-radius:12px;padding:16px;margin:8px 0;}
.plan-day{font-size:1.1em;font-weight:800;color:#f59e0b;margin-bottom:10px;}
.plan-slot{font-size:0.82em;font-weight:700;color:#60a5fa;text-transform:uppercase;letter-spacing:.05em;margin:8px 0 4px;}
.plan-activity{color:#e0eaf8;font-weight:600;}
.plan-context{color:#8090a8;font-size:0.84em;margin-top:3px;}

/* focus ring */
*:focus-visible{outline:2px solid #f59e0b !important;outline-offset:2px !important;}
[data-testid="stCheckbox"] label{color:#c8d8f0 !important;}
</style>
<a class="skip-nav" href="#main-content">Skip to main content</a>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
TRAVELLER_TYPES = ["solo", "couple", "family", "backpacker", "luxury", "culture"]
TRAVELLER_ICONS = {"solo":"🧳","couple":"💑","family":"👨‍👩‍👧","backpacker":"🎒","luxury":"✨","culture":"🎭"}
BUDGET_LABELS   = {1:"Budget ($)", 2:"Moderate ($$)", 3:"Comfortable ($$$)", 4:"Luxury ($$$$)"}
MONTH_NAMES     = {i: calendar.month_name[i] for i in range(1, 13)}
INTEREST_ICONS  = {
    "history":"🏛️","food":"🍜","art":"🎨","architecture":"🏰","spirituality":"🕌",
    "nature":"🌿","craft":"🧶","adventure":"⛰️","music":"🎵",
}

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧭 Culture Compass")
    st.caption("AI travel discovery — works without any API key")
    st.divider()

    api_key = st.text_input(
        "Gemini API Key (optional)",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Optional — enhances storytelling with AI. App works fully without it.",
    )
    mode_label = "🤖 AI-Enhanced Mode" if api_key else "⚙️ Algorithm Mode (no key needed)"
    st.caption(mode_label)

    st.divider()
    st.markdown("**🌍 Where do you want to go?**")

    traveller_type = st.selectbox(
        "I am a...",
        TRAVELLER_TYPES,
        format_func=lambda t: f"{TRAVELLER_ICONS[t]} {t.title()} Traveller",
    )

    interests = st.multiselect(
        "My interests",
        ALL_INTERESTS,
        default=["history", "food"],
        format_func=lambda i: f"{INTEREST_ICONS.get(i,'🔹')} {i.title()}",
    )

    budget_level = st.select_slider(
        "Budget level",
        options=[1, 2, 3, 4],
        value=2,
        format_func=lambda b: BUDGET_LABELS[b],
    )

    month = st.selectbox(
        "Travel month",
        list(range(1, 13)),
        index=5,
        format_func=lambda m: MONTH_NAMES[m],
    )

    wants_hidden_gems = st.toggle("🔭 Prioritise hidden gems", value=False)

    st.divider()
    st.markdown("**🔍 Explore a specific destination**")
    dest_names = ["— Show all recommendations —"] + [f"{d['flag']} {d['name']}, {d['country']}" for d in DESTINATIONS]
    selected_dest_label = st.selectbox("Deep-dive into", dest_names)
    selected_dest_id = None
    if selected_dest_label != dest_names[0]:
        for d in DESTINATIONS:
            if d["name"] in selected_dest_label:
                selected_dest_id = d["id"]
                break

    st.divider()
    if selected_dest_id:
        story_days = st.slider("Immersion plan (days)", 1, 7, 3)
    discover_btn = st.button("🚀 Discover Destinations", type="primary", use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# PREFS DICT
# ─────────────────────────────────────────────────────────────────────────────
prefs = dict(
    traveller_type    = traveller_type,
    interests         = interests,
    budget_level      = budget_level,
    month             = month,
    wants_hidden_gems = wants_hidden_gems,
)

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div id="main-content">
<div class="hero" role="banner">
    <div class="hero-title">🧭 Culture Compass</div>
    <div class="hero-sub">
        Discover destinations through immersive storytelling, uncover hidden gems, explore
        living heritage, find authentic cultural experiences and connect with local traditions —
        powered by a personalised recommendation engine that works without any API key.
    </div>
    <div class="hero-badge">⚙️ Own Algorithm + Optional AI Enhancement</div>
</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# LANDING
# ─────────────────────────────────────────────────────────────────────────────
if "results" not in st.session_state and not discover_btn and not selected_dest_id:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
**What Culture Compass does:**

| | Feature | How |
|--|---|---|
| 🗺️ | **Smart Recommendations** | Own scoring algorithm — 5 dimensions |
| 💎 | **Hidden Gem Discovery** | Authenticity × popularity inverse score |
| 📖 | **Immersive Storytelling** | Template engine or Gemini AI |
| 🎭 | **Cultural Experiences** | Matched to your interests + budget |
| 🎪 | **Local Events** | Month-aware cultural calendar |
| 🏛️ | **Heritage Trail** | Day-by-day itinerary builder |
| 🗣️ | **Etiquette & Phrases** | Essential cultural guidance |
| 📅 | **Immersion Plan** | Full 1–7 day cultural itinerary |
        """)
    with c2:
        st.markdown("""
**How the algorithm works:**

The recommendation engine scores destinations on 5 dimensions:
- **Interest alignment** — how many of your interests match (35 pts)
- **Budget compatibility** — cost level vs. your budget (20 pts)
- **Season fit** — optimal travel months (15 pts)
- **Hidden gem preference** — authenticity score matching (20 pts)
- **Traveller type match** — solo/couple/backpacker fit (10 pts)

**No API key needed.** Every feature works without Gemini.
Add a key only for richer AI-generated storytelling.

Select your preferences in the sidebar and click **Discover Destinations**.
        """)
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# RUN DISCOVERY
# ─────────────────────────────────────────────────────────────────────────────
if discover_btn:
    with st.spinner("Running cultural recommendation engine…"):
        top_recs  = recommend(prefs, n=5)
        top_gems  = discover_hidden_gems(prefs, n=3)
    st.session_state.update(
        results   = top_recs,
        gems      = top_gems,
        prefs     = prefs,
        api_key   = api_key,
    )

results  = st.session_state.get("results", [])
gems     = st.session_state.get("gems", [])
s_prefs  = st.session_state.get("prefs", prefs)
s_key    = st.session_state.get("api_key", api_key)

# ─────────────────────────────────────────────────────────────────────────────
# DEEP-DIVE MODE: single destination selected
# ─────────────────────────────────────────────────────────────────────────────
if selected_dest_id:
    from data.destinations import DESTINATION_MAP
    dest = DESTINATION_MAP.get(selected_dest_id)
    if not dest:
        st.error("Destination not found.")
        st.stop()

    st.markdown(f"## {dest['flag']} {dest['name']}, {dest['country']}")
    st.caption(dest["tagline"])
    st.markdown(f"> {dest['overview']}")

    tabs = st.tabs(["📖 Story", "🎭 Experiences", "🎪 Events", "🏛️ Heritage Trail", "💎 Hidden Gems", "📅 Immersion Plan", "🗣️ Culture Guide"])

    with tabs[0]:  # Story
        st.markdown("### Immersive Narrative")
        with st.spinner("Generating story…"):
            story, mode = generate_story(dest, s_prefs, s_key)
        mode_str = "✨ AI-Enhanced (Gemini)" if mode == "ai" else "⚙️ Algorithm Mode — add a Gemini key for AI storytelling"
        st.markdown(f'<div class="story-mode">{mode_str}</div>', unsafe_allow_html=True)
        for para in story.split("\n\n"):
            if para.strip():
                st.markdown(f'<div class="story-para">{para.strip()}</div>', unsafe_allow_html=True)

    with tabs[1]:  # Experiences
        st.markdown("### Cultural Experiences")
        st.caption("Ranked by authenticity · matched to your budget")
        exps = match_experiences(dest, s_prefs)
        if exps:
            for exp in exps:
                auth_pct = int(exp.get("authenticity", 0) * 100)
                st.markdown(f"""
<div class="exp-card" role="article" aria-label="{exp['name']}">
  <div class="exp-name">{exp.get('tier_icon','')} {exp['name']}
    <span class="badge b-green" style="float:right">{exp.get('tier','')}</span>
  </div>
  <div class="exp-desc">{exp.get('description','')}</div>
  <div class="exp-meta">⏱ {exp.get('duration','')} &nbsp;|&nbsp; Authenticity: {auth_pct}%</div>
</div>""", unsafe_allow_html=True)
        else:
            st.info("No experiences matching your current filters.")

    with tabs[2]:  # Events
        st.markdown("### Cultural Calendar")
        events_now = get_events_for_month(dest, s_prefs.get("month", month))
        full_cal   = get_cultural_calendar(dest)

        if events_now:
            st.markdown(f"**Events around {MONTH_NAMES[s_prefs.get('month', month)]}:**")
            for ev in events_now:
                ev_type = ev.get("type","").title()
                st.markdown(f"""
<div class="gem-card" role="article">
  <div class="gem-title">🎪 {ev['name']} <span class="badge b-amber">{ev_type}</span></div>
  <div class="gem-tip">{ev.get('description','')}</div>
  <div style="color:#607080;font-size:0.8em;margin-top:6px">{ev.get('timing','')}</div>
</div>""", unsafe_allow_html=True)
        else:
            st.info(f"No events found near {MONTH_NAMES[s_prefs.get('month', month)]}.")

        if full_cal:
            st.divider()
            st.markdown("**Full year calendar:**")
            for month_name, evs in full_cal.items():
                with st.expander(f"📅 {month_name} ({len(evs)} event{'s' if len(evs)>1 else ''})"):
                    for ev in evs:
                        st.markdown(f"**{ev['name']}** — {ev.get('description','')}")

    with tabs[3]:  # Heritage Trail
        st.markdown("### Heritage Trail")
        st.caption("Day-by-day itinerary through the destination's historical layers")
        trail = build_heritage_trail(dest)
        st.markdown('<ol role="list" style="list-style:none;padding:0">', unsafe_allow_html=True)
        for item in trail:
            st.markdown(f"""
<li class="trail-row" role="listitem">
  <span class="trail-slot">{item['slot']}</span>
  <div class="trail-body">
    <strong style="color:#f0f8ff">{item['site']}</strong>
    <div class="trail-era">{item.get('era','')}</div>
    <div style="color:#90a8c0;font-size:0.85em;margin-top:4px">{item.get('significance','')}</div>
    <div style="color:#608060;font-size:0.82em;font-style:italic;margin-top:4px">💡 {item.get('tip','')}</div>
  </div>
</li>""", unsafe_allow_html=True)
        st.markdown("</ol>", unsafe_allow_html=True)

    with tabs[4]:  # Hidden Gems
        st.markdown("### Hidden Gems")
        st.caption("Places the guidebooks missed — ranked by relevance to your interests")
        gems_dest = rank_hidden_gems_for_dest(dest, s_prefs)
        for gem in gems_dest:
            st.markdown(f"""
<div class="gem-card" role="article" aria-label="{gem['name']}">
  <div class="gem-title">💎 {gem['name']} <span class="badge b-purple">{gem.get('type','').title()}</span></div>
  <div class="gem-tip">{gem.get('tip','')}</div>
</div>""", unsafe_allow_html=True)

    with tabs[5]:  # Immersion Plan
        days_val = st.session_state.get("story_days_val", 3)
        days_val = story_days if "story_days" in dir() else 3
        st.markdown(f"### {days_val}-Day Cultural Immersion Plan")
        plan = generate_cultural_immersion_plan(dest, s_prefs, days=days_val)
        for day_plan in plan:
            day_num = day_plan["day"]
            st.markdown(f'<div class="plan-card" role="article" aria-label="Day {day_num}">', unsafe_allow_html=True)
            st.markdown(f'<div class="plan-day">Day {day_num}</div>', unsafe_allow_html=True)
            for slot_key, label in [("morning","🌅 Morning"), ("afternoon","☀️ Afternoon"), ("evening","🌙 Evening")]:
                item = day_plan.get(slot_key)
                if item:
                    type_badge = {"heritage":"🏛️","cultural_experience":"🎭","hidden_gem":"💎"}.get(item.get("type",""),"🔹")
                    st.markdown(f'<div class="plan-slot">{label}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="plan-activity">{type_badge} {item["activity"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="plan-context">{item.get("context","")}</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tabs[6]:  # Culture Guide
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### 🗣️ Essential Phrases")
            phrases = dest.get("phrases", {})
            for eng, local in phrases.items():
                st.markdown(f"**{eng}** → *{local}*")

        with col_b:
            st.markdown("### 🙏 Etiquette & Customs")
            for tip in dest.get("etiquette", []):
                st.markdown(f'<div class="etiq-item">• {tip}</div>', unsafe_allow_html=True)

        st.divider()
        st.markdown("### 🍽️ Food Highlights")
        foods = dest.get("food_highlights", [])
        food_cols = st.columns(min(len(foods), 5))
        for i, food in enumerate(foods):
            food_cols[i % len(food_cols)].markdown(f"**{food}**")

    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# RESULTS MODE: recommendations + gems
# ─────────────────────────────────────────────────────────────────────────────
if not results:
    st.stop()

tab_recs, tab_gems, tab_culture = st.tabs([
    "🗺️ Recommended Destinations",
    "💎 Hidden Gems",
    "🌍 Cultural Snapshot",
])

with tab_recs:
    st.markdown(f"### Top {len(results)} destinations for you")
    st.caption(f"Ranked by: interest alignment · budget fit · season · {'hidden gem score' if s_prefs['wants_hidden_gems'] else 'popularity'} · traveller type")
    st.write("")

    for rank, dest in enumerate(results, 1):
        match = dest["match_pct"]
        bar_w = min(match, 100)
        interests_html = "".join(
            f'<span class="badge b-blue">{INTEREST_ICONS.get(i,"🔹")} {i}</span>'
            for i in dest.get("matched_interests", [])[:4]
        )
        cost_icons = "💲" * dest.get("cost_level", 2)
        gem_badge = f'<span class="badge b-purple">💎 Hidden Gem</span>' if dest.get("gem_score", 0) > 0.6 else ""

        st.markdown(f"""
<div class="dest-card" role="article" aria-label="{dest['name']}">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">
    <div>
      <div class="dest-name">#{rank} {dest['flag']} {dest['name']}, {dest['country']} {gem_badge}</div>
      <div class="dest-tagline">{dest['tagline']}</div>
    </div>
    <div style="text-align:right">
      <div style="color:#f59e0b;font-size:1.4em;font-weight:800">{match}<span style="font-size:0.6em;color:#607080">%</span></div>
      <div style="color:#607080;font-size:0.78em">match score</div>
    </div>
  </div>
  <div class="score-bar-wrap" role="progressbar" aria-valuenow="{bar_w}" aria-valuemin="0" aria-valuemax="100">
    <div class="score-bar" style="width:{bar_w}%"></div>
  </div>
  <div style="margin:8px 0">{interests_html}
    <span class="badge b-amber">{cost_icons}</span>
    <span class="badge b-green">📅 Best: {', '.join(calendar.month_abbr[m] for m in dest.get('best_months',[])[:3])}</span>
  </div>
  <div style="color:#7090a0;font-size:0.84em;font-style:italic">{dest.get('why','')}</div>
</div>
""", unsafe_allow_html=True)

        with st.expander(f"📖 Read the {dest['name']} story"):
            story, mode = generate_story(dest, s_prefs, s_key)
            mode_str = "✨ AI" if mode == "ai" else "⚙️ Algorithm"
            st.caption(f"Story mode: {mode_str}")
            for para in story.split("\n\n"):
                if para.strip():
                    st.markdown(f'<div class="story-para">{para.strip()}</div>', unsafe_allow_html=True)
            st.markdown(f"**Explore {dest['name']} in depth:** select it from the sidebar dropdown →")

with tab_gems:
    st.markdown("### 💎 Hidden Gems")
    st.caption("Destinations scored high on authenticity + low on tourist density · personalised to your interests")
    st.write("")

    if gems:
        for gem_dest in gems:
            gem_relevance = int(gem_dest.get("gem_relevance", 0) * 100)
            st.markdown(f"""
<div class="gem-card" role="article" aria-label="{gem_dest['name']}">
  <div style="display:flex;justify-content:space-between">
    <div class="gem-title">{gem_dest['flag']} {gem_dest['name']}, {gem_dest['country']}</div>
    <span class="badge b-purple">Gem score {gem_relevance}%</span>
  </div>
  <div style="color:#b0c8b8;font-size:0.9em;margin:6px 0">{gem_dest['overview'][:200]}…</div>
</div>
""", unsafe_allow_html=True)
            with st.expander(f"💎 Hidden spots in {gem_dest['name']}"):
                for spot in gem_dest.get("hidden_gems", []):
                    st.markdown(f"**{spot['name']}**")
                    st.markdown(f"*{spot['tip']}*")
                    st.write("")

with tab_culture:
    st.markdown("### 🌍 Quick Cultural Snapshot")
    st.caption("Top cultural experiences across your recommended destinations")
    for dest in results[:3]:
        st.markdown(f"#### {dest['flag']} {dest['name']}")
        intro = generate_cultural_intro(dest)
        st.markdown(f'<div class="story-para">{intro}</div>', unsafe_allow_html=True)
        exps = match_experiences(dest, s_prefs)[:2]
        for exp in exps:
            st.markdown(f"- **{exp['name']}** {exp.get('tier_icon','')} — {exp.get('description','')[:100]}…")
        st.write("")

# Footer
st.divider()
col_dl, col_reset, _ = st.columns([1, 1, 4])
with col_dl:
    import json
    export = {
        "recommendations": [{"name": d["name"], "country": d["country"], "score": d["score"], "why": d["why"]} for d in results],
        "hidden_gems": [{"name": g["name"], "country": g["country"]} for g in gems],
        "preferences": s_prefs,
    }
    st.download_button("⬇️ Export Results", json.dumps(export, indent=2), "culture_compass_results.json", "application/json")
with col_reset:
    if st.button("🔄 New Search"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
