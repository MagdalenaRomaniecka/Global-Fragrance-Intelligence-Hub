import streamlit as st
import plotly.express as px
import pandas as pd
import os
import re
from data_loader import load_and_merge_data

# -----------------------------------------------------------------------------
# 1. UI & LUXURY CSS (WITH MOBILE RESPONSIVENESS)
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
    .metric-box { border: 1px solid #222; background-color: #080808; padding: 15px; text-align: center; transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; }
    .metric-box:hover { border-color: #D4AF37; box-shadow: 0 0 10px rgba(212, 175, 55, 0.1); }
    .metric-label { color: #666; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-family: 'Lato', sans-serif; }
    .metric-value { color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 2.2rem; margin: 0; }
    div[data-baseweb="tab-list"] { justify-content: center !important; gap: 20px; margin-top: 10px; margin-bottom: 30px; border-bottom: 1px solid #222 !important; padding-bottom: 10px; flex-wrap: wrap; }
    button[data-baseweb="tab"] { background-color: transparent !important; border: none !important; color: #666 !important; font-family: 'Lato', sans-serif !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; font-size: 0.75rem !important; padding: 10px !important; }
    button[data-baseweb="tab"]:hover { color: #D4AF37 !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #D4AF37 !important; border-bottom: 2px solid #D4AF37 !important; font-weight: 700 !important; }
    .section-header { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; border-left: 3px solid #D4AF37; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }
    .transcript-box { font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.6; color: #cccccc; background: #080808; padding: 30px; border: 1px solid #222; overflow-x: hidden; }
    .transcript-box h1, .transcript-box h2, .transcript-box h3 { color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-weight: normal; margin-top: 25px; margin-bottom: 15px; }
    .transcript-box h1 { font-size: 1.5rem; text-align: center; border-bottom: 1px solid #D4AF37; padding-bottom: 15px; margin-bottom: 25px; }
    .transcript-box h2 { font-size: 1.25rem; color: #F0E68C; border-bottom: 1px solid #333; padding-bottom: 10px; }
    .transcript-box p { margin-bottom: 15px; text-align: justify; }
    .transcript-box strong { color: #F0E68C; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; font-weight: 700; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #000; color: #444; text-align: center; padding: 10px; font-size: 0.6rem; border-top: 1px solid #111; letter-spacing: 1px; z-index: 999; text-transform: uppercase; font-family: 'Lato', sans-serif; }
    a { color: #D4AF37 !important; text-decoration: none !important; transition: 0.3s; }
    a:hover { color: #FFF !important; }
    .project-card { border:1px solid #222; background:#0a0a0a; padding:20px; transition:0.3s; display:flex; flex-direction:column; justify-content:space-between; height:100%; }
    .project-card:hover { border-color:#D4AF37; }
    .btn-launch { display:block; width:100%; padding:10px; background:#D4AF37; color:#000 !important; text-align:center; font-weight:bold; text-transform:uppercase; font-size:0.7rem; margin-bottom:10px; border-radius:2px; font-family:'Lato', sans-serif; }
    .btn-code { display:block; width:100%; padding:10px; border:1px solid #444; color:#888 !important; text-align:center; text-transform:uppercase; font-size:0.7rem; border-radius:2px; font-family:'Lato', sans-serif; }
    .btn-code:hover { border-color:#D4AF37; color:#D4AF37 !important; }

    /* --- MOBILE RESPONSIVENESS --- */
    @media (max-width: 768px) {
        .header-outer { padding: 4px; }
        .header-inner { padding: 15px 10px; }
        .main-title { font-size: 1.4rem; letter-spacing: 2px; }
        .sub-title { font-size: 0.6rem; letter-spacing: 1px; }
        .metric-value { font-size: 1.6rem; }
        .transcript-box { padding: 15px; font-size: 0.85rem; }
        .transcript-box h1 { font-size: 1.2rem; }
        div[data-baseweb="tab-list"] { gap: 5px; }
        button[data-baseweb="tab"] { font-size: 0.65rem !important; padding: 8px 5px !important; letter-spacing: 0.5px !important; }
        .section-header { font-size: 1.1rem; }
    }
    </style>
""", unsafe_allow_html=True)

df = load_and_merge_data()

# -----------------------------------------------------------------------------
# 2. HEADER & METRICS
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

c1, c2, c3 = st.columns(3)
c1.markdown('<div class="metric-box"><div class="metric-label">Global Beauty Market</div><div class="metric-value">$593.2B</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="metric-box"><div class="metric-label">Fragrance Growth</div><div class="metric-value">+16.2%</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="metric-box"><div class="metric-label">RU Local Production</div><div class="metric-value">68% Share</div></div>', unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)
c4.markdown('<div class="metric-box"><div class="metric-label">PL Global Econ Rank (PPP)</div><div class="metric-value">20th</div></div>', unsafe_allow_html=True)
c5.markdown('<div class="metric-box"><div class="metric-label">Scent-Stacking Boom</div><div class="metric-value">+125%</div></div>', unsafe_allow_html=True)
c6.markdown('<div class="metric-box"><div class="metric-label">Sol de Janeiro Share</div><div class="metric-value">31.6%</div></div>', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. LOGICAL TAB ORDER (Storytelling Flow)
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(["STRATEGIC BRIEFING", "DEEP DIVE ANALYTICS", "FRAGRANCE VAULT", "2026 OUTLOOK", "ECOSYSTEM"])

current_transcript_file = "podcast_transcript.md"

# --- TAB 1: STRATEGIC BRIEFING ---
with tab1:
    col_audio, col_viz = st.columns([1, 1.5], gap="large")
    
    with col_audio:
        st.markdown('<div class="section-header">Audio Intelligence</div>', unsafe_allow_html=True)
        
        selected_episode = st.radio("Select Episode:", [
            "🎧 Ep. 1: Recession Glam & 2025 Market Dynamics", 
            "🔮 Ep. 2: 2026 Outlook (AI, Tariffs & Functional Fragrance)"
        ])
        
        if "Ep. 1" in selected_episode:
            current_transcript_file = "podcast_transcript.md"
            PODCAST_SCRIPT = {
                "I. INTRODUCTION: RECESSION GLAM": {"start_time": 0, "filter": "None", "desc": "Global market resilience ($593.2B). Analysis of 'The Lipstick Effect'."},
                "II. SCENT TREND: GOURMAND 2.0": {"start_time": 571, "filter": "Notes_Gourmand", "desc": "Case study: Sol de Janeiro and Scent-stacking strategy."},
                "III. MARKET FOCUS: RUSSIA & DUHI": {"start_time": 1433, "filter": "Market_Russia", "desc": "How import tariffs (35%) drove local production to 68% market share."}
            }
            selected_chapter = st.radio("Select Chapter:", list(PODCAST_SCRIPT.keys()))
            chapter_data = PODCAST_SCRIPT[selected_chapter]
            
            st.audio("https://raw.githubusercontent.com/MagdalenaRomaniecka/Global-Fragrance-Intelligence-Hub/main/podcast_trends.mp3", start_time=chapter_data["start_time"])
            
            st.markdown(f"""
                <div style="margin-top:20px; border-left:3px solid #D4AF37; padding:15px; background:rgba(212,175,55,0.05);">
                    <p style="color:#D4AF37; font-size:0.6rem; text-transform:uppercase; margin-bottom:5px; font-weight:bold;">Key Narrative</p>
                    <p style="color:#ccc; font-size:0.95rem; line-height:1.6; font-family:'Lato', sans-serif;">{chapter_data['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            current_filter = chapter_data["filter"]
            viz_title = selected_chapter.split(':')[1]

        else:
            current_transcript_file = "podcast_transcript_2026.md"
            st.audio("podcast_2026.mp3")
            st.markdown("""
                <div style="margin-top:20px; border-left:3px solid #D4AF37; padding:15px; background:rgba(212,175,55,0.05);">
                    <p style="color:#D4AF37; font-size:0.6rem; text-transform:uppercase; margin-bottom:5px; font-weight:bold;">Key Narrative</p>
                    <p style="color:#ccc; font-size:0.95rem; line-height:1.6; font-family:'Lato', sans-serif;">
                    Exclusive 2026-2035 briefing. Deep dive into Nvidia's AI dominance, US trade protectionism, Poland's economic rise, and the evolution of 'Functional Fragrance' and 'Vamp Romantic' aesthetics.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            current_filter = "None"
            viz_title = "Global Market Overview"

    with col_viz:
        st.markdown(f'<div class="section-header">Live Data: {viz_title}</div>', unsafe_allow_html=True)
        if not df.empty:
            df_story = df.copy()
            if current_filter == "Notes_Gourmand" and 'top_notes' in df_story.columns:
                df_story = df_story[df_story['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar|Praline', case=False, na=False)]
            elif current_filter == "Market_Russia" and 'country' in df_story.columns:
                df_story = df_story[df_story['country'] == 'Russia']
            
            df_top = df_story.nlargest(10, 'community_votes').sort_values('community_votes', ascending=True)
            
            fig = px.bar(
                df_top, x="community_votes", y="name", orientation='h',
                color="segment", hover_name="name", template="plotly_dark",
                color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'],
                title="Top 10 Most Voted Fragrances in this Segment",
                text="community_votes"
            )
            fig.update_traces(textposition='outside', textfont_size=12, textfont_color='#E0E0E0', cliponaxis=False)
            fig.update_xaxes(range=[0, df_top['community_votes'].max() * 1.25]) 
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                font_family="Lato", height=380, margin=dict(l=0,r=50,t=40,b=0),
                yaxis_title=None, xaxis_title="Community Votes", showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

    # --- DOCUMENTS ---
    st.write("---")
    col_doc1, col_doc2 = st.columns(2)
    
    if "Ep. 1" in selected_episode:
        with col_doc1:
            with st.expander("📄 READ EXECUTIVE SUMMARY (EPISODE 1)"):
                try:
                    with open(current_transcript_file, 'r', encoding='utf-8') as f:
                        raw_text = f.read()
                        st.markdown(f'<div class="transcript-box">\n\n{raw_text}\n\n</div>', unsafe_allow_html=True)
                except:
                    st.markdown('<div class="transcript-box">Summary unavailable. Missing file.</div>', unsafe_allow_html=True)
        with col_doc2:
            with st.expander("📈 READ 2025 TREND REPORT"):
                try:
                    with open('trend_report_2025.md', 'r', encoding='utf-8') as f:
                        raw_report = f.read()
                        st.markdown(f'<div class="transcript-box">\n\n{raw_report}\n\n</div>', unsafe_allow_html=True)
                except:
                    st.markdown('<div class="transcript-box">Trend report unavailable. Please ensure file is in the directory.</div>', unsafe_allow_html=True)
    else:
        with col_doc1:
            with st.expander("📄 READ EXECUTIVE SUMMARY (EPISODE 2)"):
                try:
                    with open(current_transcript_file, 'r', encoding='utf-8') as f:
                        raw_text = f.read()
                        st.markdown(f'<div class="transcript-box">\n\n{raw_text}\n\n</div>', unsafe_allow_html=True)
                except:
                    st.markdown('<div class="transcript-box">Summary unavailable. Missing file.</div>', unsafe_allow_html=True)
        with col_doc2:
            with st.expander("📈 READ 2026 MACRO REPORT"):
                try:
                    with open('macro_report_2026.md', 'r', encoding='utf-8') as f:
                        raw_macro = f.read()
                        st.markdown(f'<div class="transcript-box">\n\n{raw_macro}\n\n</div>', unsafe_allow_html=True)
                except:
                    st.markdown('<div class="transcript-box">Macro report unavailable. Please ensure file is in the directory.</div>', unsafe_allow_html=True)


# --- TAB 2: DEEP DIVE ANALYTICS (BUBBLE CHART) ---
with tab2:
    st.markdown('<div class="section-header">Market Positioning Map</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="color: #aaa; font-family: 'Lato', sans-serif; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.6; border-left: 2px solid #333; padding-left: 15px;">
            This scatter plot acts as a strategic quadrant matrix. It plots the <strong>Community Score (Quality)</strong> against 
            <strong>Total Votes (Popularity)</strong>. Bubble size indicates estimated retail price (USD). 
            Use the filters below to isolate specific market trends.
        </div>
    """, unsafe_allow_html=True)

    if not df.empty:
        filter_option = st.selectbox("Filter Strategic View:", [
            "Show All Global Data", "Focus: Gourmand 2.0 Notes", "Focus: Russian Market",
            "Focus: Functional Fragrance (2026 Trend)", "Focus: Vamp Romantic Notes (2026 Trend)"
        ])
        
        df_plot = df.copy()
        if filter_option == "Focus: Gourmand 2.0 Notes" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Vanilla|Caramel|Pistachio|Sugar|Praline', case=False, na=False)]
        elif filter_option == "Focus: Russian Market" and 'country' in df_plot.columns:
            df_plot = df_plot[df_plot['country'] == 'Russia']
        elif filter_option == "Focus: Functional Fragrance (2026 Trend)" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Functional|Neuro|Clean|Mineral|Musk|Green|Fresh|Lavender', case=False, na=False)]
        elif filter_option == "Focus: Vamp Romantic Notes (2026 Trend)" and 'top_notes' in df_plot.columns:
            df_plot = df_plot[df_plot['top_notes'].str.contains('Cherry|Plum|Leather|Smoke|Incense|Dark|Vamp', case=False, na=False)]

        fig2 = px.scatter(
            df_plot, 
            x="community_votes", 
            y="community_score", 
            size="price_usd", 
            color="segment", 
            hover_name="name",
            text="name",
            color_discrete_sequence=['#D4AF37', '#F0E68C', '#666'],
            template="plotly_dark",
            size_max=40
        )
        
        fig2.update_traces(
            textposition='top center', 
            textfont_size=10, 
            textfont_color='#E0E0E0',
            marker=dict(line=dict(width=1, color='#111'), opacity=0.85)
        )
        
        if not df_plot.empty and len(df_plot) > 1:
            median_votes = df_plot['community_votes'].median()
            median_score = df_plot['community_score'].median()
            fig2.add_vline(x=median_votes, line_width=1, line_dash="dash", line_color="#555")
            fig2.add_hline(y=median_score, line_width=1, line_dash="dash", line_color="#555")

        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)', 
            font_family="Lato", 
            height=550, 
            margin=dict(l=0,r=50,t=40,b=0),
            xaxis_title="Popularity (Community Votes)",
            yaxis_title="Quality (Community Score out of 5.0)",
            legend_title_text="Market Segment",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        fig2.update_xaxes(range=[0, df_plot['community_votes'].max() * 1.2])
        fig2.update_yaxes(range=[df_plot['community_score'].min() * 0.95, 5.2])

        st.plotly_chart(fig2, use_container_width=True)
        
        insight_html = """
        <div style="border: 1px solid #D4AF37; background: #080808; padding: 30px; margin-top: 30px; margin-bottom: 20px; border-radius: 2px;">
            <div style="color: #D4AF37; font-family: 'Tenor Sans', sans-serif; font-size: 1.3rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; border-bottom: 1px solid #222; padding-bottom: 15px; line-height: 1.4;">
                Strategic Insight: The Trickle-Down Effect
            </div>
            <div style="color: #ccc; font-family: 'Lato', sans-serif; font-size: 0.95rem; line-height: 1.7;">
                <p>Market data reveals a clear <strong>Trickle-Down Effect</strong> in olfactory trends, visibly tracked by the color-coded segments in the charts above. Radical innovations typically originate within the <strong>Niche / Concept</strong> segment (e.g., The Nue Co. or Room 1015), prioritizing artistry over cost.</p>
                <p>Within 1-2 years, these profiles are smoothed and commercialized by <strong>Prestige / Designer</strong> houses (e.g., Paco Rabanne Phantom or Tom Ford Lost Cherry), gaining global traction through high-budget campaigns.</p>
                <p>Finally, in the maturity phase (years 3-4), the trend is fully absorbed by the <strong>Mass-Market</strong>. This is when we observe an explosion in community votes and market volume, driven by drugstore and fast-fashion brands (such as Zara) capitalizing on established consumer demand.</p>
            </div>
        </div>
        """
        st.markdown(insight_html, unsafe_allow_html=True)
        
        with st.expander("🔎 INSPECT RAW DATA"):
            st.dataframe(df.head(50), height=400, use_container_width=True, hide_index=True)


# --- TAB 3: FRAGRANCE VAULT ---
with tab3:
    st.markdown('<div class="section-header">The Fragrance Vault</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="color: #aaa; font-family: 'Lato', sans-serif; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.6; border-left: 2px solid #333; padding-left: 15px;">
            This curated vault contains strategic <strong>market case studies</strong> rather than a generic catalogue. 
            Each fragrance here has been specifically selected to demonstrate key industry shifts discussed in our reports, 
            from AI-formulated <em>Neuro-Perfumery</em> to the commercialization of the <em>Trickle-Down Effect</em>.
        </div>
    """, unsafe_allow_html=True)
    
    if not df.empty:
        col_filt1, col_filt2 = st.columns(2)
        
        with col_filt1:
            segments = ["All Segments"] + sorted(df['segment'].dropna().unique().tolist())
            selected_segment = st.selectbox("Filter by Market Segment:", segments)
            
        df_vault = df.copy()
        if selected_segment != "All Segments":
            df_vault = df_vault[df_vault['segment'] == selected_segment]
            
        with col_filt2:
            fragrance_list = sorted(df_vault['name'].dropna().unique().tolist())
            selected_fragrance = st.selectbox("Select a Case Study:", ["-- Select a Fragrance --"] + fragrance_list)
        
        if selected_fragrance != "-- Select a Fragrance --":
            frag_data = df_vault[df_vault['name'] == selected_fragrance].iloc[0]
            
            f_name = frag_data.get('name', 'Unknown')
            f_segment = frag_data.get('segment', 'Global')
            f_score = frag_data.get('community_score', 'N/A')
            f_votes = frag_data.get('community_votes', 'N/A')
            f_notes = frag_data.get('top_notes', 'Not specified')
            
            if isinstance(f_score, (int, float)):
                f_score = f"{f_score:.2f}"
            
            card_html = f"""<div style="border: 1px solid #D4AF37; background: #050505; padding: 40px 20px; margin-top: 20px; text-align: center; border-radius: 2px;">
<div style="font-family: 'Tenor Sans', sans-serif; color: #D4AF37; font-size: 2.2rem; letter-spacing: 2px; margin-bottom: 5px; text-transform: uppercase;">{f_name}</div>
<div style="font-family: 'Lato', sans-serif; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 30px;">Market Segment: {f_segment}</div>
<div style="display: flex; justify-content: center; gap: 60px; margin-bottom: 30px; flex-wrap: wrap;">
<div><div style="color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; font-family: 'Lato', sans-serif;">Community Score</div><div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem;">{f_score} <span style="font-size: 1rem; color: #666;">/ 5.0</span></div></div>
<div><div style="color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; font-family: 'Lato', sans-serif;">Global Votes</div><div style="color: #F0E68C; font-family: 'Tenor Sans', sans-serif; font-size: 1.8rem;">{f_votes}</div></div>
</div>
<div style="border-top: 1px solid #222; padding-top: 25px; max-width: 600px; margin: 0 auto;">
<div style="color: #D4AF37; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; font-weight: bold; font-family: 'Lato', sans-serif;">Key Notes / Profile</div>
<div style="color: #ccc; font-family: 'Lato', sans-serif; font-size: 1rem; line-height: 1.8; padding: 0 20px;">{f_notes}</div>
</div>
</div>"""
            st.markdown(card_html, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="border: 1px solid #222; background: #080808; color: #888; padding: 20px; text-align: center; font-family: 'Lato', sans-serif; letter-spacing: 1px; font-size: 0.85rem; border-radius: 2px; margin-top: 20px;">
                Select a case study from the '{selected_segment}' segment to view its profile.
            </div>
            """, unsafe_allow_html=True)


# --- TAB 4: 2026 OUTLOOK ---
with tab4:
    st.markdown('<div class="section-header">Trend Radar 2026–2030</div>', unsafe_allow_html=True)
    radar_html = """
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:20px; margin-bottom: 30px;">
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #D4AF37;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">🧪 Functional Fragrance</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                Scent moves beyond aesthetics into neuroscience. Driven by post-pandemic wellness, 71% of consumers now expect fragrances to offer mood-enhancing benefits. AI-assisted formulas, like the 45 million brain scans utilized for <b>Paco Rabanne Phantom</b>, bridge the gap between perfumery and mental wellbeing.
            </div>
        </div>
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #8B0000;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">🧛‍♀️ Vamp Romantic</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                A rebellion against 'Clean Girl' minimalism. Gen Z is driving a resurgence of dark, bold profiles. Key notes include <b>black cherry, smoked plum, incense, and leather</b>. This aesthetic blends gothic opulence with modern sensuality.
            </div>
        </div>
        <div style="border:1px solid #333; background:#080808; padding:20px; border-left: 3px solid #F0E68C;">
            <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.2rem; margin-bottom:10px;">📈 Macro Forces: Protectionism</div>
            <div style="color:#ccc; font-size:0.9rem; font-family:'Lato', sans-serif; line-height: 1.6;">
                Supply chains are adapting to aggressive US trade policies (tariffs). Capital is heavily concentrated in AI (Nvidia dominating S&P 500). Meanwhile, <b>Poland has advanced to the 20th largest global economy (PPP)</b>, creating a robust new market for luxury beauty.
            </div>
        </div>
    </div>
    """
    st.markdown(radar_html, unsafe_allow_html=True)

# --- TAB 5: ECOSYSTEM ---
with tab5:
    st.markdown('<div class="section-header">Project Ecosystem</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="color: #aaa; font-family: 'Lato', sans-serif; font-size: 0.95rem; margin-bottom: 25px; line-height: 1.6; border-left: 2px solid #333; padding-left: 15px;">
            This Project Ecosystem represents a comprehensive suite of interconnected analytical tools. 
            Each application is engineered to extract, process, and visualize fragrance data from distinct global sources 
            (such as Fragrantica or Aromo.ru), providing a 360-degree view of the market.
        </div>
    """, unsafe_allow_html=True)
    
    ecosystem_html = """
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:20px;">
        <div class="project-card">
            <div>
                <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:5px;">🌍 Aromo Intelligence</div>
                <div style="color:#F0E68C; font-size:0.6rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; font-weight:bold;">Data Source: Aromo.ru Scraper</div>
                <div style="color:#888; font-size:0.8rem; margin-bottom:20px; line-height:1.4;">Global market scraping engine & dashboard focusing on the Russian market structure.</div>
            </div>
            <div style="margin-top:auto;"><a href="https://huggingface.co/spaces/Baphomert/Aromo-Market-Intelligence" target="_blank" class="btn-launch">🚀 Launch App</a><a href="https://github.com/MagdalenaRomaniecka/Aromo-Market-Intelligence" target="_blank" class="btn-code">💻 View Code</a></div>
        </div>
        <div class="project-card">
            <div>
                <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:5px;">🔍 Perfume Finder</div>
                <div style="color:#F0E68C; font-size:0.6rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; font-weight:bold;">Data Source: Preference Matrix</div>
                <div style="color:#888; font-size:0.8rem; margin-bottom:20px; line-height:1.4;">Consumer recommendation system based on complex algorithmic matching.</div>
            </div>
            <div style="margin-top:auto;"><a href="https://perfume-finder-app-btskyvq7eytc5ujrgzr2dk.streamlit.app/" target="_blank" class="btn-launch">🚀 Launch App</a><a href="https://github.com/MagdalenaRomaniecka/Perfume-Finder-Streamlit" target="_blank" class="btn-code">💻 View Code</a></div>
        </div>
        <div class="project-card">
            <div>
                <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:5px;">📊 ScentSational Analytics</div>
                <div style="color:#F0E68C; font-size:0.6rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; font-weight:bold;">Data Source: Fragrantica Data</div>
                <div style="color:#888; font-size:0.8rem; margin-bottom:20px; line-height:1.4;">Deep learning analysis and visualization of global community olfactory insights.</div>
            </div>
            <div style="margin-top:auto;"><a href="https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/" target="_blank" class="btn-launch">🚀 Launch App</a><a href="https://github.com/MagdalenaRomaniecka/Olfactory-Insights" target="_blank" class="btn-code">💻 View Code</a></div>
        </div>
        <div class="project-card">
            <div>
                <div style="color:#D4AF37; font-family:'Tenor Sans', sans-serif; font-size:1.1rem; margin-bottom:5px;">🧪 ScentSational LFS Hub</div>
                <div style="color:#F0E68C; font-size:0.6rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; font-weight:bold;">Data Source: Git LFS Storage</div>
                <div style="color:#888; font-size:0.8rem; margin-bottom:20px; line-height:1.4;">Backend engineering hub designed to handle massive, heavy fragrance datasets.</div>
            </div>
            <div style="margin-top:auto;"><a href="https://baphomert-scentsational-fragrantica-lfs2.hf.space/" target="_blank" class="btn-launch">🚀 Launch App</a><a href="https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS" target="_blank" class="btn-code">💻 View Code</a></div>
        </div>
    </div>
    """
    st.markdown(ecosystem_html, unsafe_allow_html=True)

# --- GLOBAL FOOTER ---
st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">FRAGRANCE INTELLIGENCE HUB • DEVELOPED BY MAGDALENA ROMANIECKA</div>', unsafe_allow_html=True)