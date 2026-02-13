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

# --- 2. UPDATED AUDIO URL (Pointing to Root) ---
# Since your file is in the root, we removed '/assets/audio/' from the link
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

# --- 3. TIMESTAMPS (Verified from your analysis) ---
PODCAST_SCRIPT = {
    "1. Intro: The 'Recession Glam' Concept": {
        [cite_start]"start_time": 160, # [cite: 5]
        "filter_type": "None",
        [cite_start]"description": "Fragrance as 'affordable luxury' in the 2026 economic landscape. [cite: 23]"
    },
    "2. Scent Trend: Gourmand 2.0 (Vanilla)": {
        [cite_start]"start_time": 571, # [cite: 8]
        "filter_type": "Notes_Gourmand",
        [cite_start]"description": "Beyond sweet: The shift to balanced, high-end edible notes. [cite: 116]"
    },
    "3. Market Focus: Russia & The 'Duhi' Shift": {
        [cite_start]"start_time": 1433, # [cite: 12]
        "filter_type": "Market_Russia",
        [cite_start]"description": "Strategic insights into the Russian market and local 'Duhi' production. [cite: 272]"
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

with col_info:
    st.markdown(f"### 💡 Key Insight: {selected}")
    st.info(data["description"])
    
    # Filter Logic
    df_view = df.copy()
    if not df_view.empty:
        if data['filter_type'] == "Market_Russia":
            if 'segment' in df_view.columns:
                df_view = df_view[df_view['segment'].isin(['Mass-Market', 'Local'])]
        elif data['filter_type'] == "Notes_Gourmand":
            if 'top_notes' in df_view.columns:
                df_view = df_view[df_view['top_notes'].str.contains('Vanilla|Sugar|Caramel', case=False, na=False)]

# --- 4. EXECUTIVE SUMMARY ---
st.divider()
with st.expander("📄 View Executive Summary"):
    st.markdown("""
    #### 🎙️ Podcast Insights (Deep Dive 2026)
    * [cite_start]**Recession Glam:** Market reached **$593 billion** in 2024[cite: 18].
    * [cite_start]**Fragrance Effect:** Category driving **23%** of all beauty growth[cite: 30].
    * [cite_start]**Givaudan:** Using AI to digitize smell and improve focus[cite: 37, 182].
    * [cite_start]**Russia:** Local brands like **Faberlic** hold **68%** market share[cite: 270, 274].
    """)

# --- 5. DATA VISUALIZATION ---
st.divider()
st.subheader("📊 Market Sentiment vs. Community Scoring")
if not df_view.empty:
    fig = px.scatter(df_view, x="year_clean", y="community_score", size="community_votes", 
                     color="segment", hover_name="name", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please ensure fragrance_data.csv is uploaded to the root folder.")