import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_json_keyfile', scope)
client = gspread.authorize(creds)

# Función para almacenar datos en Google Sheets
def save_to_sheet(barcode, image_url, quantity, description, title):
    sheet = client.open("Product Data").sheet1
    sheet.append_row([barcode, image_url, quantity, description, title])
