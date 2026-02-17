import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 0. NUCLEAR OPTION: AUTO-GENERATE DARK THEME CONFIG
# -----------------------------------------------------------------------------
if not os.path.exists('.streamlit'):
    os.makedirs('.streamlit')

with open('.streamlit/config.toml', 'w') as f:
    f.write("""
[theme]
base="dark"
primaryColor="#D4AF37"
backgroundColor="#000000"
secondaryBackgroundColor="#0e0e0e"
textColor="#E0E0E0"
font="sans serif"
""")

# -----------------------------------------------------------------------------
# 1. UI CONFIGURATION & LUXURY ATELIER CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500&display=swap');

    /* GLOBAL APP STYLING */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        font-family: 'Montserrat', sans-serif !important;
    }

    /* LUXURY HEADERS */
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.8rem !important;
        text-transform: uppercase;
        margin-top: 0px;
        letter-spacing: 2px;
        padding-bottom: 10px;
        text-shadow: 0px 4px 12px rgba(0,0,0,0.5);
    }

    h3 {
        font-family: 'Playfair Display', serif !important;
        color: #D4AF37 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 5px;
        margin-top: 20px;
        display: inline-block;
    }

    .sub-header {
        color: #888;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.8rem !important;
        letter-spacing: 4px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 50px;
        border-top: 1px solid rgba(212, 175, 55, 0.2);
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
        padding: 15px 0;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- DROPDOWN MENUS FIX --- */
    div[data-baseweb="popover"], div[data-baseweb="popover"] > div {
        background-color: #000000 !important;
        border: 1px solid #D4AF37 !important;
    }
    ul[data-baseweb="menu"] { background-color: #000000 !important; }
    li[data-baseweb="option"] { color: #cccccc !important; background-color: #000000 !important; }
    li[data-baseweb="option"]:hover, li[aria-selected="true"] {
        background-color: #D4AF37 !important; color: #000000 !important;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #0e0e0e !important; border: 1px solid #333 !important; color: #D4AF37 !important;
    }

    /* --- CUSTOM TABLE STYLING (HTML) --- */
    .luxury-table {
        width: 100%; border-collapse: collapse; background-color: #0e0e0e; color: #cccccc; font-family: 'Montserrat', sans-serif; font-size: 0.85rem;
    }
    .luxury-table th {
        background-color: #1a1a1a; color: #D4AF37; font-family: 'Playfair Display', serif; font-weight: normal; text-align: left; padding: 12px; border-bottom: 1px solid #D4AF37; text-transform: uppercase; letter-spacing: 1px;
    }
    .luxury-table td { padding: 10px; border-bottom: 1px solid #333; }
    .luxury-table tr:hover { background-color: rgba(212, 175, 55, 0.05); }

    /* --- LINKS & BUTTONS STYLING --- */
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; text-shadow: 0 0 8px #D4AF37; }

    /* --- METRICS & CARDS --- */
    .gold-metric {
        background-color: rgba(5, 5, 5, 0.5); border: 1px solid #222; padding: 25px; text-align: center; transition: all 0.3s ease; position: relative;
    }
    .gold-metric::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, #D4AF37, transparent);
    }
    .gold-metric:hover { background-color: rgba(212, 175, 55, 0.05); border-color: #444; }
    .metric-label { color: #888; font-family: 'Montserrat', sans-serif; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; }
    .metric-value { font-family: 'Playfair Display', serif; font-size: 2.8rem; color: #F0E68C; background: linear-gradient(to bottom, #FCF6BA, #AA771C); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    
    .insight-card {
        border-left: 2px solid #D4AF37; background: linear-gradient(90deg, rgba(20,20,20,0.9) 0%, rgba(10,10,10,0.0) 100%); padding: 25px; margin-bottom: 20px;
    }

    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #555; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; letter-spacing: 2px; z-index: 999; font-family: 'Montserrat', sans-serif; text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. DATA LOAD & CONFIG
# -----------------------------------------------------------------------------
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

PODCAST_SCRIPT = {
    "I. INTRODUCTION: RECESSION GLAM": {
        "start_time": 0, "filter": "None",
        "desc": "Analysis of fragrance as 'affordable luxury' in the 2026 economic landscape. Substitution effect in full force."
    },
    "II. SCENT TREND: GOURMAND 2.0": {
        "start_time": 571, "filter": "Notes_Gourmand",
        "desc": "The evolution from sugar-sweet scents to balanced, sophisticated edible notes (Pistachio, Salted Caramel)."
    },
    "III. MARKET FOCUS: RUSSIA & DUHI": {
        "start_time": 1433, "filter": "Market_Russia",
        "desc": "Strategic insights into local production and high-concentration status symbols in the RU market."
    }
}

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 3. HEADER & KPI SECTION
# -----------------------------------------------------------------------------
st.markdown("<h1>Fragrance Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Global Trends • Market Sentiment • Strategic Forecast 2026</div>", unsafe_allow_html=True)

# KPIS
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="gold-metric"><div class="metric-label">Market Valuation</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="gold-metric"><div class="metric-label">Growth Driver</div><div class="metric-value">23% Scent</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="gold-metric"><div class="metric-label">Regional Share (RU)</div><div class="metric-value">68% Local</div></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. TABBED INTERFACE
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🎙️ STRATEGIC BRIEFING", "📊 DEEP DIVE ANALYTICS", "🔗 METHODOLOGY & ECOSYSTEM"])

# --- TAB 1: STORY MODE (AUDIO + AUTO CHART) ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large") 
    
    # 1. LEFT COLUMN - AUDIO & CONTROLS
    with col_audio:
        st.markdown("### 🎧 AI-Synthesized Market Report")
        selected_chapter = st.radio("Select Chapter to Navigate Audio:", list(PODCAST_SCRIPT.keys()))
        chapter_data = PODCAST_SCRIPT[selected_chapter]
        
        st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
        
        st.markdown(f"""
            <div class="insight-card">
                <p style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
                <p style="font-style:italic; color:#e0e0e0; font-size:1.1rem; line-height:1.6; font-family:'Playfair Display', serif;">"{chapter_data['desc']}"</p>
            </div>
        """, unsafe_allow_html=True)

    # 2. RIGHT COLUMN - AUTO CHART (STORY MODE)
    with col_viz:
        st.markdown(f"### 📉 Data Visualization: {selected_chapter.split(':')[1]}")
        
        if not df.empty:
            # AUTOMATIC FILTERING BASED ON CHAPTER
            df_story = df.copy()
            
            if chapter_data["filter"] == "Notes_Gourmand" and 'top_notes' in df_story.columns:
                df_story = df_story[df_story['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
                chart_title = "Trending Gourmand 2.0 Clusters"
            elif chapter_data["filter"] == "Market_Russia" and 'country' in df_story.columns:
                df_story = df_story[df_story['country'] == 'Russia']
                chart_title = "Russian Market Landscape (High Concentration)"
            else:
                chart_title = "Global Market Overview (All Data)"
            
            # CHART
            fig = px.scatter(
                df_story, x="year_clean", y="community_score", size="community_votes",
                color="segment", hover_name="name", template="plotly_dark",
                color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'],
                title=chart_title
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_family="Montserrat", height=450,
                xaxis=dict(title="Launch Year", gridcolor="#222"),
                yaxis=dict(title="Sentiment Score", gridcolor="#222")
            )
            st.plotly_chart(fig, use_container_width=True)
            
        else:
            st.error("Data loading error.")

# --- TAB 2: ANALYST MODE (MANUAL EXPLORATION) ---
with tab2:
    st.markdown("### 📈 Deep Dive Analytics (Manual Exploration)")
    
    if not df.empty:
        # Styled Filter Box
        filter_option = st.selectbox("Filter Data View:", ["Show All Global Data", "Focus: Gourmand 2.0 Notes", "Focus: Russian Market"])
        
        df_plot = df.copy()
        if filter_option == "Focus: Gourmand 2.0 Notes" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
        elif filter_option == "Focus: Russian Market" and 'country' in df_plot.columns:
            df_plot = df_plot[df_plot['country'] == 'Russia']

        # Chart
        fig = px.scatter(
            df_plot, x="year_clean", y="community_score", size="community_votes",
            color="segment", hover_name="name", template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#666']
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_family="Montserrat", height=500,
            xaxis=dict(title="Launch Year", gridcolor="#222"),
            yaxis=dict(title="Sentiment Score", gridcolor="#222")
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # HTML TABLE (Guarantees black background)
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 ROWS)"):
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns: cols_to_show.append('top_notes')
            html_table = df_plot[cols_to_show].head(50).to_html(classes='luxury-table', index=False, border=0)
            st.markdown(html_table, unsafe_allow_html=True)

    else:
        st.error("Data could not be loaded.")

# --- TAB 3: ECOSYSTEM (FIXED) ---
with tab3:
    st.markdown("### 🧩 The Fragrance Data Ecosystem")
    st.markdown("This hub serves as the central command for my deployed machine learning applications. Launch a tool below:")
    
    # CSS + HTML Combined Block for Safety
    st.markdown("""
    <style>
    .project-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-top: 20px;
    }
    .project-card {
        background-color: #0e0e0e;
        border: 1px solid #333;
        padding: 20px;
        border-radius: 4px;
        transition: 0.3s;
    }
    .project-card:hover {
        border-color: #D4AF37;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
    }
    .project-title {
        color: #D4AF37;
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        margin-bottom: 5px;
    }
    .project-desc {
        color: #888;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.8rem;
        margin-bottom: 20px;
        min-height: 40px;
    }
    .btn-row {
        display: flex;
        gap: 10px;
    }
    
    /* BUTTON STYLES */
    a.btn-launch {
        display: block;
        flex: 1;
        background-color: #D4AF37;
        color: #000000 !important;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.75rem;
        border-radius: 2px;
        transition: 0.3s;
        border: 1px solid #D4AF37;
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
    }
    a.btn-launch:hover {
        background-color: #F0E68C;
        border-color: #F0E68C;
        box-shadow: 0 0 10px #D4AF37;
        color: #000 !important;
    }
    
    a.btn-code {
        display: block;
        flex: 1;
        background-color: transparent;
        color: #888888 !important;
        border: 1px solid #444;
        padding: 10px;
        text-align: center;
        text-transform: uppercase;
        font-size: 0.75rem;
        border-radius: 2px;
        transition: 0.3s;
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
    }
    a.btn-code:hover {
        border-color: #D4AF37;
        color: #D4AF37 !important;
    }
    </style>
    
    <div class="project-container">
        
        <div class="project-card">
            <div class="project-title">🌍 Aromo Intelligence</div>
            <div class="project-desc">Global market scraping engine & trend forecasting dashboard covering 50k+ products.</div>
            <div class="btn-row">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">🔍 Perfume Finder</div>
            <div class="project-desc">Consumer-facing recommendation system using similarity algorithms for retail.</div>
            <div class="btn-row">
                <a href="#" target="_blank" class="btn-launch">🚀 Launch App</a>
                <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" target="_blank" class="btn-code">💻 View Code</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">📊 Olfactory Insights</div>
            <div class="project-desc">Deep learning analysis of scent structures and chemical composition mapping.</div>
            <div class="btn-row">
                <a href="https://github.com/MagdalenaRomaniecka/Olfactory-Insights" target="_blank" class="btn-code" style="width:100%">💻 View Code</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">🧪 ScentSational LFS</div>
            <div class="project-desc">Backend engineering pipeline & Large File Storage documentation.</div>
            <div class="btn-row">
                <a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" target="_blank" class="btn-code" style="width:100%">💻 View Code</a>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    col_source, col_blank = st.columns([1,1])
    with col_source:
         st.markdown("### 📚 Primary Intelligence Sources")
         st.markdown("""
         * **[1] Euromonitor International:** *Beauty and Personal Care 2025 Edition*
         * **[2] Givaudan:** *2024 Half Year Results & Integrated Report*
         * **[3] Journal of Retailing:** *Pricing vs. Sales correlation analysis*
         """)
         st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="repo-btn" style="border-color:#D4AF37; color:#D4AF37; text-align:center;"><b>📄 View Research Notebook (Colab)</b></a>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. FOOTER & TRANSCRIPT
# -----------------------------------------------------------------------------
st.write("")
st.write("")
st.write("")

with st.expander("📄 READ FULL STRATEGIC TRANSCRIPT"):
    try:
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            st.markdown(f.read())
    except:
        st.info("Transcript file currently unavailable.")

st.markdown("""
    <div class="footer">
        DATA SOURCE: FRAGRANTICA (KAGGLE) & NOTEBOOKLM INSIGHTS <br>
        © 2026 DEVELOPED BY <a href="https://github.com/MagdalenaRomaniecka" target="_blank">MAGDALENA ROMANIECKA</a> • STRATEGIC INSIGHTS
    </div>
""", unsafe_allow_html=True)