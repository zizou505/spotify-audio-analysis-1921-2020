import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def audio_analysis(df):

    st.title("📊 Audio Analysis")

    features = [
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "popularity"
    ]

    corr = df[features].corr()

    fig, ax = plt.subplots(figsize=(10,8))

    sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=True,
        ax=ax
    )

    st.pyplot(fig)

    feature = st.selectbox(
        "Choose Feature",
        features
    )

    fig2, ax2 = plt.subplots()

    ax2.hist(
        df[feature],
        bins=30
    )

    ax2.set_title(feature)

    st.pyplot(fig2)