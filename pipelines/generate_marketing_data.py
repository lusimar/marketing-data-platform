import pandas as pd
import random
from datetime import datetime, timedelta

channels = [
    "Google Ads",
    "Facebook Ads",
    "Instagram Ads",
    "Email"
]

campaigns = [
    "Search Campaign",
    "Lead Campaign",
    "Remarketing",
    "Newsletter"
]

data = []

start_date = datetime(2024,1,1)

for i in range(30):

    date = start_date + timedelta(days=i)

    for channel in channels:

        cost = random.randint(50,600)
        clicks = random.randint(200,1500)
        leads = random.randint(10,80)

        data.append([
            date.strftime("%Y-%m-%d"),
            channel,
            random.choice(campaigns),
            cost,
            clicks,
            leads
        ])

df = pd.DataFrame(
    data,
    columns=[
        "date",
        "channel",
        "campaign",
        "cost",
        "clicks",
        "leads"
    ]
)

df.to_csv("data/raw/marketing_campaigns.csv", index=False)

print("Dados de marketing gerados!")