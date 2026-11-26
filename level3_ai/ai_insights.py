import pandas as pd

df = pd.read_csv(
    "../data/processed/final_dataset.csv"
)

top_decade = (
    df.groupby("decade")
      ["popularity"]
      .mean()
      .idxmax()
)

print(
    f"Most popular decade: {top_decade}"
)