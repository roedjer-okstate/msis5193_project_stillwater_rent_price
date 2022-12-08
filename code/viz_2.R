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

df_viz2 = read.csv("data\\consolidated\\final_rent.csv", header = T)

###################################
# - Data transformation to fit visualization
###################################

df_viz2_1 <- (df_viz2 
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
              # grouping data into "2 rooms or less" and "3 rooms or more" so that graphics will not be confusing
              %>% mutate(group_number_rooms = ifelse(`Number of Rooms` %in% c("None","One","Two"), '2 rooms or less', '3 rooms or more'))
              %>% select(-`Number of Rooms`)
              %>% group_by(group_number_rooms, Year) 
              %>% summarise(Rent_Prices = mean(`Rent Prices`)))


# joining back grouped data to original data
df_viz2_2 = merge(df_viz2_1,df_viz2) 

# select relevant columns and make covid year indication
df_viz2_2 = (df_viz2_2 
             %>% select(Year, group_number_rooms, Rent_Prices, Population, Enrollment)
             %>% mutate(before_covid = if_else(Year<=2019, 'green','darkgreen')))


###################################
# - creating theme
###################################

# instantiate scale for dual axis scaling
scale = 40

plot_theme = (
  ggplot(df_viz2_2, aes(x=Year)) +
    # limiting x and y axis, creating secondary axis
    scale_y_continuous(sec.axis = sec_axis( trans=~.*scale/2, name="OSU Enrollment")) +
    scale_x_continuous(breaks = seq(2015,2020, by = 1)) +
    # setting up x and y axis label, title, and subtitle
    labs(
      x='Year',
      y='Median Rent Price in US Dollar',
      title = 'Rent Price Trend vs. OSU Enrollment in Stillwater',
      subtitle = 'This chart shows trend of the rent prices in Stillwater from 2015 to 2020 and how Oklahoma State University (OSU) \nenrollment has impacted.'
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
  x1 = c(2018.55),
  y1 = c(1410),
  x2 = c(2019),
  y2 = c(1300)
)

plot_theme + 
  # create 2 boxes on the plot to indicate the if COVID has started
  geom_tile(aes(y=750,fill=before_covid), height=1600, alpha=0.02) + guides(fill="none") +
  # plotting bar chart with enrollment as y-axis
  geom_col(aes(y=Enrollment/scale), size=.1, alpha=0.3) +
  # inserting labels for bar chart
  geom_text(aes(y=Enrollment/scale, label = Enrollment), vjust = -22.8, colour = "white") +
  # plotting rent prices according to number of rooms
  geom_line(aes(y=Rent_Prices, color = group_number_rooms), show.legend = T,) +
  # setting line color preference
  scale_color_manual(values=c("red", "blue"), name="Number of Bedrooms") +
  # plot 1 vertical line to emphasize dips
  geom_vline(aes(xintercept = 2019), color = 'black', alpha = 0.5) +
  # input annotation for explanation
  annotate('text', x = 2020, y = 1580, size = 4, color='black', 
           label = glue::glue('COVID Started')) +
  annotate('text', x = 2017, y = 1580, size = 4, color='black', 
           label = glue::glue('Before COVID')) +
  geom_label(x = 2017, y = 1400, size = 4, color='black', fill = 'grey',
           label = glue::glue('When OSU enrollment (24079 students) dipped in 2019, \nthe median rent prices for 3 rooms or more dipped too.')) + 
  # input arrow
  geom_curve(data = arrow_1, 
             aes(x = x1, y = y1, xend = x2, yend = y2),
             arrow = arrow(length = unit(0.07, 'inch')), 
             size = 0.4,
             color = 'black', 
             curvature = -0.2)

