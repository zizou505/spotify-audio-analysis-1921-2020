import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(
    "../data/processed/final_dataset.csv"
)

features = [
    "danceability",
    "energy",
    "valence",
    "acousticness"
]

similarity = cosine_similarity(
    df[features]
)

print(similarity.shape)