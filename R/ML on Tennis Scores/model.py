"""In this file, I created number of classes."""

__author__ = "Yoav Weller"
__copyright__ = "Copyright 2022, Yoav Weller"
__credits__ = ["Yoav Weller"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoav Weller"
__email__ = "yoav.weller@gmail.com"
__status__ = "Production"

# Modules Imports
import pandas as pd

# Importing training Data
first_year_data = 2000 # The first year I have data about
last_year_data = 2017 # Last year I have data about
interval_between_years = 1 # Interval between years

years = list(range(first_year_data, last_year_data + 1, interval_between_years)) # Creating a list with all the years I have data about.

print(years) # Checking if the list contines all the years I have