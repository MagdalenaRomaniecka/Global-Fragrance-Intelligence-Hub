import pandas as pd
import streamlit as st
import os

def load_and_merge_data():
    """
    Cleans and loads fragrance data from the local CSV file.
    """
    # Important: Path must match your GitHub structure
    file_path = "assets/fragrance_data.csv"
    
    if not os.path.exists(file_path):
        st.error(f"Data file not found at {file_path}. Please check your GitHub folder.")
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_path)
        
        # Cleaning year
        if 'year' in df.columns:
            df['year_clean'] = pd.to_numeric(df['year'], errors='coerce').fillna(2024).astype(int)
        else:
            df['year_clean'] = 2024
            
        # Ensuring scores are numbers
        for col in ['community_score', 'community_votes']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        return df

    except Exception as e:
        st.error(f"Critical error loading data: {e}")
        return pd.DataFrame()