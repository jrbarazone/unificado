import os
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
keyfile_path = '/app/sqlbarazone-2fdbb67f3964.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scope)
