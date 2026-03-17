import pandas as pd
import numpy as np

def classify_barbell_structure(price):
    if pd.isna(price): return 'Unknown'
    if price < 70.0: return 'Budget (Barbell Bottom)'
    elif price > 150.0: return 'Ultra-Niche (Barbell Top)'
    else: return 'Squeezed Middle'

def load_and_merge_data():
    """
    Simulation of professional data loading from multiple sources (e.g., API, SQL databases).
    Replaced placeholders with real-world case studies to prove analytical trends 
    (Trickle-Down Effect, Neuro-Perfumery, Functional Fragrance).
    """
    
    # Main database: Global hits and pure Niche representatives
    data = {
        'fragrance_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'name': [
            'Sol de Janeiro Cheirosa 62', 
            'Paco Rabanne Phantom', 
            'The Nue Co. Functional Fragrance', 
            'Tom Ford Lost Cherry',
            'Room 1015 Cherry Punk',
            'Zara Cherry Smoothie',
            'Zara Red Temptation',
            'Faberlic Russian Beauty',
            'Novaya Zarya Red Moscow',
            'Dior Sauvage',
            'Maison Francis Kurkdjian Baccarat Rouge 540',
            'Amouage Guidance',
            'Ariana Grande Cloud',
            'YSL Black Opium',
            'Le Labo Santal 33'
        ],
        'brand': [
            'Sol de Janeiro', 
            'Paco Rabanne', 
            'The Nue Co.', 
            'Tom Ford',
            'Room 1015',
            'Zara',
            'Zara',
            'Faberlic',
            'Novaya Zarya',
            'Dior',
            'Maison Francis Kurkdjian',
            'Amouage',
            'Ariana Grande',
            'Yves Saint Laurent',
            'Le Labo'
        ],
        'segment': [
            'Prestige', 
            'Prestige', 
            'Niche', 
            'Prestige',
            'Niche',
            'Mass-Market',
            'Mass-Market',
            'Mass-Market',
            'Mass-Market',
            'Prestige',
            'Niche',
            'Niche',
            'Mass-Market',
            'Prestige',
            'Niche'
        ],
        'release_year': [2020, 2021, 2018, 2018, 2020, 2022, 2020, 2015, 1925, 2015, 2015, 2023, 2018, 2014, 2011],
        'top_notes': [
            'Pistachio, Salted Caramel, Vanilla (Gourmand 2.0)',
            'Lavender, Lemon, Styrallyl Acetate (Neuro-Perfumery / AI)',
            'Green Cardamom, Iris, Palo Santo (Anti-Stress / Functional)',
            'Black Cherry, Bitter Almond, Liqueur (Vamp Romantic)',
            'Cherry, Saffron, Leather (Niche Vamp Romantic)',
            'Cherry, Plum, Vanilla (Mass-Market Vamp)',
            'Saffron, Bitter Almond, Jasmine (Baccarat Clone)',
            'Floral Notes, Musk, Woody Notes (Russian Market)',
            'Carnation, Rose, Coriander (Russian Heritage)',
            'Bergamot, Pepper, Amberwood (Fresh Spicy)',
            'Saffron, Jasmine, Ambergris (Luxury Sweet)',
            'Pear, Hazelnut, Olibanum (Niche Phenomenon)',
            'Lavender, Pear, Praline, Vanilla (Celeb Gourmand)',
            'Coffee, Vanilla, White Flowers (Prestige Gourmand)',
            'Sandalwood, Papyrus, Leather (Cult Niche)'
        ],
        'country': [
            'USA', 'France', 'UK', 'USA', 'France', 'Spain', 'Spain', 'Russia', 'Russia', 'France', 'France', 'Oman', 'USA', 'France', 'USA'
        ]
    }
    
    df_main = pd.DataFrame(data)
    
    # Community database
    community_data = {
        'fragrance_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'community_score': [4.5, 3.8, 4.2, 4.3, 4.4, 3.9, 4.0, 3.7, 3.9, 4.1, 4.6, 4.5, 4.2, 4.0, 4.3],
        'community_votes': [1250, 850, 320, 1100, 450, 950, 1050, 450, 520, 2100, 1800, 890, 1500, 1950, 1600]
    }
    
    df_community = pd.DataFrame(community_data)
    df_merged = pd.merge(df_main, df_community, on='fragrance_id', how='left')
    
    np.random.seed(42)
    df_merged['price_usd'] = np.random.randint(25, 350, size=len(df_merged))
    
    # NEW STRATEGIC DATA FOR EPISODE 3 (BARBELL MARKET)
    europe_brands = ['Paco Rabanne', 'Room 1015', 'Zara', 'Dior', 'Maison Francis Kurkdjian', 'Amouage', 'Yves Saint Laurent']
    df_merged['region'] = df_merged['brand'].apply(lambda x: 'Europe' if x in europe_brands else 'Global')
    df_merged['market_structure'] = df_merged['price_usd'].apply(classify_barbell_structure)
    
    return df_merged

if __name__ == "__main__":
    df = load_and_merge_data()
    print("Data loaded successfully. Shape:", df.shape)