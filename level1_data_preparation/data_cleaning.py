import pandas as pd

df = pd.read_csv("../data/spotify.csv")

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

df = df.drop_duplicates()

num_cols = df.select_dtypes(include="number").columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include="object").columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df.to_csv(
    "../data/spotify_clean.csv",
    index=False
)

print("Cleaning Complete")