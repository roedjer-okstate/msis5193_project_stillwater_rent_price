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

#============================================
# Connect to the webpage for Rent Price 2021
#============================================

driver = webdriver.Firefox(executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

rent2021_url = 'https://data.census.gov/cedsci/table?q=Renter%20Costs&g=0400000US40_0500000US40119&tid=ACSDT1Y2021.B25031'

driver.get(rent2021_url)

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2021_label_xp = "//span[@class='ag-group-value']"
census_rent_2021_label_elements = driver.find_elements('xpath',census_rent_2021_label_xp)

census_rent_2021_label = []
for i in range(1,len(census_rent_2021_label_elements)):
    census_rent_2021_label.append(census_rent_2021_label_elements[i].text)

#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2021_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2021_OK_elements = driver.find_elements('xpath',census_rent_2021_OK_xp)

census_rent_2021_OK = []
for i in census_rent_2021_OK_elements:
    census_rent_2021_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2021_OK)):
    for char in census_rent_2021_OK[i]:
        if char in punc:
            census_rent_2021_OK[i] = census_rent_2021_OK[i].replace(char, "")

census_rent_2021_OK = census_rent_2021_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2021_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2021_Payne_elements = driver.find_elements('xpath',census_rent_2021_Payne_xp)

census_rent_2021_Payne = []
for i in census_rent_2021_Payne_elements:
    census_rent_2021_Payne.append(i.text)
    
for i in range(len(census_rent_2021_Payne)):
    for char in census_rent_2021_Payne[i]:
        if char in punc:
            census_rent_2021_Payne[i] = census_rent_2021_Payne[i].replace(char, "")
            
census_rent_2021_Payne = census_rent_2021_Payne[1:]

census_rent_2021_dictionary = {
    'Number of Rooms': census_rent_2021_label,
    'Median Rent Price - Oklahoma': census_rent_2021_OK,
    'Median Rent Price - Payne County': census_rent_2021_Payne   
}

census_rent_2021_df = pd.DataFrame(census_rent_2021_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2020
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2020_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT5Y2020.B25031']"
rent2020 = driver.find_element('xpath',rent2020_xpath)
rent2020.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2020_label_xp = "//span[@class='ag-group-value']"
census_rent_2020_label_elements = driver.find_elements('xpath',census_rent_2020_label_xp)

census_rent_2020_label = []
for i in range(1,len(census_rent_2020_label_elements)):
    census_rent_2020_label.append(census_rent_2020_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2020_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2020_OK_elements = driver.find_elements('xpath',census_rent_2020_OK_xp)

census_rent_2020_OK = []
for i in census_rent_2020_OK_elements:
    census_rent_2020_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2020_OK)):
    for char in census_rent_2020_OK[i]:
        if char in punc:
            census_rent_2020_OK[i] = census_rent_2020_OK[i].replace(char, "")

census_rent_2020_OK = census_rent_2020_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2020_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2020_Payne_elements = driver.find_elements('xpath',census_rent_2020_Payne_xp)

census_rent_2020_Payne = []
for i in census_rent_2020_Payne_elements:
    census_rent_2020_Payne.append(i.text)
    
for i in range(len(census_rent_2020_Payne)):
    for char in census_rent_2020_Payne[i]:
        if char in punc:
            census_rent_2020_Payne[i] = census_rent_2020_Payne[i].replace(char, "")
            
census_rent_2020_Payne = census_rent_2020_Payne[1:]

census_rent_2020_dictionary = {
    'Number of Rooms': census_rent_2020_label,
    'Median Rent Price - Oklahoma': census_rent_2020_OK,
    'Median Rent Price - Payne County': census_rent_2020_Payne   
}

census_rent_2020_df = pd.DataFrame(census_rent_2020_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2019
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2019_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2019.B25031']"
rent2019 = driver.find_element('xpath',rent2019_xpath)
rent2019.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2019_label_xp = "//span[@class='ag-group-value']"
census_rent_2019_label_elements = driver.find_elements('xpath',census_rent_2019_label_xp)

census_rent_2019_label = []
for i in range(1,len(census_rent_2019_label_elements)):
    census_rent_2019_label.append(census_rent_2019_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2019_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2019_OK_elements = driver.find_elements('xpath',census_rent_2019_OK_xp)

census_rent_2019_OK = []
for i in census_rent_2019_OK_elements:
    census_rent_2019_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2019_OK)):
    for char in census_rent_2019_OK[i]:
        if char in punc:
            census_rent_2019_OK[i] = census_rent_2019_OK[i].replace(char, "")

census_rent_2019_OK = census_rent_2019_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2019_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2019_Payne_elements = driver.find_elements('xpath',census_rent_2019_Payne_xp)

census_rent_2019_Payne = []
for i in census_rent_2019_Payne_elements:
    census_rent_2019_Payne.append(i.text)
    
for i in range(len(census_rent_2019_Payne)):
    for char in census_rent_2019_Payne[i]:
        if char in punc:
            census_rent_2019_Payne[i] = census_rent_2019_Payne[i].replace(char, "")
            
census_rent_2019_Payne = census_rent_2019_Payne[1:]

census_rent_2019_dictionary = {
    'Number of Rooms': census_rent_2019_label,
    'Median Rent Price - Oklahoma': census_rent_2019_OK,
    'Median Rent Price - Payne County': census_rent_2019_Payne   
}

census_rent_2019_df = pd.DataFrame(census_rent_2019_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2018
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2018_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2018.B25031']"
rent2018 = driver.find_element('xpath',rent2018_xpath)
rent2018.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2018_label_xp = "//span[@class='ag-group-value']"
census_rent_2018_label_elements = driver.find_elements('xpath',census_rent_2018_label_xp)

census_rent_2018_label = []
for i in range(1,len(census_rent_2018_label_elements)):
    census_rent_2018_label.append(census_rent_2018_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2018_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2018_OK_elements = driver.find_elements('xpath',census_rent_2018_OK_xp)

census_rent_2018_OK = []
for i in census_rent_2018_OK_elements:
    census_rent_2018_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2018_OK)):
    for char in census_rent_2018_OK[i]:
        if char in punc:
            census_rent_2018_OK[i] = census_rent_2018_OK[i].replace(char, "")

census_rent_2018_OK = census_rent_2018_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2018_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2018_Payne_elements = driver.find_elements('xpath',census_rent_2018_Payne_xp)

census_rent_2018_Payne = []
for i in census_rent_2018_Payne_elements:
    census_rent_2018_Payne.append(i.text)
    
for i in range(len(census_rent_2018_Payne)):
    for char in census_rent_2018_Payne[i]:
        if char in punc:
            census_rent_2018_Payne[i] = census_rent_2018_Payne[i].replace(char, "")
            
census_rent_2018_Payne = census_rent_2018_Payne[1:]

census_rent_2018_dictionary = {
    'Number of Rooms': census_rent_2018_label,
    'Median Rent Price - Oklahoma': census_rent_2018_OK,
    'Median Rent Price - Payne County': census_rent_2018_Payne   
}

census_rent_2018_df = pd.DataFrame(census_rent_2018_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2017
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2017_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2017.B25031']"
rent2017 = driver.find_element('xpath',rent2017_xpath)
rent2017.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2017_label_xp = "//span[@class='ag-group-value']"
census_rent_2017_label_elements = driver.find_elements('xpath',census_rent_2017_label_xp)

census_rent_2017_label = []
for i in range(1,len(census_rent_2017_label_elements)):
    census_rent_2017_label.append(census_rent_2017_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2017_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2017_OK_elements = driver.find_elements('xpath',census_rent_2017_OK_xp)

census_rent_2017_OK = []
for i in census_rent_2017_OK_elements:
    census_rent_2017_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2017_OK)):
    for char in census_rent_2017_OK[i]:
        if char in punc:
            census_rent_2017_OK[i] = census_rent_2017_OK[i].replace(char, "")

census_rent_2017_OK = census_rent_2017_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2017_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2017_Payne_elements = driver.find_elements('xpath',census_rent_2017_Payne_xp)

census_rent_2017_Payne = []
for i in census_rent_2017_Payne_elements:
    census_rent_2017_Payne.append(i.text)
    
for i in range(len(census_rent_2017_Payne)):
    for char in census_rent_2017_Payne[i]:
        if char in punc:
            census_rent_2017_Payne[i] = census_rent_2017_Payne[i].replace(char, "")
            
census_rent_2017_Payne = census_rent_2017_Payne[1:]

census_rent_2017_dictionary = {
    'Number of Rooms': census_rent_2017_label,
    'Median Rent Price - Oklahoma': census_rent_2017_OK,
    'Median Rent Price - Payne County': census_rent_2017_Payne   
}

census_rent_2017_df = pd.DataFrame(census_rent_2017_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2016
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2016_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2016.B25031']"
rent2016 = driver.find_element('xpath',rent2016_xpath)
rent2016.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2016_label_xp = "//span[@class='ag-group-value']"
census_rent_2016_label_elements = driver.find_elements('xpath',census_rent_2016_label_xp)

census_rent_2016_label = []
for i in range(1,len(census_rent_2016_label_elements)):
    census_rent_2016_label.append(census_rent_2016_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2016_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2016_OK_elements = driver.find_elements('xpath',census_rent_2016_OK_xp)

census_rent_2016_OK = []
for i in census_rent_2016_OK_elements:
    census_rent_2016_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2016_OK)):
    for char in census_rent_2016_OK[i]:
        if char in punc:
            census_rent_2016_OK[i] = census_rent_2016_OK[i].replace(char, "")

census_rent_2016_OK = census_rent_2016_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2016_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2016_Payne_elements = driver.find_elements('xpath',census_rent_2016_Payne_xp)

census_rent_2016_Payne = []
for i in census_rent_2016_Payne_elements:
    census_rent_2016_Payne.append(i.text)
    
for i in range(len(census_rent_2016_Payne)):
    for char in census_rent_2016_Payne[i]:
        if char in punc:
            census_rent_2016_Payne[i] = census_rent_2016_Payne[i].replace(char, "")
            
census_rent_2016_Payne = census_rent_2016_Payne[1:]

census_rent_2016_dictionary = {
    'Number of Rooms': census_rent_2016_label,
    'Median Rent Price - Oklahoma': census_rent_2016_OK,
    'Median Rent Price - Payne County': census_rent_2016_Payne   
}

census_rent_2016_df = pd.DataFrame(census_rent_2016_dictionary)

#============================================
# Navigate to the webpage for Rent Price 2015
#============================================

dropdownlist_xpath = "//div[@class='aqua-flex nowrap']"
dropdownlist = driver.find_element('xpath',dropdownlist_xpath)
dropdownlist.click()

rent2015_xpath = "//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2015.B25031']"
rent2015 = driver.find_element('xpath',rent2015_xpath)
rent2015.click()

#======================================================
# Extracting Labels
#======================================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//span[@class='ag-group-value']"))
census_rent_2015_label_xp = "//span[@class='ag-group-value']"
census_rent_2015_label_elements = driver.find_elements('xpath',census_rent_2015_label_xp)

census_rent_2015_label = []
for i in range(1,len(census_rent_2015_label_elements)):
    census_rent_2015_label.append(census_rent_2015_label_elements[i].text)
    
#======================================================
# Extracting first column - Oklahoma Estimates
#======================================================
sleep(5)
census_rent_2015_OK_xp = "//div[@class='ag-center-cols-container']/div/div[1]"
census_rent_2015_OK_elements = driver.find_elements('xpath',census_rent_2015_OK_xp)

census_rent_2015_OK = []
for i in census_rent_2015_OK_elements:
    census_rent_2015_OK.append(i.text)
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for i in range(len(census_rent_2015_OK)):
    for char in census_rent_2015_OK[i]:
        if char in punc:
            census_rent_2015_OK[i] = census_rent_2015_OK[i].replace(char, "")

census_rent_2015_OK = census_rent_2015_OK[1:]

#======================================================
# Extracting second column - Payne County Estimates
#======================================================

sleep(5)
census_rent_2015_Payne_xp = "//div[@class='ag-center-cols-container']/div/div[3]"
census_rent_2015_Payne_elements = driver.find_elements('xpath',census_rent_2015_Payne_xp)

census_rent_2015_Payne = []
for i in census_rent_2015_Payne_elements:
    census_rent_2015_Payne.append(i.text)
    
for i in range(len(census_rent_2015_Payne)):
    for char in census_rent_2015_Payne[i]:
        if char in punc:
            census_rent_2015_Payne[i] = census_rent_2015_Payne[i].replace(char, "")
            
census_rent_2015_Payne = census_rent_2015_Payne[1:]

census_rent_2015_dictionary = {
    'Number of Rooms': census_rent_2015_label,
    'Median Rent Price - Oklahoma': census_rent_2015_OK,
    'Median Rent Price - Payne County': census_rent_2015_Payne   
}

census_rent_2015_df = pd.DataFrame(census_rent_2015_dictionary)

# Quit driver

driver.quit()

#============================================
# Converting to all character to numeric
#============================================
census_rent_2021_df['Median Rent Price - Oklahoma'] = census_rent_2021_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2021_df['Median Rent Price - Payne County'] = census_rent_2021_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2020_df['Median Rent Price - Oklahoma'] = census_rent_2020_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2020_df['Median Rent Price - Payne County'] = census_rent_2020_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2019_df['Median Rent Price - Oklahoma'] = census_rent_2019_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2019_df['Median Rent Price - Payne County'] = census_rent_2019_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2018_df['Median Rent Price - Oklahoma'] = census_rent_2018_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2018_df['Median Rent Price - Payne County'] = census_rent_2018_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2017_df['Median Rent Price - Oklahoma'] = census_rent_2017_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2017_df['Median Rent Price - Payne County'] = census_rent_2017_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2016_df['Median Rent Price - Oklahoma'] = census_rent_2016_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2016_df['Median Rent Price - Payne County'] = census_rent_2016_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2016_df['Median Rent Price - Oklahoma'] = census_rent_2020_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2016_df['Median Rent Price - Payne County'] = census_rent_2020_df['Median Rent Price - Payne County'].astype(int, errors='ignore')

census_rent_2015_df['Median Rent Price - Oklahoma'] = census_rent_2015_df['Median Rent Price - Oklahoma'].astype(int, errors='ignore')
census_rent_2015_df['Median Rent Price - Payne County'] = census_rent_2015_df['Median Rent Price - Payne County'].astype(int, errors='ignore')


#============================================
# Transposing all census rent df
#============================================

census_rent_2021_df = census_rent_2021_df.set_index('Number of Rooms').transpose()
census_rent_2021_df['Year'] = 2021

census_rent_2020_df = census_rent_2020_df.set_index('Number of Rooms').transpose()
census_rent_2020_df['Year'] = 2020

census_rent_2019_df = census_rent_2019_df.set_index('Number of Rooms').transpose()
census_rent_2019_df['Year'] = 2019

census_rent_2018_df = census_rent_2018_df.set_index('Number of Rooms').transpose()
census_rent_2018_df['Year'] = 2018

census_rent_2017_df = census_rent_2017_df.set_index('Number of Rooms').transpose()
census_rent_2017_df['Year'] = 2017

census_rent_2016_df = census_rent_2016_df.set_index('Number of Rooms').transpose()
census_rent_2016_df['Year'] = 2016

census_rent_2015_df = census_rent_2015_df.set_index('Number of Rooms').transpose()
census_rent_2015_df['Year'] = 2015

overall_census_rent_df = pd.concat([census_rent_2015_df,census_rent_2016_df,census_rent_2017_df,census_rent_2018_df,
                                    census_rent_2019_df,census_rent_2020_df,census_rent_2021_df])

overall_census_rent_df.reset_index(inplace=True)

overall_census_rent_df = overall_census_rent_df.rename_axis(None, axis=1)

overall_census_rent_df.columns=['Location', 'Total','No bedroom','1 bedroom','2 bedrooms', '3 bedrooms', '4 bedrooms', '5 or more bedrooms','Year']

os.chdir(r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau')
if not os.path.exists('data\raw\\census_rent'):
    os.makedirs('data\\raw\\census_rent')

census_rent_2015_df.to_csv('data\\raw\\census_rent\\census_rent_2015.csv', header=True, index=False)
census_rent_2016_df.to_csv('data\\raw\\census_rent\\census_rent_2016.csv', header=True, index=False)
census_rent_2017_df.to_csv('data\\raw\\census_rent\\census_rent_2017.csv', header=True, index=False)
census_rent_2018_df.to_csv('data\\raw\\census_rent\\census_rent_2018.csv', header=True, index=False)
census_rent_2019_df.to_csv('data\\raw\\census_rent\\census_rent_2019.csv', header=True, index=False)
census_rent_2020_df.to_csv('data\\raw\\census_rent\\census_rent_2020.csv', header=True, index=False)
census_rent_2021_df.to_csv('data\\raw\\census_rent\\census_rent_2021.csv', header=True, index=False)



# Checking dataframe information with .info()
overall_census_rent_df.info()

# converting empty string to null
for cols in overall_census_rent_df.columns:
    for rows in range(len(overall_census_rent_df[cols])):
        if overall_census_rent_df.loc[rows,cols]==None:
            overall_census_rent_df.loc[rows,cols]=np.nan

# converting every numeric columns from str to numeric
overall_census_rent_df[['Total','No bedroom','1 bedroom','2 bedrooms','3 bedrooms','4 bedrooms','5 or more bedrooms']] = overall_census_rent_df[['Total','No bedroom','1 bedroom','2 bedrooms','3 bedrooms','4 bedrooms','5 or more bedrooms']].apply(pd.to_numeric).astype('Float64')

# check if there is any null value
overall_census_rent_df.isnull().sum()

# check skewness
overall_census_rent_df['No bedroom'].skew(axis = 0, skipna = True)

# check skewness
overall_census_rent_df['5 or more bedrooms'].skew(axis = 0, skipna = True)

# Since both columns with null have normal skewed distribution (skewness between -2 and 2)
# impute null values with colums mean
overall_census_rent_df['No bedroom'] = overall_census_rent_df['No bedroom'].fillna(overall_census_rent_df['No bedroom'].mean())
overall_census_rent_df['5 or more bedrooms'] = overall_census_rent_df['5 or more bedrooms'].fillna(overall_census_rent_df['5 or more bedrooms'].mean())

# export to transformed folder
directory = "data\\transformed\\census_rent"

if not os.path.exists(directory):
    os.makedirs(directory)

overall_census_rent_df.to_csv(f"{directory}\\overall_census_rent.csv",index=False,header=True)