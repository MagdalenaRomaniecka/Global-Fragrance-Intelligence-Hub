import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# --- 1. SETTINGS & STYLE ---
st.set_page_config(page_title="Fragrance Hub 2026", layout="wide", page_icon="✨")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; }
    .stAudio { border: 1px solid #d4af37; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AUDIO SOURCE ---
# Using the root link as per your GitHub screenshot
AUDIO_URL = "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"

# --- 3. SCRIPT & TIMESTAMPS ---
PODCAST_SCRIPT = {
    "1. Intro: Recession Glam": {"start_time": 160, "filter": "None"},
    "2. Trend: Gourmand 2.0": {"start_time": 571, "filter": "Notes_Gourmand"},
    "3. Market: Russia & Duhi": {"start_time": 1433, "filter": "Market_Russia"}
}

st.title("✨ Global Fragrance Intelligence Hub")

# Load data using our smart loader
df = load_and_merge_data()

# Layout
col_a, col_b = st.columns([1, 2])

with col_a:
    st.subheader("🎧 Briefing")
    chapter = st.radio("Chapter:", list(PODCAST_SCRIPT.keys()))
    st.audio(AUDIO_URL, start_time=PODCAST_SCRIPT[chapter]["start_time"])

with col_b:
    st.info(f"Currently playing: {chapter}")
    # Filtering Logic
    df_filtered = df.copy()
    if not df_filtered.empty:
        if PODCAST_SCRIPT[chapter]["filter"] == "Notes_Gourmand":
            df_filtered = df_filtered[df_filtered['top_notes'].str.contains('Vanilla|Caramel', case=False, na=False)]
        elif PODCAST_SCRIPT[chapter]["filter"] == "Market_Russia":
            df_filtered = df_filtered[df_filtered['segment'] == 'Local']

# --- 4. SUMMARY & TRANSCRIPT ---
with st.expander("📄 View Summary"):
    st.write("Deep dive into Givaudan, Russian market isolation, and the shift to high-concentration scents.")

# --- 5. CHART ---
st.divider()
if not df_filtered.empty:
    fig = px.scatter(df_filtered, x="year_clean", y="community_score", size="community_votes", 
                     color="segment", hover_name="name", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data found to visualize. Check your CSV file content.")