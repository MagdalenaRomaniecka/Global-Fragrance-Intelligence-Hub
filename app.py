import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI CONFIGURATION & LUXURY ATELIER CSS
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

    /* GLOBAL STYLE OVERRIDE */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        color: #E0E0E0 !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    /* LUXURY TYPOGRAPHY */
    h1 {
        font-family: 'Cormorant Garamond', serif !important;
        background: linear-gradient(to bottom, #D4AF37 0%, #F0E68C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.8rem !important;
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-top: -20px;
    }
    
    .sub-header {
        color: #888;
        font-size: 0.85rem !important;
        letter-spacing: 5px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 50px;
    }

    /* CUSTOM CARDS */
    .insight-card {
        border: 1px solid rgba(212, 175, 55, 0.25);
        background: rgba(15, 15, 15, 0.6);
        padding: 25px;
        border-radius: 2px;
        backdrop-filter: blur(15px);
        margin-bottom: 25px;
    }

    /* ATELIER METRICS */
    .gold-metric {
        border-left: 1px solid #D4AF37;
        background-color: rgba(255, 255, 255, 0.02);
        padding: 20px;
        text-align: left;
    }
    .metric-label { color: #D4AF37; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 3px; font-weight: 600; }
    .metric-value { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; color: #F0E68C; line-height: 1; margin-top: 5px; }

    /* UI ELEMENTS */
    .stAudio { background-color: transparent !important; margin-top: 20px; }
    .stExpander { border: 1px solid rgba(212, 175, 55, 0.2) !important; background: rgba(10,10,10,0.8) !important; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SOURCE & DATA CONFIGURATION
# -----------------------------------------------------------------------------
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

PODCAST_SCRIPT = {
    "I. INTRODUCTION: RECESSION GLAM": {
        "start_time": 160, "filter": "None",
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

# -----------------------------------------------------------------------------
# 3. LUXURY INTERFACE
# -----------------------------------------------------------------------------
st.markdown("<h1>Fragrance Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Global Trends • Market Sentiment • Strategic Forecast 2026</div>", unsafe_allow_html=True)

df = load_and_merge_data()

# TOP METRICS ROW
if not df.empty:
    m1, m2, m3 = st.columns(3)
    m1.markdown('<div class="gold-metric"><div class="metric-label">Market Valuation</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
    m2.markdown('<div class="gold-metric"><div class="metric-label">Growth Driver</div><div class="metric-value">23% Scent</div></div>', unsafe_allow_html=True)
    m3.markdown('<div class="gold-metric"><div class="metric-label">Regional Share (RU)</div><div class="metric-value">68% Local</div></div>', unsafe_allow_html=True)

st.write("")

# MAIN ANALYTICS HUB
col_audio, col_viz = st.columns([1, 2], gap="large")

with col_audio:
    st.markdown("<p style='color:#D4AF37; letter-spacing:3px; font-size:0.9rem; font-weight:bold;'>STRATEGIC BRIEFING</p>", unsafe_allow_html=True)
    selected_chapter = st.radio("Chapter Selection", list(PODCAST_SCRIPT.keys()), label_visibility="collapsed")
    
    chapter_data = PODCAST_SCRIPT[selected_chapter]
    st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
    
    st.markdown(f"""
        <div class="insight-card">
            <p style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
            <p style="font-style:italic; color:#BBB; font-size:0.95rem; line-height:1.6;">{chapter_data['desc']}</p>
        </div>
    """, unsafe_allow_html=True)

with col_viz:
    st.markdown("<p style='color:#D4AF37; letter-spacing:3px; font-size:0.9rem; font-weight:bold;'>MARKET SENTIMENT ANALYTICS</p>", unsafe_allow_html=True)
    
    # Filter Logic based on selected chapter
    df_filtered = df.copy()
    if not df_filtered.empty:
        if chapter_data["filter"] == "Notes_Gourmand":
            df_filtered = df_filtered[df_filtered['top_notes'].str.contains('Vanilla|Caramel|Pistachio', case=False, na=False)]
        elif chapter_data["filter"] == "Market_Russia":
            df_filtered = df_filtered[df_filtered['segment'] == 'Local']

        # Styled Plotly Chart
        fig = px.scatter(
            df_filtered, x="year_clean", y="community_score", size="community_votes",
            color="segment", hover_name="name", template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#777']
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_family="Montserrat", 
            margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(title="Launch Year", gridcolor="#222"),
            yaxis=dict(title="Sentiment Score", gridcolor="#222")
        )
        st.plotly_chart(fig, use_container_width=True)

# EXECUTIVE TRANSCRIPT
st.write("")
with st.expander("📄 VIEW EXECUTIVE SUMMARY & TRANSCRIPT"):
    st.markdown("""
    ### 🎙️ Strategic Intelligence Report: Fragrance 2026
    
    **I. Recession Glam & The Fragrance Effect**
    * Substitution of high-ticket assets with high-end scents.
    * Category driving **23%** of all beauty growth worldwide.
    
    **II. Gourmand 2.0 Evolution**
    * Shift from simple 'sugar' profiles to **Sophisticated Indulgence**.
    * Key molecules: Toasted Pistachio, Sea-Salt Caramel, and Smoked Vanilla.
    
    **III. Givaudan's Neural Edge**
    * Implementation of **Cereboost** technology for cognitive performance via scent.
    * **MYRSI System:** Mapping chemical structures to visual color palettes for digital retail.
    
    **IV. Geopolitics & The Russian Market**
    * Closed-loop economic growth due to 35% import duties.
    * Local champions like **Faberlic** and **Novaya Zarya** dominating with 68% share.
    """)