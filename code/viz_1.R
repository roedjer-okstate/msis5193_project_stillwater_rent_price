###################################
# - Calling necessary libraries
###################################

library(dplyr)
library(tidyr)
library(ggplot2)
library(extrafont)
library(reshape2)

setwd("C:\\Users\\roedj\\Documents\\GitHub\\homework_MSIS5193\\project-deliverable-2-orange-intelligence-bureau\\")

###################################
# - Read in data set
###################################

df_viz1 = read.csv("data\\consolidated\\final_rent.csv", header = T)

###################################
# - Data transformation to fit visualization
###################################

df_viz1 <- (df_viz1 
            # select relevant columns
            %>% select(Year,Overall.Median.Rent,No.bedroom,X1.bedroom,X2.bedrooms,X3.bedrooms,X4.bedrooms,X5.or.more.bedrooms) 
            # unpivot rent prices columns
            %>% melt(id=c('Year'), value.name=c('Rent Prices'), variable.name=c('Number of Rooms'))
            # mark years without covid and year with covid
            %>% mutate(before_covid = if_else(Year<=2019, 'green','darkgreen'))
            # recoding number of rooms to shorter text values
            %>% mutate(`Number of Rooms`=recode(`Number of Rooms`, 
                       "Overall.Median.Rent" = "Overall",
                       "No.bedroom" = "None",
                       "X1.bedroom" = "One",
                       "X2.bedrooms" = "Two",
                       "X3.bedrooms" = "Three",
                       "X4.bedrooms" = "Four",
                       "X5.or.more.bedrooms" = "Five or more")))


###################################
# - creating theme
###################################

plot_theme = (
  ggplot(df_viz1, aes(x=Year)) +
    # limiting x and y axis
    scale_y_continuous(breaks = seq(500,1800, by = 250)) +
    scale_x_continuous(breaks = seq(2015,2020, by = 1)) +
    # setting up x and y axis lable, title, and subtitle
    labs(
      x='Year',
      y='Median Rent Price in US Dollar',
      title = 'Rent Price Trend in Stillwater from 2015 to 2020',
      subtitle = 'This is a timeline chart showing trend of the rent prices in Stillwater from 2015 to 2020 based on number of rooms\nto find if the pandemic has any impact.'
    ) +
    theme(
      # setting up axis formatting
      text = element_text(size=12, family = 'Helvetica', color = 'white'),
      axis.title = element_text(size=15, family = 'Helvetica', color = 'white'),
      axis.text.x = element_text(size = 12, family = 'Arial', color = 'white'),
      axis.text.y = element_text(size = 12, family = 'Arial', color = 'white'),
      axis.ticks = element_line(colour = "lightgrey"),
      axis.line = element_line(colour = "lightgrey"),
      
      # setting up background formatting
      plot.background = element_rect(fill = "gray60"),
      panel.background = element_rect(fill = "white"),
      panel.grid.major.y  = element_line(color = "gray90", size = 0.5, linetype = 2),
      
      # setting up title and subtitle formatting
      plot.title = element_text(size=20, family = 'Georgia', color = 'white', face='bold'),
      plot.subtitle = element_text(size = 12, family = 'Helvetica', color = 'white', face = 'italic'),
      
      # setting up legend formatting
      legend.text = element_text(size=14, family = 'Helvetica', color = 'white'),
      legend.title = element_text(size=14, family = 'Georgia', color = 'white', face='bold'),
      legend.position = 'bottom',
      legend.background = element_rect(fill = "gray60")
    ) 
)

###################################
# - Visualize
###################################

# instantiate parameters for arrow
arrow_1 = tibble(
  x1 = c(2019.667),
  y1 = c(1360),
  x2 = c(2019),
  y2 = c(1200)
)

plot_theme + 
  # plotting rent prices according to number of rooms
  geom_line(aes(y=`Rent Prices`, color = `Number of Rooms`), show.legend = T,) + 
  # setting line color preference
  scale_color_manual(values=c("black", "#A50000", "#FF6565","#FFB2B2","#B2BFFF","#6B73FF","#0002A5"), name="Number of Bedrooms") +
  # create 2 boxes on the plot to indicate the if COVID has started 
  geom_tile(aes(y=1000,fill=before_covid), height=1200, alpha=0.01) + guides(fill="none") +
  # plot 1 vertical line to emphasize dips
  geom_vline(aes(xintercept = 2019), color = 'orange', alpha = 0.5) +
  # input annotation for explanation
  annotate('text', x = 2020, y = 1625, size = 4, color='black', 
           label = glue::glue('COVID Started')) +
  annotate('text', x = 2017, y = 1625, size = 4, color='black', 
           label = glue::glue('Before COVID')) +
  geom_label(x = 2019.667, y = 1400, size = 4, color='black', fill = 'grey',
             label = glue::glue('When room numbers are four or more, \nthey suffered great dip in rent prices in 2019')) +
  # input arrow
  geom_curve(data = arrow_1, 
             aes(x = x1, y = y1, xend = x2, yend = y2),
             arrow = arrow(length = unit(0.07, 'inch')), 
             size = 0.4,
             color = 'black', 
             curvature = -0.2)
  #

