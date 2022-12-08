###################################
# - Calling necessary libraries
###################################

library(dplyr)
library(tidyr)
library(ggplot2)
library(extrafont)
library(reshape2)
library(tidyr)

setwd("C:\\Users\\roedj\\Documents\\GitHub\\homework_MSIS5193\\project-deliverable-2-orange-intelligence-bureau\\")

###################################
# - Read in data set
###################################

df_viz4 = read.csv("data\\consolidated\\final_rent.csv", header = T)

###################################
# - Data transformation to fit visualization
###################################

df_viz4_1 <- (df_viz4 
              # select relevant columns
              %>% select(Year, Overall.Median.Rent,No.bedroom,X1.bedroom,X2.bedrooms,X3.bedrooms,X4.bedrooms,X5.or.more.bedrooms) 
              # unpivot rent prices columns
              %>% melt(id=c('Year'), value.name=c('Rent Prices'), variable.name=c('Number of Rooms'))
              # recoding number of rooms to shorter text values
              %>% mutate(`Number of Rooms`=recode(`Number of Rooms`, 
                         "Overall.Median.Rent" = "Overall",
                         "No.bedroom" = "None",
                         "X1.bedroom" = "One",
                         "X2.bedrooms" = "Two",
                         "X3.bedrooms" = "Three",
                         "X4.bedrooms" = "Four",
                         "X5.or.more.bedrooms" = "Five or more"))
              # remove number of rooms == overall as it is not used
              %>% filter(`Number of Rooms` != "Overall")
              # Grouping data into "2 rooms or less" and "3 rooms or more" so that graphics will not be confusing
              %>% mutate(group_number_rooms = ifelse(`Number of Rooms` %in% c("None","One","Two"), '2 rooms or less', '3 rooms or more'))
              %>% select(-`Number of Rooms`)
              %>% group_by(group_number_rooms, Year) 
              %>% summarise(Rent_Prices = mean(`Rent Prices`)))

# joining back grouped data to original data
df_viz4_2 = merge(df_viz4_1,df_viz4) 

# select relevant columns
df_viz4_2 = (df_viz4_2 
             %>% select(Year, group_number_rooms, Rent_Prices, Median.Age))


###################################
# - creating theme
###################################


plot_theme = (
  ggplot(df_viz4_2, aes(x=Median.Age)) +
    # limiting y axis
    scale_y_continuous(breaks = seq(600,1200, by = 100)) +
    # setting up x and y axis label, title, and subtitle
    labs(
      x='Median Age in Years',
      y='Median Rent Price in US Dollar',
      title = 'Rent Price vs. Population Age in Stillwater',
      subtitle = 'This chart shows the relationship between median rent prices and median population age in Stillwater.'
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
# - Preparation for regression lines
###################################

# using lm - linear model to obtain model parameters
reg1<-lm(formula = Rent_Prices~Median.Age, data=filter(df_viz4_2,group_number_rooms == '2 rooms or less'))  

# assigning intercept and slope for first regression line
coeff1<-coefficients(reg1)          
intercept1<-coeff1[1]
slope1 <- coeff1[2]

# same processes for second regression
reg2<-lm(formula = Rent_Prices~Median.Age, data=filter(df_viz4_2,group_number_rooms == '3 rooms or more'))  

coeff2<-coefficients(reg2)          
intercept2<-coeff2[1]
slope2 <- coeff2[2]

###################################
# - Visualize
###################################

# instantiate parameters for arrows
arrow_1 = tibble(
  x1 = c(23.8),
  y1 = c(790),
  x2 = c(23.78),
  y2 = c(670)
)

arrow_2 = tibble(
  x1 = c(23.68),
  y1 = c(990),
  x2 = c(23.73),
  y2 = c(1090)
)

plot_theme + 
  # plot scatterplot with rent prices over years based on number of rooms
  geom_point(aes(y=Rent_Prices, color=group_number_rooms)) +
  # plot regression line 1
  geom_abline(intercept = intercept1, slope = slope1, color="red", alpha=0.5, size=1) + 
  # plot regression line 2
  geom_abline(intercept = intercept2, slope = slope2, color="blue", alpha=0.5, size=1) +
  # input annotation for explanation
  annotate('text', x = 23.75, y = 680, size = 4, color='red', 
           label = glue::glue('Slope = ', round(slope1[[1]],2))) + 
  annotate('text', x = 23.75, y = 1120, size = 4, color='blue', 
           label = glue::glue('Slope = ', round(slope2[[1]],2))) +
  geom_label(x = 23.8, y = 810, size = 4, color='black', fill = 'pink',
             label = glue::glue('When there are 2 rooms or less, there are virtually \nno relationship between rent prices and population age.')) + 
  # input arrow
  geom_curve(data = arrow_1, 
             aes(x = x1, y = y1, xend = x2, yend = y2),
             arrow = arrow(length = unit(0.07, 'inch')), 
             size = 0.4,
             color = 'red', 
             curvature = 0.2) +
  geom_label(x = 23.68, y = 980, size = 4, color='black', fill = 'lightblue',
             label = glue::glue('When there are 3 rooms or more, rent prices increases with population age.')) + 
  geom_curve(data = arrow_2, 
             aes(x = x1, y = y1, xend = x2, yend = y2),
             arrow = arrow(length = unit(0.07, 'inch')), 
             size = 0.4,
             color = 'blue', 
             curvature = 0.2)


