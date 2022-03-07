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

# Splitting the date column
DB <- separate(DB, Release.Date, c("release.month", "release.day", "release.year"), sep = " ")
DB <- separate(DB, Genre, c("Genre.1", "Genre.2", "Genre.3", "Genre.4", "Genre.5", "Genre.6"), sep = ", ")

# Cleaning from unwanted symbols that might affect the analysis.
DB[] <- lapply(DB, gsub, pattern=',', replacement='')
DB[] <- lapply(DB, gsub, pattern="'", replacement='')
DB[] <- lapply(DB, gsub, pattern='\\[', replacement='')
DB[] <- lapply(DB, gsub, pattern='\\]', replacement='')

# Descriptive Statistics ----------------------------

worldwide_sales_mean <- mean(as.numeric(DB$World.Sales..in...), na.rm = TRUE)
worldwide_sales_sd <- sd(as.numeric(DB$World.Sales..in...), na.rm = TRUE)
