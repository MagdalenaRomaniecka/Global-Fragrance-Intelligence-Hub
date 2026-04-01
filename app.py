import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Audio Intelligence Hub | Strategic Insights 2026",
    page_icon="📊",
    layout="wide"
)

# --- MAIN HEADER ---
st.title("📊 Audio Intelligence Hub")
st.subheader("Data-Driven Fragrance Market Analysis & Forecasts")
st.markdown("---")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Strategic Navigation")
st.sidebar.markdown("Select a briefing to begin your analysis:")

# The navigation list including the new Foundation (Base Notes)
selection = st.sidebar.radio(
    "Intelligence Briefings:",
    [
        "0. Global Foundation", 
        "Ep. 1: Recession Glam", 
        "Ep. 2: Global Trade", 
        "Ep. 3: 2026 Outlook", 
        "Ep. 4: European Barbell", 
        "Master Strategic Synthesis"
    ]
)

# Mapping selections to the specific markdown filenames
# Ensure these names match your files in VS Code exactly
file_map = {
    "0. Global Foundation": "master_prologue.md",
    "Ep. 1: Recession Glam": "trend_report_2025.md",
    "Ep. 2: Global Trade": "ep2_trade_report.md",
    "Ep. 3: 2026 Outlook": "ep3_outlook_report.md",
    "Ep. 4: European Barbell": "barbell_strategy_2026.md",
    "Master Strategic Synthesis": "master_synthesis.md"
}

# --- CONTENT RENDERING ENGINE ---
# This block reads the selected markdown file and displays it
target_file = file_map.get(selection)

if target_file:
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content)
    except FileNotFoundError:
        st.error(f"Critical Error: The file **{target_file}** was not found in the root directory.")
        st.info("Check your VS Code explorer and ensure the filename matches exactly (case-sensitive).")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Intelligence Hub curated by Magdalena Romaniecka ✦ Strategic Data Synthesis 2026")