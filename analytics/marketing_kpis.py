import pandas as pd

df = pd.read_csv("data/processed/marketing_campaigns_processed.csv")

kpis = df.groupby("channel").agg({
    "cost": "sum",
    "leads": "sum",
}).reset_index()

kpis["cpl"] = kpis["cost"] / kpis["leads"]

kpis["performance"] = kpis["cpl"].apply(lambda x: "Alta" if x < 15 else "Baixa")

kpis = kpis.sort_values("cpl")
kpis["ranking_custo"] = range(1, len(kpis) + 1)

kpis.to_csv("data/processed/marketing_kpis.csv", index=False)
print("KPIs de marketing calculados com sucesso!")
print(kpis)