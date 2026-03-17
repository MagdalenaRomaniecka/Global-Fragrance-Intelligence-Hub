import pandas as pd
import numpy as np

def classify_barbell_structure(price):
    """
    Classifies the product into the Barbell Market structure based on pricing.
    - Below $30: Budget (Barbell Bottom)
    - Above $150: Ultra-Niche (Barbell Top)
    - Between $30 and $150: Squeezed Middle
    """
    if pd.isna(price):
        return 'Unknown'
    
    if price < 30.0:
        return 'Budget (Barbell Bottom)'
    elif price > 150.0:
        return 'Ultra-Niche (Barbell Top)'
    else:
        return 'Squeezed Middle'

def load_and_merge_data():
    """
    Main ETL function. 
    Loads datasets, aligns schemas, filters outliers, and assigns strategic categories.
    """
    
    # ---------------------------------------------------------
    # MOCK DATA FOR THE DASHBOARD
    # Replace this block with pd.read_csv('your_kaggle_file.csv') 
    # if you are loading external files.
    # ---------------------------------------------------------
    data = {
        'name': ['Cheirosa 62', 'Baccarat Rouge 540', 'Sauvage', 'Polish Niche 1', 'Cheap Mist', 'Chanel No 5', 'Budget Polish', 'Acqua di Gio', 'La Vie Est Belle'],
        'brand': ['Sol de Janeiro', 'Maison Francis Kurkdjian', 'Dior', 'Bohoboco', 'Bodycology', 'Chanel', 'La Rive', 'Giorgio Armani', 'Lancome'],
        'price_usd': [38.0, 325.0, 120.0, 180.0, 15.0, 160.0, 12.0, 90.0, 110.0],
        'community_score': [4.5, 4.8, 4.2, 4.6, 3.8, 4.7, 3.5, 4.4, 4.3],
        'community_votes': [15000, 25000, 30000, 1200, 5000, 40000, 800, 22000, 18000],
        'segment': ['Mass-Premium', 'Ultra-Niche', 'Designer', 'Ultra-Niche', 'Budget', 'Luxury', 'Budget', 'Designer', 'Designer']
    }
    df = pd.DataFrame(data)

    # 1. APPLY EUROPEAN REGIONAL FLAG
    europe_brands = [
        'Chanel', 'Dior', 'Bohoboco', 'Piotr Czarnecki', 
        'Maison Francis Kurkdjian', 'Versace', 'La Rive', 'Lancome', 'Giorgio Armani'
    ]
    df['region'] = df['brand'].apply(lambda x: 'Europe' if x in europe_brands else 'Global')

    # 2. APPLY BARBELL MARKET CLASSIFICATION
    if 'price_usd' in df.columns:
        df['market_structure'] = df['price_usd'].apply(classify_barbell_structure)
    else:
        df['market_structure'] = 'Unknown'

    return df