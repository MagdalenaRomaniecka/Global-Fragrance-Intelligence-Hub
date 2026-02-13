import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_and_merge_data():
    """
    Loads market data and sentiment data.
    If files are missing, it generates dummy data so the app doesn't crash.
    """
    try:
        # 1. Define paths to your data
        market_path = "assets/data/market_data.csv"
        sentiment_path = "assets/data/sentiment_data.csv"

        # 2. Check if files exist
        if os.path.exists(market_path):
            # Load real data if available
            df = pd.read_csv(market_path)
            # Ensure year is numeric
            if 'year' in df.columns:
                 df['year_clean'] = pd.to_numeric(df['year'], errors='coerce').fillna(0).astype(int)
            return df
        
        else:
            # 3. FALLBACK: Generate Dummy Data (Safe Mode)
            # This ensures your app works immediately, even without CSV files.
            data = {
                "display_name": ["Baccarat Rouge 540", "Lost Cherry", "Santal 33", "Black Opium", "Cloud", "Bianco Latte"],
                "brand": ["Maison Francis Kurkdjian", "Tom Ford", "Le Labo", "YSL", "Ariana Grande", "Giardini Di Toscana"],
                "segment": ["Niche", "Luxury", "Niche", "Mass-Market", "Mass-Market", "Niche"],
                "year": ["2015", "2018", "2011", "2014", "2018", "2023"],
                "year_clean": [2015, 2018, 2011, 2014, 2018, 2023],
                "community_score": [4.2, 3.9, 4.1, 3.8, 4.0, 4.5],