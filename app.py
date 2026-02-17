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
    
    /* MARKDOWN TEXT STYLING */
    .stMarkdown p { font-size: 1.05rem; line-height: 1.6; color: #CCCCCC; }
    .stMarkdown h3 { color: #D4AF37 !important; font-family: 'Cormorant Garamond', serif; margin-top: 30px; }
    .stMarkdown strong { color: #F0E68C; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SOURCE & DATA CONFIGURATION
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

# -----------------------------------------------------------------------------
# 3. LUXURY INTERFACE STRUCTURE
# -----------------------------------------------------------------------------
st.markdown("<h1>Fragrance Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Global Trends • Market Sentiment • Strategic Forecast 2026</div>", unsafe_allow_html=True)

df = load_and_merge_data()

# TOP METRICS ROW
col1, col2, col3 = st.columns(3)
col1.markdown('<div class="gold-metric"><div class="metric-label">Market Valuation</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
col2.markdown('<div class="gold-metric"><div class="metric-label">Growth Driver</div><div class="metric-value">23% Scent</div></div>', unsafe_allow_html=True)
col3.markdown('<div class="gold-metric"><div class="metric-label">Regional Share (RU)</div><div class="metric-value">68% Local</div></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# MAIN CONTENT: AUDIO & VISUALS
col_audio, col_viz = st.columns([1, 2], gap="large")

with col_audio:
    st.markdown("<p style='color:#D4AF37; letter-spacing:3px; font-size:0.9rem; font-weight:bold;'>STRATEGIC BRIEFING</p>", unsafe_allow_html=True)
    
    # Chapter Selection
    selected_chapter = st.radio("Select Chapter", list(PODCAST_SCRIPT.keys()), label_visibility="collapsed")
    chapter_data = PODCAST_SCRIPT[selected_chapter]
    
    # Audio Player
    st.audio(AUDIO_URL, start_time=chapter_data["start_time"])
    
    # Insight Card
    st.markdown(f"""
        <div class="insight-card">
            <p style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
            <p style="font-style:italic; color:#BBB; font-size:0.95rem; line-height:1.6;">{chapter_data['desc']}</p>
        </div>
    """, unsafe_allow_html=True)

with col_viz:
    st.markdown("<p style='color:#D4AF37; letter-spacing:3px; font-size:0.9rem; font-weight:bold;'>MARKET SENTIMENT ANALYTICS</p>", unsafe_allow_html=True)
    
    if not df.empty:
        # Dynamic Filtering
        df_plot = df.copy()
        if chapter_data["filter"] == "Notes_Gourmand":
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar', case=False, na=False)]
        elif chapter_data["filter"] == "Market_Russia":
            df_plot = df_plot[df_plot['country'] == 'Russia']
        
        # Interactive Bubble Chart
        fig = px.scatter(
            df_plot, 
            x="year_clean", 
            y="community_score", 
            size="community_votes",
            color="segment", 
            hover_name="name", 
            template="plotly_dark",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#A9A9A9']
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="Montserrat", 
            margin=dict(l=0, r=0, t=20, b=0),
            xaxis=dict(title="Launch Year", gridcolor="#333"),
            yaxis=dict(title="Sentiment Score (5.0 Scale)", gridcolor="#333"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Data not loaded. Please check data_loader.py")

# -----------------------------------------------------------------------------
# 4. TRANSCRIPT & EXECUTIVE SUMMARY SECTION
# -----------------------------------------------------------------------------
st.write("")
st.markdown("---")

with st.expander("📄 VIEW FULL STRATEGIC TRANSCRIPT", expanded=False):
    try:
        # Tries to load the Markdown file first (Preferred)
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            transcript_text = f.read()
        st.markdown(transcript_text)
        
    except FileNotFoundError:
        # Fallback if MD file is missing
        st.error("⚠️ Transcript file 'podcast_transcript.md' not found. Please upload it to the repository.")
        st.info("Displaying Executive Summary instead:")
        
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