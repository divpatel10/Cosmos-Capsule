import pandas as pd

data = pd.read_html("https://nssdc.gsfc.nasa.gov/planetary/factsheet/",index_col=0)

data = data[0]

new_header = data.iloc[0]
data = data[1:]
data.columns = new_header

d_json = data.to_json(orient='index')
print((data.values.tolist()))
print(data)

new_indx = data