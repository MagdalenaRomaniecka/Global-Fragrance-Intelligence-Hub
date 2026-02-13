import pandas as pd
import streamlit as st
import os

def load_and_merge_data():
    # Looking directly in the root folder now
    file_path = "fragrance_data.csv"
    
    if not os.path.exists(file_path):
        return pd.DataFrame() # Return empty if missing

    try:
        df = pd.read_csv(file_path)
        if 'year' in df.columns:
            df['year_clean'] = pd.to_numeric(df['year'], errors='coerce').fillna(2024).astype(int)
        return df
    except:
        return pd.DataFrame()