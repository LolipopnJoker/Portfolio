# Imports
library(shiny)
library(shinythemes)

ui <- fluidPage(
  title = 'Follow The Money',
  sidebarLayout(
    sidebarPanel(
      textInput('txtInput', 'Input the text to display')
    ),
    mainPanel(
      paste('You typed'),
      textOutput('txtOutput')
    )
  )
)

server <- function(input, output){}

shinyApp(ui=ui, server = server)
