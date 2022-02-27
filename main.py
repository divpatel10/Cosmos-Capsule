from ast import Eq
import pandas as pd


data = pd.read_html("https://nssdc.gsfc.nasa.gov/planetary/factsheet/",index_col=0)

data = data[0]

new_header = data.iloc[0]
data = data[1:]

data.columns = new_header

d_json = data.to_json(orient='index')

TEN_POWER = "(10"
PER_POWER = "/s /m"

print(type(TEN_POWER))


# Index String formatting 
idx_list = data.index.tolist()
j = 0

print(list(data.index.values))

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

print(list(data.index.values))
# print(data.head())

