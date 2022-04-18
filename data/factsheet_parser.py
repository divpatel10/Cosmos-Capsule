import pandas as pd

METRIC_DATA_TYPE = "metric"
IMPERIAL_DATA_TYPE = "us"
TEN_POWER = "(10"
PER_POWER = "/s /m /ft"

# Method reads a url and returns the DataFrame of the table from the URL
def gen_factsheet(data_unit):

    if data_unit == METRIC_DATA_TYPE:
        PLANETARY_FACTSHEET = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"
    else:
        PLANETARY_FACTSHEET = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_british.html"

    data = pd.read_html(PLANETARY_FACTSHEET,index_col=0)
    data = data[0]

    new_header = data.iloc[0]
    data = data[1:]

    data.columns = new_header

    # Index String formatting 
    idx_list = data.index.tolist()
    j = 0


# Iterate through the DataFrame for formatting
    for idx in data.index.values:
        newstr = ''
        if "?" in str(idx):
            newstr = idx[:-1]
            idx_list[j] = newstr 
            
        elif TEN_POWER in str(idx):
            i = idx.index(TEN_POWER) + len(TEN_POWER)
            newstr = idx[:i] + '^' + idx[i:]
            idx_list[j] = newstr 

        elif "/" in str(idx):
            pwr_list = PER_POWER.split()
            for pwr in pwr_list:

                if pwr in str(idx):
                    i = idx.index(pwr) + len(pwr)
                    if idx[i] != ')':
                        newstr = idx[:i] + '^' + idx[i:]
                        idx_list[j] = newstr
        j+=1


    data.index = idx_list
    data = data[:-1].transpose()
    
    return data

# method that returns the factsheet Dataframe
def get_factsheet( units = METRIC_DATA_TYPE):
    return gen_factsheet(units)


