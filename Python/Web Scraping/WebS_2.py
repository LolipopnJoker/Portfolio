"""
Based on Yahoo's financial API, I created a function that takes the trading paper symbol and returns
real time quote data for stocks, ETFs, mutuals funds, bonds, crypto and national currencies.

The second version of the function runs the function every N seconds.
"""
__author__ = "Yoav Weller"
__copyright__ = "Copyright 2022, Purple Dove"
__credits__ = ["Yoav Weller"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoav Weller"
__email__ = "yoav.weller@gmail.com"
__status__ = "Production"

def Yahoo_Raw_Data_V6(symbol):
    """
    Based on Yahoo's financial API, I created a function that takes the trading paper symbol and returns
    real time quote data for stocks, ETFs, mutuals funds, bonds, crypto and national currencies.

    ...

    Importing Modules:
    -----------------
    """
    
    import requests
    from pandas.io.json import json_normalize
   
    """
    Attributes
    ----------
    symbol : str
        The symbols of the papers to search. It can be one, or more, symbols (If more than one symbol is
        to be searched - a comma shell be used between each symbol).

    ...

    An Example
    ----------
    Yahoo_Raw_Data_V6("AAPL,BTC-USD,EURUSD=X") 

    """

    """ Lines 46 to 55 were copied from Yahoo's financial API websites'. """
    url = "https://yfapi.net/v6/finance/quote"
    
    querystring = {"symbols":symbol} # The products I'm following after.

    headers = {
        'x-api-key': "6rkx6BIKro3bjZT5Q2neg89xVoOrU6sP3kNWljj7" # API KEY
            }

    response = requests.request("GET", url, headers = headers, params = querystring)
    response_text = response.json()

    raw_data_Yahoo = json_normalize(response_text, ['quoteResponse', 'result']) # Normalize semi-structured JSON data into a flat table.
   
    return raw_data_Yahoo # Returning a dataframe with 80 variables.

def Yahoo_Raw_Data_V6_V2(symbol, seconds):
    """
    This is an upgrade of the previous function - it allowas us to execute the function every N seconds.
    
    In this version of the function, the output is a dataframe being printed to the console every N seconds.
    In future updates of this function I intened to send the dataframe to an SQL server, insted of printing
    it to the console.
    ...

    Attributes
    ----------
    symbol : str
        The symbols of the papers to search. It can be one, or more, symbols (If more than one symbol is
        to be searched - a comma shell be used between each symbol).
    seconds: int
        Inreval, in seconds.

    ...

    An Example
    ----------
    Yahoo_Raw_Data_V6_V2("AAPL,BTC-USD,EURUSD=X", 20)
    ...

    Importing Modules:
    -----------------
    """
    import time
    import pandas as pd
    
    container_df = pd.DataFrame() # Creating an empty dataframe that will store all the data from the API.
    
    iteration_count = 0

    while(iteration_count<5):
        DF = pd.DataFrame(Yahoo_Raw_Data_V6(symbol))
        container_df = container_df.append(DF, ignore_index=True, sort=False)
        container_df.to_csv('Yahoo_V6_Raw_Data.csv')
        iteration_adding_string = f"This is iteration number {iteration_count+1}.\nThe data is updating every {seconds}, just like you asked for!"
        iteration_count += 1
        print(iteration_adding_string)
        time.sleep(seconds)
    
    finished_string = f"Hey, just to let you know we finished scanning the papers you wanted.\nWe searched {iteration_count} times, with {seconds} seconds interval between each search.\nHave a great day!"
    print(finished_string)

Yahoo_Raw_Data_V6_V2("AAPL,BTC-USD,EURUSD=X", 10)