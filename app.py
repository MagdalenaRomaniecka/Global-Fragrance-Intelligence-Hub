import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# --- 1. CONFIG & LUXURY STYLE ---
st.set_page_config(page_title="Fragrance Hub | 2026", layout="wide", page_icon="✨")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Playfair Display', serif; }
    .stAudio { background-color: #1a1c24; border-radius: 15px; padding: 10px; border: 1px solid #d4af37; }
    .stMetric { background-color: #1a1c24; border-radius: 10px; border: 1px solid #d4af37; }
    .stExpander { border: 1px solid #d4af37 !important; background-color: #1a1c24 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AUDIO URL (Update with your username if needed) ---
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/assets/audio/podcast_trends.mp3"

# --- 3. FINAL TIMESTAMPS ---
PODCAST_SCRIPT = {
    "1. Intro: The 'Recession Glam' Concept": {
        "start_time": 160,
        "filter_type": "None",
        "description": "Fragrance as 'affordable luxury' in the 2026 economic landscape."
    },
    "2. Scent Trend: Gourmand 2.0 (Vanilla)": {
        "start_time": 571,
        "filter_type": "Notes_Gourmand",
        "description": "Beyond sweet: The shift from 'Sugar era' to balanced, high-end edible notes."
    },
    "3. Market Focus: Russia & The 'Duhi' Shift": {
        "start_time": 1433,
        "filter_type": "Market_Russia",
        "description": "Strategic insights into the Russian market and local 'Duhi' production."
    }
}

st.title("✨ Global Fragrance Intelligence Hub")

# Load Data
with st.spinner("Syncing Global Intelligence Data..."):
    df = load_and_merge_data()

# Layout
col_audio, col_info = st.columns([1, 2])

with col_audio:
    st.subheader("🎧 Strategic Audio Briefing")
    selected = st.radio("Select Chapter:", list(PODCAST_SCRIPT.keys()))
    data = PODCAST_SCRIPT[selected]
    st.audio(AUDIO_URL, start_time=data["start_time"])
    st.caption("Pro Tip: Navigation syncs with the audio player.")

with col_info:
    st.markdown(f"### 💡 Key Insight: {selected}")
    st.info(data["description"])
    
    # Filter Logic
    df_view = df.copy()
    if data['filter_type'] == "Market_Russia":
        if 'segment' in df_view.columns:
            df_view = df_view[df_view['segment'].isin(['Mass-Market', 'Local'])]
    elif data['filter_type'] == "Notes_Gourmand":
        if 'top_notes' in df_view.columns:
            df_view = df_view[df_view['top_notes'].str.contains('Vanilla|Sugar|Caramel', case=False, na=False)]

# --- 4. LUXURY TRANSCRIPT SECTION ---
st.divider()
with st.expander("📄 View Executive Summary & Transcription"):
    st.markdown("""
    #### 🎙️ Podcast Executive Summary (Deep Dive 2026)
    
    **Phase 1: Recession Glam**
    * Global beauty market: **$593 billion**. 
    * Shift from 'Lipstick Effect' to 'Fragrance Effect' (23% growth driver).
    
    **Phase 2: Gourmand 2.0**
    * Focus on **Balanced Indulgence**. Key notes: Pistachio, Macadamia, and Salted Vanilla.
    * Scent as an "emotional weighted blanket".
    
    **Phase 3: Givaudan & Neuroscience**
    * **Cereboost Technology:** Ginseng-based scents for cognitive focus.
    * **AI MYRSI:** Translating chemical scent formulas into digital color palettes.
    
    **Phase 4: Russia Market Isolation**
    * Impact of 35% import duties. Dominance of **Faberlic** & **Novaya Zarya** (68% share).
    * Shift toward high-concentration "Duhi" as a status symbol.
    """)

# --- 5. DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Market Sentiment vs. Community Scoring")
if not df_view.empty:
    fig = px.scatter(
        df_view, 
        x="year_clean", 
        y="community_score", 
        size="community_votes", 
        color="segment", 
        hover_name="name",
        template="plotly_dark",
        color_discrete_sequence=px.colors.qualitative.Antique
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data found for this specific segment.")