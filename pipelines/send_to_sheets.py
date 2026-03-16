import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

client = gspread.authorize(creds)

spreadsheet = client.open("marketing_data_dashboard")

# ---------- DADOS PROCESSADOS ----------
sheet_data = spreadsheet.sheet1

df = pd.read_csv("data/processed/marketing_campaigns_processed.csv")

sheet_data.clear()

sheet_data.update(
    [df.columns.values.tolist()] + df.values.tolist()
)

# ---------- KPIS ----------
try:
    sheet_kpis = spreadsheet.worksheet("marketing_kpis")
except:
    sheet_kpis = spreadsheet.add_worksheet(title="marketing_kpis", rows="100", cols="20")

kpis = pd.read_csv("data/processed/marketing_kpis.csv")

sheet_kpis.clear()

sheet_kpis.update(
    [kpis.columns.values.tolist()] + kpis.values.tolist()
)

print("Dados enviados para Google Sheets com sucesso!")