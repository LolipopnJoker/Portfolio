#' @title Project 1 analysis
#' @author Yoav Weller
#' @source https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies
#' @description Analyzing information about the top 1000 highest grossing holywood films. 
#' It is up to date as of 10th January 2022.
#' @details This data has been scraped from multiple site and has been added together
#' for performing various datat operations. The data has been taken from idmb,
#' rotten tomatoes and many other sites.

# Imports ------------------------------------------

library(tidyverse) # Importing tidyverse

DB  <- read.csv('G:/My Drive/Portfolio/R/Project_1/dataset.csv', row.names = 1) # Importing the data.
                                                                                # The first column is
                                                                                # row indexes, therefor
                                                                                # the argument row.names
                                                                                # is needed.

# Data Cleaning ------------------------------------

# Creating a for loop that would split the release date
DB <- separate(DB, Release.Date, c("release.month", "release.day", "release.year"), sep = " ")
