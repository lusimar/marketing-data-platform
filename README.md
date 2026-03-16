# Marketing Data Platform

Mini plataforma de dados para análise de campanhas de marketing.

O projeto simula um pipeline de dados usado por times de marketing e BI, realizando:

- geração de dados simulados de campanhas
- ingestão e transformação de dados
- cálculo de KPIs de marketing
- envio automático para Google Sheets
- consumo dos dados em dashboard no Looker Studio

## Arquitetura

Data Generation → Ingestion → Transformation → Analytics → Dashboard

## Tecnologias

Python  
Pandas  
Google Sheets API  
Looker Studio  

## Métricas de Marketing

CPL (Cost per Lead)  
CPC (Cost per Click)  
Leads por canal  
Ranking de canais

## Data Pipeline Architecture
Marketing Data Generation
        ↓
Ingestion Pipeline (Python)
        ↓
Data Transformation
        ↓
Analytics Layer (KPIs)
        ↓
Google Sheets
        ↓
Looker Studio Dashboard

## Como executar o projeto

1 - Clonar repositório

git clone https://github.com/lusimar/marketing-data-platform.git

2 - Instalar dependências

pip install -r requirements.txt

3 - Rodar pipeline

python run_pipeline.py