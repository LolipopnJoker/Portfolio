#' @title Project 1 analysis
#' @author Yoav Weller
#' @source https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies
#' @description Analyzing information about the top 1000 highest grossing Hollywood films. 
#' It is up to date as of 10th January 2022.
#' @details This data has been scraped from multiple site and has been added together
#' for performing various data operations. The data has been taken from IMDB,
#' rotten tomatoes and many other sites.

# Imports ------------------------------------------

suppressWarnings(library(tidyverse)) # Importing tidyverse
suppressWarnings(library(tm)) # Importing tm
suppressWarnings(library(syuzhet)) # Importing syuzhet
suppressWarnings(library(srt))# Importing srt
suppressWarnings(library(glue)) # Importing glue

subtitles <- t(read_srt('G:/My Drive/Portfolio/R/Project_1/subtitles/890.srt')) # Experimenting with importing an SRT file
subtitles <- as.data.frame(subtitles)
subtitles <- unite(subtitles, col = "subtitles", 1:ncol(subtitles), remove = TRUE, sep = " ")

DB  <- read.csv('G:/My Drive/Portfolio/R/Project_1/dataset.csv', row.names = 1) # Importing the data.
                                                                                # The first column is
                                                                                # row indexes, therefor
                                                                                # the argument row.names
                                                                                # is needed.

DB$Subtitles <- NA

number_of_subtitles_files <- 918

progress_bar <- txtProgressBar(min = 0,
                               max = number_of_subtitles_files,
                               style = 3,
                               width = 50,
                               char = "=")

for (i in 1:number_of_subtitles_files){
try({
  subtitle_path <- glue('G:/My Drive/Portfolio/R/Project_1/subtitles/{i}.srt')
  subtitle <- suppressWarnings(t(read_srt(subtitle_path)))
  subtitle <- as.data.frame(subtitle)
  subtitle <- unite(subtitle, col = "subtitles", 1:ncol(subtitle), remove = TRUE, sep = " ")
  DB$Subtitles[i] <- subtitle$subtitle[4] 
  setTxtProgressBar(progress_bar, i)
},
silent = TRUE)
}

close(progress_bar)
sum(is.na(DB$Subtitles))
for (i in 1:number_of_subtitles_files){
  subtitle_path <- glue('G:/My Drive/Portfolio/R/Project_1/subtitles/{i}.srt')
  print(subtitle_path)
  }
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
