import pandas as pd
import streamlit as st
import os

def load_and_merge_data():
    """
    Load data from root or assets folder as a fallback.
    """
    # Try root first, then assets folder
    possible_paths = ["fragrance_data.csv", "assets/fragrance_data.csv"]
    file_path = None

    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    if file_path is None:
        st.error("⚠️ Database Error: 'fragrance_data.csv' not found in root or assets folder.")
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_path)
        # Clean year data
        if 'year' in df.columns:
            df['year_clean'] = pd.to_numeric(df['year'], errors='coerce').fillna(2024).astype(int)
        
        # Clean numeric scores
        for col in ['community_score', 'community_votes']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        return df
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        return pd.DataFrame()