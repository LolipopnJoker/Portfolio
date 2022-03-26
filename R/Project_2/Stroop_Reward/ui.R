#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(glue)



green_rgb <- c(0, 255, 0)
blue_rgb <- c(0, 0, 255)
yellow_rgb <- c(234, 221, 202)
pink_rgb <- c(255,192,203)
purple_rgb <- c(153,50,204)
color_codes <- list(green_rgb,
                    blue_rgb,
                    yellow_rgb,
                    pink_rgb,
                    purple_rgb)

displayed_color <- sample(color_codes, 1)
# Define UI for application that draws a histogram
shinyUI(fluidPage(

    # Application title
    titlePanel("Our Research"),

    # Show a plot of the generated distribution
    mainPanel(
        fluidRow(
            align = "center",
            textOutput("target_word")
        )
    )
)
)
