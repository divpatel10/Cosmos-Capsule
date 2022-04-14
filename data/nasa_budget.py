import os
from dotenv import load_dotenv
import requests, json
import pandas as pd
load_dotenv()

SHEETS_API = os.getenv('SHEETS_API_KEY')
SPREADSHEET_ID = "12frTU01gfT1CXGWFimN3whf4348F_r3XolTqBt02OyM"


def get_data_json(sheet_name):
    ADD_KEY = f"?key={SHEETS_API}"
    NASA_MISSION_BUDGET = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/"

    URL = f"{NASA_MISSION_BUDGET}{sheet_name}{ADD_KEY}"

    try:
        url = requests.get(URL).text
    except:
        return("Unhandled Exception")
    
    # we only need the values from the google sheets API 
    data_json = json.loads(url)["values"]

    df_sheet = pd.DataFrame.from_dict(data_json)

    # make the first row as column header
    new_header = df_sheet.iloc[0]
    df_sheet = df_sheet[1:]
    df_sheet.columns = new_header



    return df_sheet
    



def get_mission_costs(only_summary = False):
    df_sheet = get_data_json("Mission Costs")

    

    if only_summary:
        # drop all rows except the first 4
        df_sheet = df_sheet.drop( df_sheet.index.to_list()[4:] ,axis = 0 )
        # df_sheet = df_sheet.transpose()

    return df_sheet
    # if its only summary, we only need the first 
    
get_mission_costs()
# print(json_data)