import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI & LUXURY ATELIER CSS (SUPREME ENGLISH EDITION)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Global Deep Background */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #151515 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* Main Luxury Header */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 20px 0; }
    .header-outer { border: 1px solid #444; padding: 8px; display: inline-block; width: 100%; max-width: 650px; }
    .header-inner { border: 1px solid #D4AF37; padding: 30px 60px; text-align: center; background-color: #050505; box-shadow: inset 0 0 20px rgba(212,175,55,0.1); }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 6px; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; margin-top: 10px; font-weight: 300; }
    
    /* Strategic Metrics Boxes */
    .metric-box { border: 1px solid #222; background: rgba(10,10,10,0.8); padding: 20px; text-align: center; transition: 0.4s; height: 100%; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2); transform: translateY(-2px); }
    .metric-label { color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; font-weight: 700; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.9rem; margin: 0; }
    
    /* Section Gold Headers */
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans', sans-serif; 
        font-size: 1.4rem; 
        border-left: 4px solid #D4AF37; 
        padding-left: 20px; 
        margin: 30px 0 20px 0; 
        text-transform: uppercase; 
        letter-spacing: 2px;
    }

    /* TRANSCRIPT & REPORT BOX - GOLD TYPOGRAPHY REINSTATED */
    .transcript-box { 
        font-family: 'Lato', sans-serif; 
        font-size: 1rem; 
        line-height: 1.8; 
        color: #ddd; 
        background: #080808; 
        padding: 40px; 
        border: 1px solid #222; 
        border-radius: 4px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .transcript-box h1 { color: #D4AF37 !important; font-family: 'Tenor Sans', sans-serif !important; font-size: 1.8rem !important; text-align: center; border-bottom: 1px solid #D4AF37; padding-bottom: 15px; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 2px; }
    .transcript-box h2 { color: #F0E68C !important; font-family: 'Tenor Sans', sans-serif !important; font-size: 1.4rem !important; margin-top: 30px; border-left: 3px solid #D4AF37; padding-left: 15px; }
    .transcript-box h3 { color: #D4AF37 !important; font-family: 'Tenor Sans', sans-serif !important; font-size: 1.15rem !important; margin-top: 25px; font-weight: 400; }
    .transcript-box strong { color: #F0E68C; font-weight: 700; }
    .transcript-box p { margin-bottom: 15px; text-align: justify; }

    /* Ecosystem Project Cards */
    .project-card { border: 1px solid #222; background: rgba(15,15,15,0.9); padding: 25px; transition: 0.3s; height: 100%; border-radius: 2px; display: flex; flex-direction: column; justify-content: space-between; }
    .project-card:hover { border-color: #D4AF37; background: #0a0a0a; }
    .btn-launch { 
        display: block; width: 100%; padding: 12px; background: #D4AF37; color: #000 !important; 
        text-align: center; font-weight: bold; text-transform: uppercase; font-size: 0.75rem; 
        text-decoration: none; letter-spacing: 1px;
    }
    .btn-launch:hover { background: #F0E68C; box-shadow: 0 0 15px rgba(212,175,55,0.4); }

    /* Atelier Footer */
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 12px; font-size: 0.65rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 3px; text-transform: uppercase; }
    
    /* Tab Styling Overrides */
    button[data-baseweb="tab"] { font-family: 'Tenor Sans', sans-serif !important; font-size: 0.8rem !important; letter-spacing: 1.5px !important; color: #666 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & STRATEGIC MACRO METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div class="sub-title">Global Hub • Strategic Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [
    ("Global Beauty Sector", "$593.2B"),
    ("EU Market Growth", "+16.2%"),
    ("Poland Growth (Max)", "+75.3%"),
    ("Forecasting Accuracy", "91%")
]
for col, (label, value) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. ANALYTICAL TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "MARKET ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        episode = st.radio("Select Intelligence Series:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market", 
            "🔮 Ep. 2: 2026 Outlook & AI Chips",
            "🌍 Ep. 3: The European Barbell & Poland"
        ], label_visibility="collapsed")
        
        if "Ep. 1" in episode:
            current_transcript, current_audio = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
            f_type, v_title = "Notes_Gourmand", "The Gourmand 2.0 Phenomenon"
            desc = "Analyzing 'The Lipstick Effect' and Sol de Janeiro's global scent-stacking dominance."
        elif "Ep. 2" in episode:
            current_transcript, current_audio = "podcast_transcript_2026.md", "podcast_2026.mp3"
            f_type, v_title = "None", "2026 Global Projections"
            desc = "Deep dive into NVIDIA's AI dominance, US trade protectionism, and neuro-perfumery."
        else:
            current_transcript, current_audio = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3"
            f_type, v_title = "Barbell", "The Barbell Market Structure 2026"
            desc = "How the EU market is bifurcating, leaving only extreme budget and ultra-luxury tiers."

        st.audio(current_audio)
        st.markdown(f'<p style="color:#888; font-size:0.85rem; font-style:italic; margin-top:15px; border-left: 2px solid #333; padding-left: 15px;">{desc}</p>', unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Market Data: {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            b_counts = b_counts.sort_values('Tier')
            
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count',
                         color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'},
                         template="plotly_dark")
            fig.update_traces(textposition='outside', textfont_size=14, marker_line_color='#D4AF37', marker_line_width=2)
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand":
                df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment",
                         text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'], template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=1.5)

        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=420, margin=dict(t=50))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 OPEN STRATEGIC TRANSCRIPT"):
            try:
                with open(current_transcript, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Strategic transcript file is missing from the directory.")
    with d2:
        with st.expander("📈 OPEN MARKET REPORT"):
            rep = 'trend_report_2025.md' if "Ep. 1" in episode else 'macro_report_2026.md'
            try:
                with open(rep, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info("This strategic report is currently being finalized in the Intelligence Atelier.")

# --- TAB 2: MARKET ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Strategic Matrix</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment",
                       hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'],
                       template="plotly_dark", size_max=45)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=650, font_family="Lato")
    st.plotly_chart(fig_b, use_container_width=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Market Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Select Intelligence Profile:", ["-- Choose a Profile --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Choose a Profile --":
        f_data = df[df['name'] == f_choice].iloc[0]
        st.markdown(f"""
            <div style="border: 1px solid #D4AF37; background: #050505; padding: 50px; text-align: center; border-radius: 2px; box-shadow: 0 0 30px rgba(212,175,55,0.15);">
                <h2 style="color: #D4AF37; font-family: 'Tenor Sans'; margin-bottom:5px; font-size: 2.3rem; letter-spacing: 3px;">{f_data['name']}</h2>
                <p style="color: #888; text-transform: uppercase; letter-spacing: 5px; font-size:0.8rem;">{f_data['brand']} • {f_data['segment']}</p>
                <div style="display: flex; justify-content: center; gap: 70px; margin: 45px 0;">
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_score']}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.75rem; letter-spacing:2px; margin-bottom:12px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans'; font-size:2.2rem;">{f_data['community_votes']}</h3></div>
                </div>
                <div style="border-top:1px solid #222; padding-top:30px; max-width:650px; margin:0 auto;">
                    <p style="color:#D4AF37; font-size:0.85rem; font-weight:bold; letter-spacing:2px; margin-bottom:15px; text-transform:uppercase;">Olfactory Strategic Profile</p>
                    <p style="color:#ccc; font-size:1.15rem; line-height:1.7;">{f_data['top_notes']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tabs[3]:
    st.markdown('<div class="section-header">Strategic Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    t_list = [
        ("🧪 Functional Scent", "Mood-regulating neuro-perfs designed by AI. Scent moves from aesthetics to biotech wellness."),
        ("🧛‍♀️ Vamp Romantic", "The definitive shift toward dark cherry, leather, and gothic luxury in Gen Z prestige segments."),
        ("📈 Macro Resilience", "Poland's rise as a top-tier European economy. Supply chain adaptation to Trillion-dollar CEE markets.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], t_list):
        col.markdown(f'<div style="border:1px solid #333; background:rgba(10,10,10,0.9); padding:35px; border-left: 4px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans; letter-spacing:1px; margin-bottom:15px;">{t_title}</h4><p style="color:#bbb; font-size:0.95rem; line-height:1.7;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tabs[4]:
    st.markdown('<div class="section-header">Interconnected Analytical Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and real-time regional dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"),
        ("🔍 Perfume Finder", "Consumer recommendation PoC based on high-fidelity preference matching.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization and community olfactory mapping.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend architecture for high-fidelity massive dataset management.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]:
            st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:12px; letter-spacing:1.5px;">{e_n}</h4><p style="color:#888; font-size:0.9rem; line-height:1.6;">{e_d}</p></div><div style="margin-top:30px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch Professional Application</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 120px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • STRATEGIC DESIGN BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)