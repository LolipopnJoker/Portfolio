#' @title Project 1 analysis
#' @author Yoav Weller
#' @source https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies
#' @description Analyzing information about the top 1000 highest grossing Hollywood films. 
#' It is up to date as of 10th January 2022.
#' @details This data has been scraped from multiple site and has been added together
#' for performing various data operations. The data has been taken from IMDB,
#' rotten tomatoes and many other sites.

# Imports ------------------------------------------

library(tidyverse) # Importing tidyverse
library(tm) # Importing tm
library(syuzhet) # Importing syuzhet

DB  <- read.csv('G:/My Drive/Portfolio/R/Project_1/dataset.csv', row.names = 1) # Importing the data.
                                                                                # The first column is
                                                                                # row indexes, therefor
                                                                                # the argument row.names
                                                                                # is needed.

# Data Cleaning ------------------------------------

# Splitting the date column
DB <- separate(DB, Release.Date, c("release.month", "release.day", "release.year"), sep = " ") # Separating the date column
DB <- separate(DB, Genre, c("Genre.1", "Genre.2", "Genre.3", "Genre.4", "Genre.5", "Genre.6"), sep = ", ")# Separating the genre column

# Cleaning from unwanted symbols that might affect the analysis.
DB[] <- lapply(DB, gsub, pattern=',', replacement='') # Deleting all the , symbols.
DB[] <- lapply(DB, gsub, pattern="'", replacement='') # Deleting all the ' symbols.
DB[] <- lapply(DB, gsub, pattern='\\[', replacement='') # Deleting all the [ symbols.
DB[] <- lapply(DB, gsub, pattern='\\]', replacement='') # Deleting all the ] symbols.

# Descriptive Statistics ----------------------------

worldwide_sales_mean <- mean(as.numeric(DB$World.Sales..in...), na.rm = TRUE)
worldwide_sales_sd <- sd(as.numeric(DB$World.Sales..in...), na.rm = TRUE)

# Sentiment Analysis --------------------------------

corpus <- iconv(DB$Movie.Info, to = "utf-8") # Creating a list with all the movie descriptions
                                             # using UTF-8 encoding.

## Obtain sentiment score
sentiment_score_DF <- get_nrc_sentiment(corpus) # Creating a dataframe with sentiment scores.

full_DB <- cbind(DB, sentiment_score_DF) # Merging the dataframes

## Creating a linear model

linear_model <- lm(full_DB$World.Sales..in...~full_DB$anger+full_DB$anticipation+
                     full_DB$disgust+full_DB$fear+full_DB$joy+full_DB$sadness+
                     full_DB$surprise+full_DB$trust+full_DB$negative+full_DB$positive)

summary(linear_model)
