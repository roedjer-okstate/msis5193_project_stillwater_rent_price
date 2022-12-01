#############################################
#=============Read in Libraries=============#
# Read in the necessary libraries.          #
#############################################

import numpy as np
import pandas as pd
import regex as re
import os

os.chdir(r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau')

#============================================
# Data Cleaning, Transformation, and reduction for Age data
#============================================

age_df = pd.read_csv("data\\raw\\age_nativity\\Age by Nativity.csv")

# Checking dataframe information with .info()
age_df.info()

# drop with there is any duplicated rows
age_df = age_df.drop_duplicates()

# removing columns with only 1 unique value
print("|-----------Columns----------|-nunique-|\n|----------------------------+---------|")
for cols in age_df.columns:
    print(f"|{cols:^28}| {age_df[cols].nunique():>8}|")
    
for cols in age_df.columns:
    if age_df[cols].nunique() <= 1:
        age_df.drop(cols, axis=1,inplace=True)

# We are interested only in population according to age across year
# dropping unnecessary columns
age_df=age_df.drop(['Place of Birth','ID Age','ID Year','Birthplace Moe','nativity','share'], axis=1)

# renaming columns
age_df=age_df.rename(columns = {'Birthplace':'Population'})

# changing dataframe structure
age_df=age_df.groupby(['Year','Age'],as_index=False).sum()

# converting age to 2 columns
Age_Min = []
Age_Max = []
for interval in age_df['Age']:
    if interval == 'Under 5 Years':
        Age_Min.append(0)
        Age_Max.append(4)
    elif interval == '75 Years & Over':
        Age_Min.append(75)
        Age_Max.append(np.inf)
    else:
        pattern = r'([0-9]+) (.*)+ ([0-9]+) Years'
        Age_Min.append(int(re.findall(pattern, interval)[0][0]))
        Age_Max.append(int(re.findall(pattern, interval)[0][2]))

age_df['Age_Min'] = Age_Min
age_df['Age_Max'] = Age_Max

# sorting columns
age_df = age_df[['Year', 'Age', 'Age_Min', 'Age_Max', 'Population']]

# check if there is any null value
age_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\age_population"

if not os.path.exists(directory):
    os.makedirs(directory)

age_df.to_csv(f"{directory}\\stillwater_age_population.csv",index=False,header=True)


#============================================
# Data Cleaning, Transformation, and reduction for Age data
#============================================
hh_income_df = pd.read_csv("data\\raw\\datausa_hh_income\\Household Income.csv")

# Checking dataframe information with .info()
hh_income_df.info()

# drop with there is any duplicated rows
hh_income_df = hh_income_df.drop_duplicates()

# removing columns with only 1 unique value
print("|-----------Columns----------|-nunique-|\n|----------------------------+---------|")
for cols in hh_income_df.columns:
    print(f"|{cols:^28}| {hh_income_df[cols].nunique():>8}|")
    
for cols in hh_income_df.columns:
    if hh_income_df[cols].nunique() <= 1:
        hh_income_df.drop(cols, axis=1,inplace=True)

# We are interested only in household according to income bucket across year
# dropping unnecessary columns
hh_income_df=hh_income_df.drop(['ID Household Income Bucket','ID Year','Household Income Moe','ID Geography','Slug Geography','share'], axis=1)

# renaming columns
hh_income_df=hh_income_df.rename(columns = {'Houshold Income':'Households'})

# changing dataframe structure
hh_income_df.groupby(['Year','Geography','Household Income Bucket'],as_index=False).sum()

# converting bucket to 2 columns
Household_Income_Min = []
Household_Income_Max = []
for interval in hh_income_df['Household Income Bucket']:
    if interval == '< $10,000':
        Household_Income_Min.append(0)
        Household_Income_Max.append(9999)
    elif interval == '$200,000+':
        Household_Income_Min.append(200000)
        Household_Income_Max.append(np.inf)
    else:
        pattern = r'\$([0-9]+,[0-9]+)-\$([0-9]+,[0-9]+)'
        Household_Income_Min.append(int(re.findall(pattern, interval)[0][0].replace(',','')))
        Household_Income_Max.append(int(re.findall(pattern, interval)[0][1].replace(',','')))

hh_income_df['Household_Income_Min'] = Household_Income_Min
hh_income_df['Household_Income_Max'] = Household_Income_Max

# renaming column
hh_income_df=hh_income_df.rename(columns = {'Household Income':'Household Counts'})

# sorting columns
hh_income_df = hh_income_df[['Year', 'Household Income Bucket', 'Household_Income_Min', 'Household_Income_Max', 'Geography','Household Counts']]

# check if there is any null value
hh_income_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\household_income"

if not os.path.exists(directory):
    os.makedirs(directory)

hh_income_df.to_csv(f"{directory}\\household_income.csv",index=False,header=True)


#============================================
# Data Cleaning, Transformation, and reduction for employment by industry data
#============================================
emp_industry_df = pd.read_csv("data\\raw\\emp_industry\\Employment by Industries.csv")

# Checking dataframe information with .info()
emp_industry_df.info()

# drop with there is any duplicated rows
emp_industry_df = emp_industry_df.drop_duplicates()

# removing columns with only 1 unique value
print("|----------------Columns---------------|-nunique-|\n|--------------------------------------+---------|")
for cols in emp_industry_df.columns:
    print(f"|{cols:^38}| {emp_industry_df[cols].nunique():>8}|")
    
for cols in emp_industry_df.columns:
    if emp_industry_df[cols].nunique() <= 1:
        emp_industry_df.drop(cols, axis=1,inplace=True)

# We are interested only in household according to income bucket across year
# dropping unnecessary columns
emp_industry_df=emp_industry_df.drop(['ID Group', 'Group', 'ID Industry', 'ID Year','Workforce by Industry and Gender Moe'], axis=1)

# renaming columns
emp_industry_df=emp_industry_df.rename(columns = {'Workforce by Industry and Gender':'Workforce'})

# check if there is any null value
emp_industry_df.isnull().sum()

# sorting columns
emp_industry_df = emp_industry_df[['Year', 'Industry', 'Workforce']] 

# export to transformed folder
directory = "data\\transformed\\emp_industry"

if not os.path.exists(directory):
    os.makedirs(directory)

emp_industry_df.to_csv(f"{directory}\\emp_industry.csv",index=False,header=True)


#============================================
# Data Cleaning, Transformation, and reduction for okstate enrollment industry data
#============================================
enrollment_df = pd.read_csv("data\\raw\\enrollment_status\\Full-Time vs Part-Time Enrollment.csv")

# Checking dataframe information with .info()
enrollment_df.info()

# drop with there is any duplicated rows
enrollment_df = enrollment_df.drop_duplicates()

# removing columns with only 1 unique value
print("|----------------Columns---------------|-nunique-|\n|--------------------------------------+---------|")
for cols in enrollment_df.columns:
    print(f"|{cols:^38}| {enrollment_df[cols].nunique():>8}|")
for cols in emp_industry_df.columns:
    if emp_industry_df[cols].nunique() <= 1:
        emp_industry_df.drop(cols, axis=1,inplace=True)

# We are interested only in enrollment according to university across year
# dropping unnecessary columns
enrollment_df=enrollment_df.drop(['ID Enrollment Status', 'ID Year', 'ID University','Slug University','share'], axis=1)

# We are interested only in enrollment of Oklahoma State University
enrollment_df = enrollment_df[enrollment_df['University'].str.contains('(?:Oklahoma State)')]

# changing dataframe structure
enrollment_df = enrollment_df.groupby(['Year','University'],as_index=False).sum()

# check if there is any null value
enrollment_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\enrollment"

if not os.path.exists(directory):
    os.makedirs(directory)

enrollment_df.to_csv(f"{directory}\\enrollment.csv",index=False,header=True)



#============================================
# Data Cleaning, Transformation, and reduction for property value data
#============================================
property_value_df = pd.read_csv("data\\raw\\property_value\\Property Value.csv")

# Checking dataframe information with .info()
property_value_df.info()

# drop with there is any duplicated rows
property_value_df = property_value_df.drop_duplicates()

# removing columns with only 1 unique value
print("|----------------Columns---------------|-nunique-|\n|--------------------------------------+---------|")
for cols in property_value_df.columns:
    print(f"|{cols:^38}| {property_value_df[cols].nunique():>8}|")
for cols in property_value_df.columns:
    if property_value_df[cols].nunique() <= 1:
        property_value_df.drop(cols, axis=1,inplace=True)

# We are interested only in property value according to bucket across year
# dropping unnecessary columns
property_value_df=property_value_df.drop(['ID Value Bucket', 'ID Year', 'Property Value by Bucket Moe', 'ID Geography', 'Slug Geography', 'share'], axis=1)

# converting bucket to 2 columns
Value_Min = []
Value_Max = []
for interval in property_value_df['Value Bucket']:
    if interval == 'Less Than $10,000':
        Value_Min.append(0)
        Value_Max.append(9999)
    elif interval == '$2,000,000 or More':
        Value_Min.append(2000000)
        Value_Max.append(np.inf)
    else:
        pattern = r'\$([0-9]*,?[0-9]+,[0-9]+) to \$([0-9]*,?[0-9]+,[0-9]+)'
        Value_Min.append(int(re.findall(pattern, interval)[0][0].replace(',','')))
        Value_Max.append(int(re.findall(pattern, interval)[0][1].replace(',','')))

pattern = r'\$([0-9]*,?[0-9]+,[0-9]+) to \$([0-9]*,?[0-9]+,[0-9]+)'
re.findall(pattern, property_value_df.loc[1,'Value Bucket'])[0][1]

property_value_df['Value_Min'] = Value_Min
property_value_df['Value_Max'] = Value_Max

# renaming column
property_value_df=property_value_df.rename(columns = {'Property Value by Bucket':'Property Counts'})

# sort the columns
property_value_df=property_value_df[['Year', 'Value Bucket', 'Value_Min', 'Value_Max', 'Geography', 'Property Counts']]

# check if there is any null value
property_value_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\property_value"

if not os.path.exists(directory):
    os.makedirs(directory)

property_value_df.to_csv(f"{directory}\\property_value.csv",index=False,header=True)



#============================================
# Data Cleaning, Transformation, and reduction for rent_own data
#============================================
rent_own_df = pd.read_csv("data\\raw\\rent_own\\Rent vs Own.csv")

# Checking dataframe information with .info()
rent_own_df.info()

# drop with there is any duplicated rows
rent_own_df = rent_own_df.drop_duplicates()

# removing columns with only 1 unique value
print("|----------------Columns---------------|-nunique-|\n|--------------------------------------+---------|")
for cols in rent_own_df.columns:
    print(f"|{cols:^38}| {rent_own_df[cols].nunique():>8}|")
for cols in rent_own_df.columns:
    if rent_own_df[cols].nunique() <= 1:
        rent_own_df.drop(cols, axis=1,inplace=True)

# We are interested only in household ownership according to bucket across year
# dropping unnecessary columns
rent_own_df=rent_own_df.drop(['ID Year', 'Household Ownership Moe', 'ID Geography', 'Slug Geography'], axis=1)

# check if there is any null value
rent_own_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\rent_own"

if not os.path.exists(directory):
    os.makedirs(directory)

rent_own_df.to_csv(f"{directory}\\rent_own.csv",index=False,header=True)



#============================================
# Data Cleaning, Transformation, and domestic trade growth for rent_own data
#============================================
trade_growth_df = pd.read_csv("data\\raw\\trade_growth\\Domestic Trade Growth.csv")

# Checking dataframe information with .info()
trade_growth_df.info()

# drop with there is any duplicated rows
trade_growth_df = trade_growth_df.drop_duplicates()

# removing columns with only 1 unique value
print("|----------------Columns---------------|-nunique-|\n|--------------------------------------+---------|")
for cols in trade_growth_df.columns:
    print(f"|{cols:^38}| {trade_growth_df[cols].nunique():>8}|")
for cols in trade_growth_df.columns:
    if trade_growth_df[cols].nunique() <= 1:
        trade_growth_df.drop(cols, axis=1,inplace=True)

# We are interested only in trade amount across year
# dropping unnecessary columns
trade_growth_df=trade_growth_df.drop(['ID Year', 'ID Origin'], axis=1)

# check if there is any null value
trade_growth_df.isnull().sum()

# export to transformed folder
directory = "data\\transformed\\trade_growth"

if not os.path.exists(directory):
    os.makedirs(directory)

trade_growth_df.to_csv(f"{directory}\\trade_growth.csv",index=False,header=True)