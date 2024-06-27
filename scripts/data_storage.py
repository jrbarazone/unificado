import os
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
keyfile_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
creds = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)
