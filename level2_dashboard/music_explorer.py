import streamlit as st

def music_explorer(df):

    st.title("🎵 Music Explorer")

    search = st.text_input("Search a song")

    popularity = st.slider(
        "Popularity",
        0,
        100,
        (0,100)
    )

    filtered = df[
        (df["popularity"] >= popularity[0]) &
        (df["popularity"] <= popularity[1])
    ]

    if search:
        filtered = filtered[
            filtered["name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        filtered[
            [
                "name",
                "artists",
                "popularity",
                "release_date"
            ]
        ]
    )