import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI CONFIGURATION & LUXURY ATELIER CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

# FORCE DARK THEME & CUSTOM FONTS
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;500&display=swap');

    /* --- GLOBAL APP STYLING --- */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        color: #E0E0E0 !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* --- TYPOGRAPHY --- */
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important; /* More aesthetic/luxury than Garamond */
        letter-spacing: 2px;
    }
    
    h1 {
        background: linear-gradient(to right, #D4AF37 20%, #F0E68C 50%, #D4AF37 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem !important;
        text-transform: uppercase;
        margin-bottom: 0px;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.3);
    }
    
    .sub-header {
        color: #888;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85rem !important;
        letter-spacing: 4px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 40px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
        padding-bottom: 20px;
    }

    /* --- WIDGET OVERRIDES (Fixing White Backgrounds) --- */
    
    /* Selectbox & Inputs */
    div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {
        background-color: rgba(25, 25, 25, 0.8) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        color: white !important;
    }
    div[data-baseweb="popover"] {
        background-color: #1a1a1a !important;
    }
    
    /* Expanders (Fixing White Box) */
    .st-emotion-cache-1h9usn1, .st-emotion-cache-12w0qpk, details {
        background-color: rgba(20, 20, 20, 0.5) !important;
        border: 1px solid rgba(212, 175, 55, 0.1) !important;
        border-radius: 5px;
        color: #E0E0E0 !important;
    }

    /* Dataframe Styling */
    [data-testid="stDataFrame"] {
        border: 1px solid #333;
        background-color: #0e0e0e;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border: none;
        color: #888;
        font-family: 'Cinzel', serif;
        font-weight: 700;
        font-size: 1rem;
    }
    .stTabs [aria-selected="true"] {
        color: #D4AF37 !important;
        border-bottom: 2px solid #D4AF37 !important;
    }

    /* --- COMPONENT CLASSES --- */
    .insight-card {
        border-left: 3px solid #D4AF37;
        background: linear-gradient(90deg, rgba(20,20,20,0.8) 0%, rgba(30,30,30,0.4) 100%);
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 0px 5px 5px 0px;
    }

    .gold-metric {
        background-color: rgba(10, 10, 10, 0.6);
        border: 1px solid #333;
        padding: 20px;
        text-align: center;
        border-radius: 2px;
        transition: all 0.3s ease;
    }
    .gold-metric:hover {
        border-color: #D4AF37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
    }
    .metric-label { color: #888; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;}
    .metric-value { font-family: 'Cinzel', serif; font-size: 2rem; color: #F0E68C; }

    /* --- FOOTER --- */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000000;
        color: #666;
        text-align: center;
        padding: 10px;
        font-size: 0.7rem;
        border-top: 1px solid #222;
        letter-spacing: 1px;
        z-index: 100;
    }
    .footer a { color: #D4AF37; text-decoration: none; }
    
    /* Repo Link Button */
    .repo-btn {
        display: block;
        width: 100%;
        padding: 10px;
        background: transparent;
        border: 1px solid #444;
        color: #bbb;
        text-align: center;
        text-decoration: none;
        border-radius: 4px;
        margin-bottom: 10px;
        transition: 0.3s;
        font-size: 0.8rem;
    }
    .repo-btn:hover {
        border-color: #D4AF37;
        color: #D4AF37;
        background: rgba(212, 175, 55, 0.05);
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
        "desc": "Analysis of fragrance as 'affordable luxury' in the 2026 economic landscape."
    },
    "II. SCENT TREND: GOURMAND 2.0": {
        "start_time": 571, "filter": "Notes_Gourmand",
        "desc": "The evolution from sugar-sweet scents to balanced, sophisticated edible notes."
    },
    "III. MARKET FOCUS: RUSSIA & DUHI": {
        "start_time": 1433, "filter": "Market_Russia",
        "desc": "Strategic insights into local production and high-concentration status symbols."
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

# --- TAB 1: BRIEFING (AUDIO FOCUSED) ---
with tab1:
    col_audio, col_desc = st.columns([1, 1], gap="large")
    
    with col_audio:
        st.markdown("### 🎧 AI-Synthesized Market Report")
        selected_chapter = st.radio("Select Chapter to Navigate Audio:", list(PODCAST_SCRIPT.keys()))
        chapter_data = PODCAST_SCRIPT[selected_chapter]
        st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
    
    with col_desc:
        st.markdown("### 📝 Chapter Insight")
        st.markdown(f"""
            <div class="insight-card">
                <p style="color:#D4AF37; font-size:0.85rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
                <p style="font-style:italic; color:#e0e0e0; font-size:1.05rem; line-height:1.6;">{chapter_data['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Mini-preview metric
        if chapter_data["filter"] != "None" and not df.empty:
            count = 0
            if 'top_notes' in df.columns and chapter_data["filter"] == "Notes_Gourmand":
                count = df[df['top_notes'].str.contains('Vanilla|Caramel|Pistachio', case=False, na=False)].shape[0]
                label = "Gourmand SKUs Tracked"
            elif 'country' in df.columns and chapter_data["filter"] == "Market_Russia":
                count = df[df['country'] == 'Russia'].shape[0]
                label = "Local Market SKUs"
            else:
                label = "Data Points"
            
            st.markdown(f"**{label}:** <span style='color:#D4AF37; font-size:1.2rem;'>{count}</span>", unsafe_allow_html=True)


# --- TAB 2: ANALYTICS (CHARTS FOCUSED) ---
with tab2:
    st.markdown("### 📈 Market Sentiment & Clustering")
    
    if not df.empty:
        # Filter controls
        filter_option = st.selectbox("Filter Data View:", ["Show All Global Data", "Focus: Gourmand 2.0 Notes", "Focus: Russian Market"])
        
        df_plot = df.copy()
        
        # Safe filtering
        if filter_option == "Focus: Gourmand 2.0 Notes" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
        elif filter_option == "Focus: Russian Market" and 'country' in df_plot.columns:
            df_plot = df_plot[df_plot['country'] == 'Russia']

        # BIG CHART
        fig = px.scatter(
            df_plot, 
            x="year_clean", 
            y="community_score", 
            size="community_votes",
            color="segment", 
            hover_name="name", 
            template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'],
            title=""
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="Montserrat", 
            height=500,
            xaxis=dict(title="Launch Year", gridcolor="#222", zeroline=False),
            yaxis=dict(title="Sentiment Score (5.0 Scale)", gridcolor="#222", zeroline=False),
            legend=dict(orientation="h", y=1.1)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # DATA TABLE
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 ROWS)"):
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns:
                cols_to_show.append('top_notes')
            
            # Using specific config to try and darken the table (Streamlit theme dependent)
            st.dataframe(df_plot[cols_to_show].head(50), use_container_width=True, height=300)
    else:
        st.error("Data could not be loaded.")


# --- TAB 3: ECOSYSTEM & SOURCES ---
with tab3:
    col_eco, col_source = st.columns(2)
    
    with col_eco:
        st.markdown("### 🧩 The Fragrance Data Ecosystem")
        st.markdown("This project is part of a larger interconnected portfolio of olfactory data tools:")
        
        st.markdown("""
        <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" class="repo-btn">
        🌍 <b>Aromo Market Intelligence</b><br>Global market scraping & trend forecasting engine
        </a>
        
        <a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" class="repo-btn">
        🧪 <b>ScentSational LFS</b><br>Large File Storage & Data Engineering pipeline
        </a>

        <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" class="repo-btn">
        🔍 <b>Perfume Finder App</b><br>Consumer-facing recommendation system
        </a>
        """, unsafe_allow_html=True)

    with col_source:
        st.markdown("### 📚 Primary Intelligence Sources")
        st.markdown("""
        The insights in the briefing are synthesized from the following key documents (via NotebookLM):
        
        * **[1] Euromonitor International:** *Beauty and Personal Care 2025 Edition* (Global Market Sizes).
        * **[2] Givaudan:** *2024 Half Year Results & Integrated Report* (Functional Fragrance Technologies).
        * **[3] Journal of Retailing / eBay Study:** *"Unravelling Men's Fragrance Preferences"* (Pricing vs. Sales correlation analysis).
        * **[4] Sol de Janeiro:** *Brand Investor Presentation* (Scent Stacking methodology).
        """)
        
        st.markdown("---")
        st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="repo-btn" style="border-color:#D4AF37; color:#D4AF37;">📄 View Research Notebook (Colab)</a>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. FOOTER & TRANSCRIPT
# -----------------------------------------------------------------------------
st.write("")
st.write("")
st.write("")

# EXPANDER FOR TRANSCRIPT
with st.expander("📄 READ FULL STRATEGIC TRANSCRIPT"):
    try:
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            st.markdown(f.read())
    except:
        st.info("Transcript file currently unavailable.")

# FIXED FOOTER
st.markdown("""
    <div class="footer">
        DATA SOURCE: FRAGRANTICA (KAGGLE) & NOTEBOOKLM INSIGHTS <br>
        © 2026 DEVELOPED BY <a href="https://github.com/MagdalenaRomaniecka" target="_blank">MAGDALENA ROMANIECKA</a> • STRATEGIC INSIGHTS
    </div>
""", unsafe_allow_html=True)