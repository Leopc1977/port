import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def upload_gg_sheet(filepath):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds_filepath = 'res/prospect-auto-944271ae2f64.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        creds_filepath, scope)
    gc = gspread.authorize(credentials)

    spreadsheet_name = "Prospect"
    csv_file_path = filepath

    df = pd.read_csv(csv_file_path)
    try:
        sh = gc.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        sh = gc.create(spreadsheet_name)

    worksheet = sh.get_worksheet(0)
    worksheet.clear()
    gc.import_csv(sh.id, df.to_csv(index=False))

    print(f"CSV data has been successfully imported into {spreadsheet_name}.")
