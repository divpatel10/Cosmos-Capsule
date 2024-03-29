# Cosmos Capsule

## Installation:
### Install dependencies: `pip3 install -r requirements.txt` 
### Run the API: `python3 main.py`
### Endpoints:
* `/factsheet` 
	* GET request to this endpoint will respond with a JSON object which will contain all the information about the planet facts.
	* **Queries**: 
		* `units`: Can be set to `"us"` for US units or `"metric"` for SI. (Metric is set by default)
		* `planet`: To filter a specifc Planet's Info(eg `/factsheet?planet=mars`)

* `/budget` 
	* In order to run `Budget` Endpoints,Obtain an API for Google sheets from the Google Developer Console,
	 	create a `.env` file in the base directory and write the following line in the .env file replacing
		 `ENTER_YOUR_API_KEY` with the API key obtained from Google Developer Console:
		 
        `SHEETS_API_KEY=ENTER_YOUR_API_KEY`

	* GET request to this endpoint will respond with a JSON object which will contain data about the budget of NASA Missions.
	* `/budget/mission_name` 
	    * GET request to this endpoint will respond with a JSON object which will contain budget details of the specified mission name.
	* `/budget/all` 
	    * GET request to this endpoint will respond with a JSON object which will contain a summary of budget details for all missions.
	    
	

### Notes:
-For Factsheet, Although they are not planets, The API also contains data for Moon and Pluto

