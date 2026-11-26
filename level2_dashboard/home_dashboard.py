import streamlit as st
import pandas as pd
import plotly.express as px


def home_dashboard(df):

    # Create year column
    df["year"] = pd.to_datetime(
        df["release_date"],
        errors="coerce"
    ).dt.year

    st.title("🎵 Spotify Analytics Dashboard")

    # ======================
    # KPI CARDS
    # ======================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Tracks",
        f"{len(df):,}"
    )

    col2.metric(
        "Artists",
        df["artists"].nunique()
    )

    col3.metric(
        "Average Popularity",
        round(df["popularity"].mean(), 2)
    )

    col4.metric(
        "Top Song",
        df.loc[df["popularity"].idxmax(), "name"]
    )

    st.divider()

    # ======================
    # TOP 100 ARTISTS
    # ======================

    st.subheader("🏆 Top 100 Artists")

    top_artists = (
        df.groupby("artists")["popularity"]
        .mean()
        .sort_values(ascending=False)
        .head(100)
        .reset_index()
    )

    fig_artists = px.bar(
        top_artists,
        x="popularity",
        y="artists",
        orientation="h",
        color="popularity"
    )

    st.plotly_chart(
        fig_artists,
        use_container_width=True
    )

    # ======================
    # TOP 200 SONGS
    # ======================

    st.subheader("🎶 Top 200 Songs")

    top_songs = (
        df.sort_values(
            "popularity",
            ascending=False
        )
        .head(200)
    )

    fig_songs = px.bar(
        top_songs,
        x="popularity",
        y="name",
        orientation="h",
        color="popularity"
    )

    st.plotly_chart(
        fig_songs,
        use_container_width=True
    )

    # ======================
    # POPULARITY TREND
    # ======================

    st.subheader("📈 Popularity Trend")

    trend = (
        df.groupby("year")["popularity"]
        .mean()
        .reset_index()
    )

    fig_trend = px.line(
        trend,
        x="year",
        y="popularity",
        markers=True
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

    # ======================
    # HISTOGRAMS
    # ======================

    col1, col2 = st.columns(2)

    with col1:

        fig_pop = px.histogram(
            df,
            x="popularity",
            nbins=50
        )

        st.plotly_chart(
            fig_pop,
            use_container_width=True
        )

    with col2:

        fig_energy = px.histogram(
            df,
            x="energy",
            nbins=50
        )

        st.plotly_chart(
            fig_energy,
            use_container_width=True
        )

    # ======================
    # TOP 300 TABLE
    # ======================

    st.subheader("🏅 Top 300 Songs")

    top300 = (
        df.sort_values(
            "popularity",
            ascending=False
        )[
            [
                "name",
                "artists",
                "popularity",
                "release_date"
            ]
        ]
        .head(300)
    )

    st.dataframe(
        top300,
        height=600,
        use_container_width=True
    )