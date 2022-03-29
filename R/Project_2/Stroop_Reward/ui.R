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
