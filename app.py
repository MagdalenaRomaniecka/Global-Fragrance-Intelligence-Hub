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
        margin-bottom: 30px;
    }

    /* TABS STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255,255,255,0.05);
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #D4AF37;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(212, 175, 55, 0.2) !important;
        border-bottom: 2px solid #D4AF37;
        color: #F0E68C !important;
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

    /* METRICS & LINKS */
    .gold-metric {
        border: 1px solid rgba(212, 175, 55, 0.2);
        background-color: rgba(255, 255, 255, 0.02);
        padding: 20px;
        text-align: center;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .metric-label { color: #D4AF37; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 3px; font-weight: 600; margin-bottom: 5px;}
    .metric-value { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: #F0E68C; line-height: 1; }
    
    .repo-link {
        text-decoration: none;
        color: #000;
        background-color: #D4AF37;
        padding: 10px 20px;
        border-radius: 4px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
        transition: 0.3s;
    }
    .repo-link:hover { background-color: #F0E68C; }

    /* UI ELEMENTS */
    .stAudio { background-color: transparent !important; margin-top: 20px; }
    
    /* MARKDOWN TEXT STYLING */
    .stMarkdown p { font-size: 1.05rem; line-height: 1.6; color: #CCCCCC; }
    .stMarkdown h3 { color: #D4AF37 !important; font-family: 'Cormorant Garamond', serif; margin-top: 30px; }
    .stMarkdown strong { color: #F0E68C; font-weight: 600; }
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

# -----------------------------------------------------------------------------
# 4. TABBED INTERFACE
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🎙️ STRATEGIC BRIEFING", "📊 DEEP DIVE ANALYTICS", "🔗 METHODOLOGY & SOURCE"])

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
                <p style="font-style:italic; color:#fff; font-size:1.1rem; line-height:1.6;">{chapter_data['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Mini-preview of data related to chapter
        if chapter_data["filter"] != "None" and not df.empty:
            count = 0
            # Safety check if columns exist before filtering
            if 'top_notes' in df.columns and chapter_data["filter"] == "Notes_Gourmand":
                count = df[df['top_notes'].str.contains('Vanilla|Caramel|Pistachio', case=False, na=False)].shape[0]
                label = "Gourmand Fragrances Analyzed"
            elif 'country' in df.columns and chapter_data["filter"] == "Market_Russia":
                count = df[df['country'] == 'Russia'].shape[0]
                label = "Local Market SKUs Tracked"
            else:
                label = "Data Points"
            
            st.metric(label=label, value=count)


# --- TAB 2: ANALYTICS (CHARTS FOCUSED) ---
with tab2:
    st.markdown("### 📈 Market Sentiment & Clustering")
    
    if not df.empty:
        # Filter controls inside the Analytics tab
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
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#A9A9A9'],
            title=f"Sentiment Analysis: {filter_option}"
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font_family="Montserrat", 
            height=500,
            xaxis=dict(title="Launch Year", gridcolor="#333"),
            yaxis=dict(title="Sentiment Score (5.0 Scale)", gridcolor="#333")
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # DATA TABLE (Fixed: Removed 'brand', kept only safe columns)
        with st.expander("🔎 Inspect Raw Data (Top 50 Rows)"):
            # Select only columns that likely exist
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns:
                cols_to_show.append('top_notes')
            
            st.dataframe(df_plot[cols_to_show].head(50), use_container_width=True)
    else:
        st.error("Data could not be loaded.")


# --- TAB 3: METHODOLOGY (LINKS & TECH) ---
with tab3:
    st.markdown("### 🏗️ Intelligence Architecture & Data Lineage")
    st.markdown("""
    This project demonstrates an **End-to-End Data Science pipeline** applied to the Luxury Beauty sector.
    It connects unstructured audio data with structured market metrics.
    """)
    
    c_tech1, c_tech2 = st.columns(2)
    
    with c_tech1:
        st.markdown("#### 🧠 AI & NLP Layer")
        st.markdown("""
        * **Whisper AI (OpenAI):** Used for high-fidelity transcription of the strategic briefing.
        * **Givaudan 'Neuro-Scent':** Analysis based on proprietary industry reports on *Cereboost* and *Myrissi* technologies.
        """)
        # Link to the Notebook
        st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/blob/main/Research_Whisper_AI.ipynb" class="repo-link" target="_blank">📄 View Research Notebook (Colab)</a>', unsafe_allow_html=True)

    with c_tech2:
        st.markdown("#### 📊 Data Engineering Layer")
        st.markdown("""
        * **Data Sources:** Euromonitor 2025/26 Forecasts, eBay API (Pricing), Fragrantica (Sentiment).
        * **Processing:** Python (Pandas) for cleaning and clustering "Recession Glam" segments.
        * **Visualization:** Streamlit + Plotly Express.
        """)
        # Link to the Main Repo
        st.markdown(f'<a href="https://github.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub" class="repo-link" target="_blank">💻 View Source Code (GitHub)</a>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. TRANSCRIPT FOOTER
# -----------------------------------------------------------------------------
st.write("")
st.markdown("---")
with st.expander("📄 READ FULL TRANSCRIPT"):
    try:
        with open('podcast_transcript.md', 'r', encoding='utf-8') as f:
            st.markdown(f.read())
    except:
        st.info("Transcript file currently unavailable.")