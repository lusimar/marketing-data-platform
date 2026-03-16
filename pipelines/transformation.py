import pandas as pd

df = pd.read_csv("data/raw/marketing_campaigns.csv")

df["cpc"] = df["cost"] / df["clicks"]
df["cpl"] = df["cost"] / df["leads"]

df.to_csv("data/processed/marketing_campaigns_processed.csv", index=False)

print("Dados transformados com sucesso!")