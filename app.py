import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI & LUXURY CSS (ATELIER SUPREME)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    /* Global Background */
    .stApp { 
        background-color: #000000; 
        background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%); 
        font-family: 'Lato', sans-serif !important; 
    }

    /* Header Styling */
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; width: 100%; max-width: 600px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }
    
    /* Metrics */
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.15); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem; margin: 0; }
    
    /* Section Headers */
    .section-header { 
        color: #D4AF37; 
        font-family: 'Tenor Sans', sans-serif; 
        font-size: 1.3rem; 
        border-left: 3px solid #D4AF37; 
        padding-left: 15px; 
        margin: 25px 0 15px 0; 
        text-transform: uppercase; 
        letter-spacing: 1px; 
    }

    /* TRANSCRIPT BOX - ZŁOTE NAGŁÓWKI I STYLIZACJA */
    .transcript-box { 
        font-family: 'Lato', sans-serif; 
        font-size: 0.95rem; 
        line-height: 1.8; 
        color: #bbbbbb; 
        background: #080808; 
        padding: 35px; 
        border: 1px solid #222; 
        border-radius: 4px;
        text-align: justify;
    }
    .transcript-box h1 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.6rem; border-bottom: 1px solid #D4AF37; padding-bottom: 10px; margin-bottom: 20px; text-align: center; text-transform: uppercase; }
    .transcript-box h2 { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; margin-top: 25px; border-left: 2px solid #D4AF37; padding-left: 10px; }
    .transcript-box h3 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.1rem; margin-top: 20px; }
    .transcript-box strong { color: #D4AF37; font-weight: 700; }
    
    /* Ecosystem Cards */
    .project-card { border:1px solid #222; background:#0a0a0a; padding:20px; transition:0.3s; height:100%; border-radius: 2px; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { 
        display:block; width:100%; padding:10px; background:#D4AF37; color:#000 !important; 
        text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; 
        text-decoration:none; transition: 0.3s;
    }
    .btn-launch:hover { background: #F0E68C; }

    /* Footer */
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; z-index: 999; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & TOP METRICS
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="header-wrapper">
        <div class="header-outer">
            <div class="header-inner">
                <h1 class="main-title">Fragrance Intelligence</h1>
                <div class="sub-title">Global Trends • Strategic Forecast 2026</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
metrics = [
    ("Global Beauty Market", "$593.2B"),
    ("EU Market Growth", "+16.2%"),
    ("Poland (EU Max)", "+75.3%"),
    ("Model Reliability", "91%")
]
for col, (lab, val) in zip([m1, m2, m3, m4], metrics):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{lab}</div><div class="metric-value">{val}</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. DASHBOARD TABS
# -----------------------------------------------------------------------------
tabs = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tabs[0]:
    col_audio, col_viz = st.columns([1, 1.4], gap="large")
    
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence</div>', unsafe_allow_html=True)
        episode = st.radio("Intelligence Briefing Series:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market", 
            "🔮 Ep. 2: 2026 Outlook & AI Chips",
            "🌍 Ep. 3: The European Barbell & Poland"
        ])
        
        if "Ep. 1" in episode:
            current_transcript, current_audio = "podcast_transcript.md", "https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3"
            f_type, v_title = "Notes_Gourmand", "The Gourmand 2.0 Phenomenon"
        elif "Ep. 2" in episode:
            current_transcript, current_audio = "podcast_transcript_2026.md", "podcast_2026.mp3"
            f_type, v_title = "None", "2026 Global Projections"
        else:
            current_transcript, current_audio = "ep3_whisper_transcript_EN.md", "ep3_europe_barbell.mp3"
            f_type, v_title = "Barbell", "The Barbell Market Structure"

        st.audio(current_audio)
        st.info("💡 Strategic tip: Expand the sections below the charts to read the full intelligence reports.")

    with col_viz:
        st.markdown(f'<div class="section-header">Live Analytics: {v_title}</div>', unsafe_allow_html=True)
        
        if f_type == "Barbell":
            b_counts = df['market_structure'].value_counts().reset_index()
            b_counts.columns = ['Tier', 'Count']
            b_order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            b_counts['Tier'] = pd.Categorical(b_counts['Tier'], categories=b_order, ordered=True)
            b_counts = b_counts.sort_values('Tier')
            
            fig = px.bar(b_counts, x='Tier', y='Count', color='Tier', text='Count',
                         color_discrete_map={'Ultra-Niche (Barbell Top)': '#D4AF37', 'Budget (Barbell Bottom)': '#F0E68C', 'Squeezed Middle': '#333333'},
                         template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=1.5)
        else:
            df_v = df.copy()
            if f_type == "Notes_Gourmand":
                df_v = df_v[df_v['top_notes'].str.contains('Vanilla|Pistachio', case=False, na=False)]
            df_t = df_v.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_t, x="community_votes", y="name", orientation='h', color="segment",
                         text="community_votes", color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'], template="plotly_dark")
            fig.update_traces(textposition='outside', marker_line_color='#D4AF37', marker_line_width=1)

        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="Lato", showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 OPEN EXECUTIVE TRANSCRIPT"):
            try:
                with open(current_transcript, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript file missing.")
    with d2:
        with st.expander("📈 OPEN STRATEGIC REPORT"):
            rep = 'trend_report_2025.md' if "Ep. 1" in episode else 'macro_report_2026.md'
            try:
                with open(rep, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info("This strategic report is currently in the Atelier for final polishing.")

# --- TAB 2: DEEP DIVE ANALYTICS ---
with tabs[1]:
    st.markdown('<div class="section-header">Quality vs. Popularity Quadrant</div>', unsafe_allow_html=True)
    fig_b = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment",
                       hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'],
                       template="plotly_dark", size_max=40)
    fig_b.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600, font_family="Lato")
    st.plotly_chart(fig_b, use_container_width=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tabs[2]:
    st.markdown('<div class="section-header">Fragrance Case Studies</div>', unsafe_allow_html=True)
    f_choice = st.selectbox("Curated Selection:", ["-- Select Case Study --"] + sorted(df['name'].tolist()))
    if f_choice != "-- Select Case Study --":
        f_data = df[df['name'] == f_choice].iloc[0]
        st.markdown(f"""
            <div style="border: 1px solid #D4AF37; background: #050505; padding: 40px; text-align: center;">
                <h2 style="color: #D4AF37; font-family: 'Tenor Sans'; margin-bottom:0;">{f_data['name']}</h2>
                <p style="color: #888; text-transform: uppercase; letter-spacing: 3px; font-size:0.7rem;">{f_data['brand']} | {f_data['segment']}</p>
                <div style="display: flex; justify-content: center; gap: 50px; margin: 30px 0;">
                    <div><p style="color:#666; font-size:0.6rem; letter-spacing:1px;">QUALITY SCORE</p><h3 style="color:#F0E68C; font-family:'Tenor Sans';">{f_data['community_score']}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.6rem; letter-spacing:1px;">GLOBAL VOTES</p><h3 style="color:#F0E68C; font-family:'Tenor Sans';">{f_data['community_votes']}</h3></div>
                </div>
                <div style="border-top:1px solid #222; padding-top:20px; max-width:500px; margin:0 auto;">
                    <p style="color:#D4AF37; font-size:0.7rem; font-weight:bold; letter-spacing:1px;">SCENT PROFILE</p>
                    <p style="color:#ccc;">{f_data['top_notes']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tabs[3]:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    t_list = [
        ("🧪 Functional Scent", "Mood-enhancing molecules designed by AI to regulate neuro-responses."),
        ("🧛‍♀️ Vamp Romantic", "The shift to dark cherry, leather, and gothic opulence in Gen Z markets."),
        ("📈 Macro Resilience", "Poland's rise as the 20th largest global economy (PPP) by 2026.")
    ]
    for col, (t_title, t_text) in zip([c1, c2, c3], t_list):
        col.markdown(f'<div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #D4AF37; height:100%;"><h4 style="color:#D4AF37; font-family:Tenor Sans;">{t_title}</h4><p style="color:#ccc; font-size:0.85rem;">{t_text}</p></div>', unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tabs[4]:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    ecosystem = [
        ("🌍 Aromo Intelligence", "Russian market scraping engine and dashboard.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"),
        ("🔍 Perfume Finder", "Algorithmic recommendation system PoC.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning trend visualization.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS", "Backend engineering hub for massive datasets.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    e_cols = st.columns(2)
    for i, (e_n, e_d, e_l) in enumerate(ecosystem):
        with e_cols[i % 2]:
            st.markdown(f'<div class="project-card"><div><h4 style="color:#D4AF37; font-family:Tenor Sans; margin-bottom:5px;">{e_n}</h4><p style="color:#888; font-size:0.8rem;">{e_d}</p></div><div style="margin-top:20px;"><a href="{e_l}" target="_blank" class="btn-launch">🚀 Launch App</a></div></div>', unsafe_allow_html=True)

st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • ATELIER DATA STRATEGY BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)