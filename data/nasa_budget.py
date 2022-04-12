import os
from dotenv import load_dotenv
import requests, json
load_dotenv()

SHEETS_API = os.getenv('SHEETS_API_KEY')
SPREADSHEET_ID = "12frTU01gfT1CXGWFimN3whf4348F_r3XolTqBt02OyM"

NASA_MISSION_BUDGET = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Introduction?key={SHEETS_API}"

url = requests.get(NASA_MISSION_BUDGET)

data = json.loads(url.text)
print(data)