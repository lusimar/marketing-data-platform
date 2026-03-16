import subprocess

print("Iniciando pipeline de marketing data...")

print("0 Gerando dados simulados")
subprocess.run(["python", "pipelines/generate_marketing_data.py"])

print("1️ Ingestion")
subprocess.run(["python", "pipelines/ingestion.py"])

print("2️ Transformation")
subprocess.run(["python", "pipelines/transformation.py"])

print("3️ Analytics")
subprocess.run(["python", "analytics/marketing_kpis.py"])

print("4️ Enviando para Google Sheets")
subprocess.run(["python", "pipelines/send_to_sheets.py"])

print("Pipeline finalizado com sucesso!")