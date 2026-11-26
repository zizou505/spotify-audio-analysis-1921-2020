import streamlit as st
import pandas as pd

from level2_dashboard.home_dashboard import home_dashboard
from level2_dashboard.music_explorer import music_explorer
from level2_dashboard.audio_analysis import audio_analysis

st.set_page_config(
    page_title="Spotify Analytics Dashboard",
    page_icon="🎵",
    layout="wide"
)

df = pd.read_csv("data/tracks.csv")

st.sidebar.title("🎵 Spotify Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home Dashboard",
        "Music Explorer",
        "Audio Analysis"
    ]
)

if page == "Home Dashboard":
    home_dashboard(df)

elif page == "Music Explorer":
    music_explorer(df)

elif page == "Audio Analysis":
    audio_analysis(df)
