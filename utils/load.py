import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

def load_to_csv(dataframe, nama_file="products.csv"):
    dataframe.to_csv(nama_file, index=False)

def load_to_google_sheets(dataframe, spreadsheet_id, range_sheet):
    kredensial = Credentials.from_service_account_file("google-sheets-api.json")
    service = build("sheets", "v4", credentials=kredensial)
    sheet = service.spreadsheets()
    values = dataframe.values.tolist()
    body = {"values": values}

    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_sheet,
        valueInputOption="RAW",
        body=body,
    ).execute()

def load_to_postgresql(dataframe, nama_tabel="products"):
    try:
        user = "postgres"
        pw = "postgres"
        host = "localhost"
        port = "5432"
        db = "pemda_db"

        engine = create_engine(f"postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}")
        dataframe.to_sql(nama_tabel, engine, if_exists="replace", index=False)
        print(f"Data telah disimpan ke tabel PostgreSQL: '{nama_tabel}'")

    except Exception as err:
        print(f"Kesalahan saat menyimpan ke PostgreSQL: {err}")