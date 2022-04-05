# NASA Planetary Factsheet API

## Installation:
### Install dependencies: `pip3 install -r requirements.txt` 
### Run the API: `uvicorn factsheet:app --reload`
### Endpoints:
* `/factsheet` 
	* GET request to this endpoint will respond with a JSON object which will contain all the information about the planet facts.
	
	* **Queries**: 
		* `?units`: Can be set to `"us"` for US units or `"metric"` for SI. (Metric is set by default)
		*`?planet`: To filter a specifc Planet's Info(eg `/factsheet?planet=mars`)

### Notes:
-Although they are not planets, The API also contains data for Moon and Pluto