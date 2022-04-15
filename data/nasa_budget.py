import os
from dotenv import load_dotenv
from numpy import full
import requests, json
import pandas as pd
import numpy as np
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
    global data_json
    data_json = json.loads(url)["values"]
    df_sheet = pd.DataFrame.from_dict(data_json)

    # make the first col as row header
    df_sheet = df_sheet.set_index(df_sheet.columns[0]) 
    
    # make the first row as column header
    new_header = df_sheet.iloc[0]
    df_sheet = df_sheet[1:]
    df_sheet.columns = new_header
    # print(json.dumps( json.loads(temp.transpose().to_json(orient='index')), indent=4))
    return df_sheet

    



def get_mission_costs(only_summary = False):
    df_sheet = get_data_json("Mission Costs")

    # if its only summary, we only need the first four rows from the google sheet
    if True:
        # drop all rows except the first 4
        full_sheet = df_sheet
        full_sheet = full_sheet.iloc[4:]
        df_sheet = df_sheet.drop( df_sheet.index.to_list()[4:] ,axis = 0 )
        
        del df_sheet[df_sheet.columns[0]] # Drops the "Fiscal Year" Empty Column
        
        # Transpose and convert to JSOn
        df_sheet = df_sheet.transpose()
        data = df_sheet.to_json(orient='index')
        data_json = json.loads(data)

        # Iterate through each mission 
        for col in full_sheet.columns:
            if col in data_json:    # If its a mission name (and not other column)
                
                # Filter the DF to be Fiscal Year and the mission
                cur_data = full_sheet[['Fiscal Year', col]] 
                
                # remove null cols
                cur_data = cur_data.replace(to_replace=['None', ''], value=np.nan).dropna() 
                cur_data = cur_data.set_index(cur_data.columns[0]) 
                
                # Transpose the newly filtered matrix ( 1 row, col- Year, val : spending)
                cur_data = cur_data.transpose()
                
                # convert to json, Remove the
                cur_data_json = json.loads(cur_data.to_json(orient='index'))[col]
                
                #Append to the final mission
                data_json[col]["Spending Timeline"] = cur_data_json
                
        return data_json
