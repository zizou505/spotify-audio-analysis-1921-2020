import pandas as pd

df = pd.read_csv("../data/spotify_clean.csv")

df["decade"] = (
    df["year"] // 10
) * 10

df["song_age"] = (
    2026 - df["year"]
)

df["popularity_category"] = pd.cut(
    df["popularity"],
    bins=[0,40,70,100],
    labels=["Low","Medium","High"]
)

df.to_csv(
    "../data/spotify_clean.csv",
    index=False
)

print("Feature Engineering Complete")