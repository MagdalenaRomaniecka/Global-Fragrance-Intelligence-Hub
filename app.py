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
    /* IMPORT FONTS: Playfair Display (Luxury Serif) & Lato (Clean Sans) */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700&display=swap');

    /* --- GLOBAL APP STYLING --- */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        color: #E0E0E0 !important;
        font-family: 'Lato', sans-serif !important;
    }

    /* --- LUXURY HEADERS (GRADIENT GOLD & FRAMES) --- */
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
        font-family: 'Lato', sans-serif;
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

    /* --- WIDGET OVERRIDES (THE "WHITE FLASH" FIX) --- */
    
    /* 1. Selectbox & Input Fields - Dark Background */
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #0e0e0e !important;
        border: 1px solid #333 !important;
        color: #D4AF37 !important;
    }
    
    /* 2. DROPDOWN MENU FIX (Killer Feature) */
    ul[data-baseweb="menu"] {
        background-color: #080808 !important;
        border: 1px solid #D4AF37 !important;
    }
    
    /* 3. Dropdown Options */
    li[data-baseweb="option"] {
        color: #bbb !important;
    }
    /* Hover state for options */
    li[data-baseweb="option"]:hover, li[aria-selected="true"] {
        background-color: #D4AF37 !important;
        color: #000 !important;
    }

    /* Expanders */
    .st-emotion-cache-1h9usn1, .st-emotion-cache-12w0qpk, details {
        background-color: rgba(15, 15, 15, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    /* --- LINKS STYLING --- */
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; text-shadow: 0 0 8px #D4AF37; }

    /* --- COMPONENT CLASSES --- */
    .insight-card {
        border: 1px solid rgba(212, 175, 55, 0.3);
        background: linear-gradient(135deg, rgba(20,20,20,0.95) 0%, rgba(10,10,10,0.8) 100%);
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    .gold-metric {
        background-color: rgba(5, 5, 5, 0.5);
        border: 1px solid #222;
        padding: 25px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
    }
    .gold-metric::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 1px;
        background: linear-gradient(90deg, transparent, #D4AF37, transparent);
    }
    .gold-metric:hover {
        background-color: rgba(212, 175, 55, 0.05);
        border-color: #444;
    }
    
    .metric-label { 
        color: #888; font-family: 'Lato', sans-serif; font-size: 0.7rem; 
        text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;
    }
    .metric-value { 
        font-family: 'Playfair Display', serif; font-size: 2.8rem; color: #F0E68C; 
        background: linear-gradient(to bottom, #FCF6BA, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* --- FOOTER --- */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #000; color: #555; text-align: center;
        padding: 12px; font-size: 0.65rem; border-top: 1px solid #111;
        letter-spacing: 2px; z-index: 999; font-family: 'Lato', sans-serif;
        text-transform: uppercase;
    }
    .footer a { color: #888 !important; font-weight: bold; }
    .footer a:hover { color: #D4AF37 !important; }
    
    /* REPO BUTTONS */
    .repo-btn {
        display: block; width: 100%; padding: 15px;
        background: #0a0a0a; border: 1px solid #222;
        color: #ccc !important; text-align: left;
        margin-bottom: 15px; transition: 0.3s; font-family: 'Lato', sans-serif;
    }
    .repo-btn:hover {
        border-color: #D4AF37; color: #D4AF37 !important; transform: translateX(5px);
    }
    .repo-btn b { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #fff; }
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

# --- TAB 1: BRIEFING ---
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
                <p style="color:#D4AF37; font-size:0.75rem; letter-spacing:2px; font-weight:bold; text-transform:uppercase;">Key Narrative</p>
                <p style="font-style:italic; color:#e0e0e0; font-size:1.1rem; line-height:1.6; font-family:'Playfair Display', serif;">"{chapter_data['desc']}"</p>
            </div>
        """, unsafe_allow_html=True)
        
        if chapter_data["filter"] != "None" and not df.empty:
            count = 0
            if 'top_notes' in df.columns and chapter_data["filter"] == "Notes_Gourmand":
                count = df[df['top_notes'].str.contains('Vanilla|Caramel|Pistachio', case=False, na=False)].shape[0]
                label = "Gourmand SKUs"
            elif 'country' in df.columns and chapter_data["filter"] == "Market_Russia":
                count = df[df['country'] == 'Russia'].shape[0]
                label = "Local Market SKUs"
            else:
                label = "Data Points"
            st.markdown(f"**{label}:** <span style='color:#D4AF37; font-size:1.5rem; font-family:Playfair Display;'>{count}</span>", unsafe_allow_html=True)

# --- TAB 2: ANALYTICS ---
with tab2:
    st.markdown("### 📈 Market Sentiment & Clustering")
    
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
            font_family="Lato", height=500,
            xaxis=dict(title="Launch Year", gridcolor="#222"),
            yaxis=dict(title="Sentiment Score", gridcolor="#222")
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # TABLE FIX: USING PANDAS STYLER TO FIX WHITE BACKGROUND
        with st.expander("🔎 INSPECT RAW DATA (TOP 50 ROWS)"):
            cols_to_show = ['name', 'segment', 'community_score']
            if 'top_notes' in df_plot.columns: cols_to_show.append('top_notes')
            
            # Prepare styled dataframe for dark mode
            df_display = df_plot[cols_to_show].head(50)
            st.dataframe(
                df_display.style.set_properties(**{
                    'background-color': '#0e0e0e',
                    'color': '#cccccc',
                    'border-color': '#333333'
                }).map(lambda x: 'color: #D4AF37' if isinstance(x, str) or isinstance(x, float) else ''),
                use_container_width=True, height=300
            )
    else:
        st.error("Data could not be loaded.")

# --- TAB 3: ECOSYSTEM ---
with tab3:
    col_eco, col_source = st.columns(2)
    with col_eco:
        st.markdown("### 🧩 The Fragrance Data Ecosystem")
        st.markdown("""
        <a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" class="repo-btn" target="_blank">
        <b>🌍 Aromo Market Intelligence</b><br>Global market scraping & trend forecasting engine
        </a>
        <a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" class="repo-btn" target="_blank">
        <b>🧪 ScentSational LFS</b><br>Large File Storage & Data Engineering pipeline
        </a>
        <a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" class="repo-btn" target="_blank">
        <b>🔍 Perfume Finder App</b><br>Consumer-facing recommendation system
        </a>
        <a href="https://github.com/MagdalenaRomaniecka/Olfactory-Insights" class="repo-btn" target="_blank">
        <b>📊 Olfactory Insights</b><br>Deep learning analysis of scent structures
        </a>
        """, unsafe_allow_html=True)

    with col_source:
        st.markdown("### 📚 Primary Intelligence Sources")
        st.markdown("""
        * **[1] Euromonitor International:** *Beauty and Personal Care 2025 Edition*
        * **[2] Givaudan:** *2024 Half Year Results & Integrated Report*
        * **[3] Journal of Retailing / eBay Study:** *"Unravelling Men's Fragrance Preferences"*
        * **[4] Sol de Janeiro:** *Brand Investor Presentation*
        """)
        st.markdown("---")
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