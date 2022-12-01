#############################################
#=============Read in Libraries=============#
# Read in the necessary libraries.          #
#############################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass
from time import sleep
import pandas as pd
import regex as re
import numpy as np
import zipfile
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir(r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau')

#============================================
# Read in all the cleaned csv
#============================================

age_df = pd.read_csv("data\\transformed\\age_population\\stillwater_age_population.csv")
hh_income_df = pd.read_csv("data\\transformed\\household_income\\household_income.csv")
emp_industry_df = pd.read_csv("data\\transformed\\emp_industry\\emp_industry.csv")
enrollment_df = pd.read_csv("data\\transformed\\enrollment\\enrollment.csv")
property_value_df = pd.read_csv("data\\transformed\\property_value\\property_value.csv")
rent_own_df = pd.read_csv("data\\transformed\\rent_own\\rent_own.csv")
trade_growth_df = pd.read_csv("data\\transformed\\trade_growth\\trade_growth.csv")
rent_df = pd.read_csv("data\\transformed\\census_rent\\overall_census_rent.csv")

#============================================
# Create function to find median class
#============================================

def median_class_finder(freq_col, interval_col, max_col, min_col):
    if freq_col.sum()%2 == 0:
        median_freq = freq_col.sum()/2
    else: 
        median_freq = (freq_col.sum()+1)/2

    cumulative = 0
    for i in range(len(freq_col)):
        cumulative += freq_col[i]
        if median_freq > cumulative:
            continue
        else:
            median_class = interval_col[i]
            print(f"Median Age class : {interval_col[i]}")
            median = (min_col[i]-0.5 + (max_col[i]+0.5-min_col[i]+0.5)*((freq_col.sum()/2-sum(freq_col[:i]))/freq_col[i]))
            print(f"Median : {median}")
            return median_class, median
            break

#============================================
# Consolidating age_df
#============================================

population_df = age_df.drop(['Age_Min','Age_Max'], axis=1).groupby(['Year']).sum()

year_list = []
median_class_list= []
median_list = []


for year in age_df['Year'].unique():
    temp = age_df[age_df['Year']==year].sort_values('Age_Min').reset_index(drop='index')
    print(f"Year {year}")
    median_class, median = median_class_finder(temp['Population'], temp['Age'], temp['Age_Max'], temp['Age_Min'])
    year_list.append(year)
    median_class_list.append(median_class)
    median_list.append(median)

pop_age_df = pd.DataFrame({'Median Age':median_list, 'Population':population_df['Population']}).reset_index()

#============================================
# Consolidating hh_income_df
#============================================

hh_income_df = hh_income_df[hh_income_df['Geography'].str.contains('(?:Stillwater)')]
household_df = hh_income_df.drop(['Household_Income_Min','Household_Income_Max'], axis=1).groupby(['Year']).sum()

year_list = []
median_class_list= []
median_list = []

for year in hh_income_df['Year'].unique():
    temp = hh_income_df[hh_income_df['Year']==year].sort_values('Household_Income_Min').reset_index(drop='index')
    print(f"Year {year}")
    median_class, median = median_class_finder(temp['Household Counts'], temp['Household Income Bucket'], temp['Household_Income_Max'], temp['Household_Income_Min'])
    year_list.append(year)
    median_class_list.append(median_class)
    median_list.append(median)

household_df = pd.DataFrame({'Median Household Income':median_list, 'Household Counts':household_df['Household Counts']}).reset_index()

#============================================
# Consolidating property_value_df
#============================================

property_value_df = property_value_df[property_value_df['Geography'].str.contains('(?:Stillwater)')]
property_df = property_value_df.drop(['Value_Min','Value_Max'], axis=1).groupby(['Year']).sum()

year_list = []
median_class_list= []
median_list = []

for year in property_value_df['Year'].unique():
    temp = property_value_df[property_value_df['Year']==year].sort_values('Value_Min').reset_index(drop='index')
    print(f"Year {year}")
    median_class, median = median_class_finder(temp['Property Counts'], temp['Value Bucket'], temp['Value_Max'], temp['Value_Min'])
    year_list.append(year)
    median_class_list.append(median_class)
    median_list.append(median)

property_df = pd.DataFrame({'Median Property Value':median_list, 'Property Counts':property_df['Property Counts']}).reset_index()


#============================================
# Consolidating rent_own_df
#============================================

rent_own_df = rent_own_df[rent_own_df['Geography'].str.contains('(?:Payne)')]
rent_own_df = rent_own_df.rename(columns={'share':'Household Ownership Share'})

#============================================
# Consolidating rent_df
#============================================

rent_df = rent_df[rent_df['Location'].str.contains('(?:Payne)')]

#============================================
# Merging all suitable df
#============================================

df = pd.merge(pop_age_df,household_df, on='Year')
df = pd.merge(df, property_df, on='Year')
df = pd.merge(df, enrollment_df, on='Year')
df = pd.merge(df, rent_own_df[['Year','Household Ownership','Household Ownership Share']], on='Year')
df = pd.merge(df, rent_df.drop('Location',axis=1), on = 'Year')
df = df.rename(columns={'Total':'Overall Median Rent'})

# export to consolidated folder
directory = "data\\consolidated"

if not os.path.exists(directory):
    os.makedirs(directory)

df.to_csv(f"{directory}\\final_rent.csv",index=False,header=True)
