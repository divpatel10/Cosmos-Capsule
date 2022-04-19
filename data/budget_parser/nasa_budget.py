
from data.budget_parser.google_sheets_parser import get_data_json
import json
import numpy as np
from dotenv import load_dotenv
load_dotenv()
# method formats the Mission Costs google sheet and returns its data
def get_mission_costs():
    df_sheet = get_data_json("Mission Costs")

    # if its only summary, we only need the first four rows from the google sheet
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


