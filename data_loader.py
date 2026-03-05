import pandas as pd
import numpy as np

def load_and_merge_data():
    """
    Simulation of professional data loading from multiple sources (e.g., API, SQL databases).
    Replaced placeholders with real-world case studies to prove analytical trends 
    (Trickle-Down Effect, Neuro-Perfumery, Functional Fragrance).
    """
    
    # Main database: Global hits and trend representatives
    data = {
        'fragrance_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'name': [
            'Sol de Janeiro Cheirosa 62', 
            'Paco Rabanne Phantom', 
            'The Nue Co. Functional Fragrance', 
            'Tom Ford Lost Cherry',
            'Kayali Lovefest Burning Cherry',
            'Zara Cherry Smoothie',
            'Zara Red Temptation',
            'Faberlic Russian Beauty',
            'Novaya Zarya Red Moscow',
            'Dior Sauvage',
            'Maison Francis Kurkdjian Baccarat Rouge 540',
            'Eisenberg Diabolique',
            'Ariana Grande Cloud',
            'YSL Black Opium',
            'Byredo Super Cedar'
        ],
        'brand': [
            'Sol de Janeiro', 
            'Paco Rabanne', 
            'The Nue Co.', 
            'Tom Ford',
            'Kayali',
            'Zara',
            'Zara',
            'Faberlic',
            'Novaya Zarya',
            'Dior',
            'Maison Francis Kurkdjian',
            'Eisenberg',
            'Ariana Grande',
            'Yves Saint Laurent',
            'Byredo'
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
        'release_year': [2020, 2021, 2018, 2018, 2022, 2022, 2020, 2015, 1925, 2015, 2015, 2010, 2018, 2014, 2016],
        'top_notes': [
            'Pistachio, Salted Caramel, Vanilla (Gourmand 2.0)',
            'Lavender, Lemon, Styrallyl Acetate (Neuro-Perfumery / AI)',
            'Green Cardamom, Iris, Palo Santo (Anti-Stress / Functional)',
            'Black Cherry, Bitter Almond, Liqueur (Vamp Romantic)',
            'Burning Cherry, Raspberry, Praline (Vamp Romantic)',
            'Cherry, Plum, Vanilla (Mass-Market Vamp)',
            'Saffron, Bitter Almond, Jasmine (Baccarat Clone)',
            'Floral Notes, Musk, Woody Notes (Russian Market)',
            'Carnation, Rose, Coriander (Russian Heritage)',
            'Bergamot, Pepper, Amberwood (Fresh Spicy)',
            'Saffron, Jasmine, Ambergris (Luxury Sweet)',
            'Yellow Mandarin, Cardamom, Iris (Niche Powdery)',
            'Lavender, Pear, Praline, Vanilla (Celeb Gourmand)',
            'Coffee, Vanilla, White Flowers (Prestige Gourmand)',
            'Rose, Virginian Cedar, Vetiver (Minimalist Wood)'
        ],
        'country': [
            'USA', 'France', 'UK', 'USA', 'UAE', 'Spain', 'Spain', 'Russia', 'Russia', 'France', 'France', 'France', 'USA', 'France', 'Sweden'
        ]
    }
    
    df_main = pd.DataFrame(data)
    
    # Community database (Simulating scraped data from portals like Fragrantica)
    community_data = {
        'fragrance_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'community_score': [4.5, 3.8, 4.2, 4.3, 4.1, 3.9, 4.0, 3.7, 3.9, 4.1, 4.6, 4.4, 4.2, 4.0, 4.3],
        'community_votes': [1250, 850, 320, 1100, 650, 950, 1050, 450, 520, 2100, 1800, 280, 1500, 1950, 700]
    }
    
    df_community = pd.DataFrame(community_data)
    
    # Merging datasets
    df_merged = pd.merge(df_main, df_community, on='fragrance_id', how='left')
    
    # Adding artificial noise for better realism during local testing (optional)
    np.random.seed(42)
    df_merged['price_usd'] = np.random.randint(25, 350, size=len(df_merged))
    
    return df_merged

if __name__ == "__main__":
    # Testing the data loader
    df = load_and_merge_data()
    print("Data loaded successfully. Shape:", df.shape)
    print(df.head())