#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

word_content <- c("green", "blue", "yellow", "pink", "purple")

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
# Define UI for application that draws a histogram
shinyUI(fluidPage(

    # Application title
    titlePanel("Old Faithful Geyser Data"),

    # Sidebar with a slider input for number of bins
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),

        # Show a plot of the generated distribution
        mainPanel(
            p(sample(word_content, 1))
        )
    )
))
