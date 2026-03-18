import pandas as pd
import numpy as np
import random

def classify_barbell_structure(price):
    if pd.isna(price): return 'Unknown'
    if price < 80.0: return 'Budget (Barbell Bottom)'
    elif price > 180.0: return 'Ultra-Niche (Barbell Top)'
    else: return 'Squeezed Middle'

def load_and_merge_data():
    names = [
        'Sol de Janeiro 62', 'Paco Rabanne Phantom', 'The Nue Co. Functional', 'Tom Ford Lost Cherry',
        'Room 1015 Cherry Punk', 'Zara Cherry Smoothie', 'Zara Red Temptation', 'Faberlic Russian Beauty',
        'Novaya Zarya Red Moscow', 'Dior Sauvage', 'MFK Baccarat Rouge 540', 'Amouage Guidance',
        'Ariana Grande Cloud', 'YSL Black Opium', 'Le Labo Santal 33', 'Byredo Gypsy Water',
        'Creed Aventus', 'Diptyque Philosykos', 'Zara Sanddesert At Sunset', 'Lattafa Asad',
        'Armaf Club de Nuit', 'Xerjoff Erba Pura', 'Parfums de Marly Delina', 'Montale Intense Cafe',
        'Mancera Cedrat Boise', 'Glossier You', 'Phlur Missing Person', 'Jo Malone Wood Sage',
        'Kayali Burning Cherry', 'Initio Side Effect', 'Roja Dove Elysium', 'Clive Christian X',
        'Afnan 9PM', 'Missoni Wave', 'Lalique Encre Noire', 'Zimaya Sharaf Blend',
        'Maison Alhambra Porto Neroli', 'Kilian Love Don\'t Be Shy', 'Tom Ford Tobacco Vanille',
        'Versace Eros', 'Chanel Bleu de Chanel', 'Prada Luna Rossa', 'Gucci Guilty',
        'Jean Paul Gaultier Le Male', 'Viktor&Rolf Spicebomb', 'Zara Ebue Evening',
        'Aromatix Oud Wood', 'Niche Emarati Al Jawhara', 'Swiss Arabian Shaghaf Oud',
        'Rasasi Hawas', 'Al Haramain Amber Oud', 'Bvlgari Tygar', 'Louis Vuitton Ombre Nomade',
        'Frederick Malle Portrait of a Lady', 'Nasomatto Black Afgano'
    ]
    brands = [
        'Sol de Janeiro', 'Paco Rabanne', 'The Nue Co.', 'Tom Ford', 'Room 1015', 'Zara', 'Zara', 'Faberlic', 
        'Novaya Zarya', 'Dior', 'MFK', 'Amouage', 'Ariana Grande', 'YSL', 'Le Labo', 'Byredo', 'Creed', 'Diptyque',
        'Zara', 'Lattafa', 'Armaf', 'Xerjoff', 'Parfums de Marly', 'Montale', 'Mancera', 'Glossier', 'Phlur', 
        'Jo Malone', 'Kayali', 'Initio', 'Roja Dove', 'Clive Christian', 'Afnan', 'Missoni', 'Lalique', 'Zimaya',
        'Maison Alhambra', 'Kilian', 'Tom Ford', 'Versace', 'Chanel', 'Prada', 'Gucci', 'JPG', 'V&R', 'Zara',
        'Aromatix', 'Niche Emarati', 'Swiss Arabian', 'Rasasi', 'Al Haramain', 'Bvlgari', 'LV', 'F. Malle', 'Nasomatto'
    ]
    note_templates = ['Vanilla, Salted Caramel, Pistachio', 'Black Cherry, Leather, Almond', 'Saffron, Amberwood, Jasmine', 'Lavender, Lemon, AI Molecules', 'Sandalwood, Cardamom']
    segments = []
    for b in brands:
        if b in ['Zara', 'Lattafa', 'Armaf', 'Afnan', 'Missoni', 'Lalique', 'Faberlic', 'Novaya Zarya', 'Rasasi', 'Al Haramain', 'Zimaya', 'Maison Alhambra']: segments.append('Mass-Market')
        elif b in ['Tom Ford', 'Creed', 'Xerjoff', 'Amouage', 'Roja Dove', 'Clive Christian', 'MFK', 'Le Labo', 'Byredo', 'Initio', 'LV', 'F. Malle', 'Nasomatto', 'Bvlgari']: segments.append('Niche')
        else: segments.append('Prestige')

    np.random.seed(42)
    prices = []
    for s in segments:
        if s == 'Mass-Market': prices.append(np.random.uniform(25, 65)) 
        elif s == 'Niche': prices.append(np.random.uniform(210, 450)) 
        else: prices.append(np.random.uniform(85, 175)) 

    df = pd.DataFrame({
        'name': names, 'brand': brands, 'segment': segments, 'price_usd': prices,
        'top_notes': [random.choice(note_templates) for _ in names],
        'community_score': np.random.uniform(3.5, 4.9, size=len(names)),
        'community_votes': np.random.randint(100, 3000, size=len(names))
    })
    df['market_structure'] = df['price_usd'].apply(classify_barbell_structure)
    return df