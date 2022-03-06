#' Analyzing the S&P stocks between the years 2012 to 2016.
#' 
#' Its name is fundamentals.csv. It includes metrics extracted from
#' annual SEC 10K fillings (2012-2016), should be enough to derive most
#' of popular fundamental indicators.
#' 
#' All the data in fundamentals are from Nasdaq Financials, extended by
#' some fields from EDGAR SEC databases.
#' 
#' @author Yoav Weller
#' @source https://www.kaggle.com/dgawlik/nyse/version/3

# Imports ------------------------------------------

library(tidyverse) # Importing tidyverse

DB = read.csv('G:/My Drive/Portfolio/R/Project_1/fundamentals.csv') # Importing the data

