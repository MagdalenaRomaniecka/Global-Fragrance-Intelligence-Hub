import streamlit as st
import plotly.express as px
import pandas as pd
import os
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI & LUXURY CSS (PREMIUM ATELIER DESIGN)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fragrance Intelligence | Atelier", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');

    .stApp { background-color: #000000; background-image: radial-gradient(circle at 50% 0%, #111 0%, #000 100%); font-family: 'Lato', sans-serif !important; }
    .header-wrapper { display: flex; justify-content: center; padding: 30px 0 15px 0; }
    .header-outer { border: 1px solid #333; padding: 6px; display: inline-block; width: 100%; max-width: 600px; box-sizing: border-box; }
    .header-inner { border: 1px solid #D4AF37; padding: 25px 60px; text-align: center; background-color: #050505; }
    .main-title { font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 4px; margin: 0; }
    .sub-title { font-family: 'Lato', sans-serif; color: #888; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 300; }
    
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; border-radius: 2px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2rem; margin: 0; }
    
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }
    .transcript-box { font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.6; color: #cccccc; background: #080808; padding: 30px; border: 1px solid #222; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; z-index: 999; text-transform: uppercase; }
    
    .project-card { border:1px solid #222; background:#0a0a0a; padding:20px; transition:0.3s; display:flex; flex-direction:column; justify-content:space-between; height:100%; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:10px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; margin-bottom:10px; text-decoration:none; }
    .btn-code { display:block; width:100%; padding:10px; border:1px solid #444; color:#888 !important; text-align:center; text-transform:uppercase; font-size:0.7rem; text-decoration:none; }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & STRATEGIC METRICS
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

# Główne KPI (Wskaźniki)
m1, m2, m3, m4 = st.columns(4)
m1.markdown('<div class="metric-box"><div class="metric-label">Global Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
m2.markdown('<div class="metric-box"><div class="metric-label">PL Growth (EU Max)</div><div class="metric-value">+75.3%</div></div>', unsafe_allow_html=True)
m3.markdown('<div class="metric-box"><div class="metric-label">Scent-Stacking surge</div><div class="metric-value">+125%</div></div>', unsafe_allow_html=True)
m4.markdown('<div class="metric-box"><div class="metric-label">Model Reliability</div><div class="metric-value">91%</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. DASHBOARD TABS
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

# --- TAB 1: STRATEGIC BRIEFING ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence Hub</div>', unsafe_allow_html=True)
        
        selected_episode = st.radio("Select Intelligence Briefing:", [
            "🎧 Ep. 1: Recession Glam & 2025 Dynamics", 
            "🔮 Ep. 2: 2026 Outlook & Functional Scent",
            "🌍 Ep. 3: European Barbell & Poland's Strategy"
        ])
        
        if "Ep. 1" in selected_episode:
            current_transcript = "podcast_transcript.md"
            st.audio("https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3")
            current_filter, viz_title = "Notes_Gourmand", "Gourmand 2.0 Movement"
            desc = "Analysis of 'The Lipstick Effect' and Sol de Janeiro's market dominance."
        
        elif "Ep. 2" in selected_episode:
            current_transcript = "podcast_transcript_2026.md"
            st.audio("podcast_2026.mp3")
            current_filter, viz_title = "None", "2026 Global Projections"
            desc = "Deep dive into AI chips, trade protectionism, and neuro-perfumery."
            
        else: # Ep. 3
            current_transcript = "ep3_whisper_transcript_EN.md"
            st.audio("ep3_europe_barbell.mp3")
            current_filter, viz_title = "Barbell", "The Barbell Market Phenomenon"
            desc = "How the EU market is hollowing out, leaving only budget and ultra-luxury tiers."

        st.markdown(f"""
            <div style="margin-top:20px; border-left:3px solid #D4AF37; padding:15px; background:rgba(212,175,55,0.05);">
                <p style="color:#D4AF37; font-size:0.6rem; text-transform:uppercase; margin-bottom:5px; font-weight:bold;">Current Narrative</p>
                <p style="color:#ccc; font-size:0.9rem; line-height:1.5;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)

    with col_viz:
        st.markdown(f'<div class="section-header">Live Intelligence: {viz_title}</div>', unsafe_allow_html=True)
        
        # WYKRES BARBELL DLA EPIZODU 3
        if current_filter == "Barbell" and 'market_structure' in df.columns:
            barbell_counts = df['market_structure'].value_counts().reset_index()
            barbell_counts.columns = ['Market Tier', 'Product Count']
            
            # Poprawna kolejność słupków
            order = ['Budget (Barbell Bottom)', 'Squeezed Middle', 'Ultra-Niche (Barbell Top)']
            barbell_counts['Market Tier'] = pd.Categorical(barbell_counts['Market Tier'], categories=order, ordered=True)
            barbell_counts = barbell_counts.sort_values('Market Tier')

            fig = px.bar(
                barbell_counts, x='Market Tier', y='Product Count', color='Market Tier',
                text='Product Count', title="Economic Structure: The Barbell Effect 2026",
                color_discrete_map={
                    'Ultra-Niche (Barbell Top)': '#D4AF37', 
                    'Budget (Barbell Bottom)': '#F0E68C', 
                    'Squeezed Middle': '#333333'
                }, template="plotly_dark"
            )
            fig.update_traces(textposition='outside', textfont_size=14, marker_line_color='#D4AF37', marker_line_width=1.5)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
            
        # WYKRESY DLA POZOSTAŁYCH EPIZODÓW
        else:
            df_viz = df.copy()
            if current_filter == "Notes_Gourmand":
                df_viz = df_viz[df_viz['top_notes'].str.contains('Vanilla|Caramel|Pistachio', case=False, na=False)]
            
            df_top = df_viz.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            fig = px.bar(df_top, x="community_votes", y="name", orientation='h', color="segment",
                         color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'], template="plotly_dark")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    # Sekcja Dokumentacji (Transkrypcja i Raporty)
    st.write("---")
    d1, d2 = st.columns(2)
    with d1:
        with st.expander("📄 VIEW EXECUTIVE TRANSCRIPT"):
            try:
                with open(current_transcript, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.error("Transcript file not found.")
    with d2:
        with st.expander("📈 VIEW STRATEGIC REPORT"):
            report = 'trend_report_2025.md' if "Ep. 1" in selected_episode else 'macro_report_2026.md'
            try:
                with open(report, 'r', encoding='utf-8') as f:
                    st.markdown(f'<div class="transcript-box">{f.read()}</div>', unsafe_allow_html=True)
            except: st.info("Strategic report for this episode is being finalized.")

# --- TAB 2: DEEP DIVE ANALYTICS ---
with tab2:
    st.markdown('<div class="section-header">Global Market Positioning Map</div>', unsafe_allow_html=True)
    fig_bubble = px.scatter(df, x="community_votes", y="community_score", size="price_usd", color="segment",
                            hover_name="name", color_discrete_sequence=['#D4AF37', '#F0E68C', '#444'],
                            template="plotly_dark", size_max=40, title="Quality vs. Popularity Matrix")
    fig_bubble.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=600)
    st.plotly_chart(fig_bubble, use_container_width=True)

# --- TAB 3: FRAGRANCE VAULT ---
with tab3:
    st.markdown('<div class="section-header">Market Case Studies</div>', unsafe_allow_html=True)
    sel_frag = st.selectbox("Select Fragrance to Analyze:", ["-- Select --"] + sorted(df['name'].tolist()))
    if sel_frag != "-- Select --":
        frag = df[df['name'] == sel_frag].iloc[0]
        st.markdown(f"""
            <div style="border: 1px solid #D4AF37; background: #050505; padding: 40px; text-align: center; border-radius: 2px;">
                <h2 style="color: #D4AF37; font-family: 'Tenor Sans';">{frag['name']}</h2>
                <p style="color: #888; text-transform: uppercase; letter-spacing: 2px;">{frag['brand']} | {frag['segment']}</p>
                <div style="display: flex; justify-content: center; gap: 50px; margin: 30px 0;">
                    <div><p style="color:#666; font-size:0.7rem;">SCORE</p><h3 style="color:#F0E68C;">{frag['community_score']}/5.0</h3></div>
                    <div><p style="color:#666; font-size:0.7rem;">VOTES</p><h3 style="color:#F0E68C;">{frag['community_votes']}</h3></div>
                </div>
                <p style="color: #ccc; font-style: italic; border-top: 1px solid #222; padding-top: 20px;">Notes: {frag['top_notes']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 2026 OUTLOOK ---
with tab4:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    trends = [
        ("🧪 Functional Fragrance", "Scent moves into neuroscience. 71% of consumers expect mood-enhancing benefits via AI-assisted neuro-perfumery."),
        ("🧛‍♀️ Vamp Romantic", "The rebellion against minimalism. Dark cherry, leather, and incense driving Gen Z gothic opulence."),
        ("📈 Macro Forces", "US Protectionism vs. Poland's Rise. Supply chains adapting to a new trillion-dollar economy in CEE.")
    ]
    for col, (title, text) in zip([c1, c2, c3], trends):
        col.markdown(f"""<div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #D4AF37; height:100%;">
            <h4 style="color:#D4AF37;">{title}</h4><p style="color:#ccc; font-size:0.85rem;">{text}</p></div>""", unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tab5:
    st.markdown('<div class="section-header">Analytical Ecosystem</div>', unsafe_allow_html=True)
    projects = [
        ("🌍 Aromo Intelligence", "Market scraping engine focusing on the Russian market structure.", "https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence"),
        ("🔍 Perfume Finder", "Consumer recommendation system based on preference matrix matching.", "https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/"),
        ("📊 ScentSational Analytics", "Deep learning analysis and visualization of Fragrantica data.", "https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/"),
        ("🧪 ScentSational LFS Hub", "Backend engineering hub for massive fragrance datasets.", "https://baphomert-scentsational-fragrantica-lfs2.hf.space/")
    ]
    cols = st.columns(2)
    for i, (name, desc, link) in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""<div class="project-card">
                <div><h4 style="color:#D4AF37; margin-bottom:5px;">{name}</h4><p style="color:#888; font-size:0.8rem;">{desc}</p></div>
                <div style="margin-top:20px;"><a href="{link}" target="_blank" class="btn-launch">🚀 Launch App</a></div>
            </div>""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • DEVELOPED BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)