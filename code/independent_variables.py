#############################################
#=============Read in Libraries=============#
# Read in the necessary libraries.          #
#############################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from getpass import getpass
from time import sleep
import pandas as pd
import regex as re
import zipfile
import os

os.chdir(r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau')

#============================================
# Connect to the webpage for household income data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\datausa_hh_income'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

hh_income_url = 'https://datausa.io/profile/geo/stillwater-ok#household_income'

driver.get(hh_income_url)

#============================================
# Navigate to the household income data
#============================================
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic household_income TextViz ']//span[@class='option-label']"))
hh_income_xpath = "//div[@class='topic household_income TextViz ']//span[@class='option-label']"
hh_income = driver.find_element('xpath',hh_income_xpath)
hh_income.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
hh_income_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
hh_income_data = driver.find_element('xpath',hh_income_data_xpath)
hh_income_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\datausa_hh_income\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\datausa_hh_income")
    
driver.quit()

#============================================
# Connect to the webpage for property value data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\property_value'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

property_value_url = 'https://datausa.io/profile/geo/stillwater-ok#property_value'

driver.get(property_value_url)

#============================================
# Navigate to the property value data
#============================================

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',r"/html/body/div[1]/div/div/div/div[1]/div[8]/div[2]/div[1]/div[2]/div[1]/span[1]/span/div/span"))
property_value_xpath = r"/html/body/div[1]/div/div/div/div[1]/div[8]/div[2]/div[1]/div[2]/div[1]/span[1]/span/div/span"
property_value = driver.find_element('xpath',property_value_xpath)
action = webdriver.ActionChains(driver)
action.move_to_element(property_value).click().perform()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
property_value_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
property_value_data = driver.find_element('xpath',property_value_data_xpath)
property_value_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\property_value\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\property_value")
    
driver.quit()

#============================================
# Connect to the webpage for rent vs own data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\rent_own'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

rent_own_url = 'https://datausa.io/profile/geo/stillwater-ok#rent_own'

driver.get(rent_own_url)

#============================================
# Navigate to the rent vs own data
#============================================

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic rent_own TextViz ']//span[@class='option-label']"))
rent_own_xpath = "//div[@class='topic rent_own TextViz ']//span[@class='option-label']"
rent_own = driver.find_element('xpath',rent_own_xpath)
rent_own.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
rent_own_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
rent_own_data = driver.find_element('xpath',rent_own_data_xpath)
rent_own_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\rent_own\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\rent_own")
    
driver.quit()

#============================================
# Connect to the webpage for domestic trade growth data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\trade_growth'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

trade_growth_url = 'https://datausa.io/profile/geo/stillwater-ok#trade_growth'

driver.get(trade_growth_url)

#============================================
# Navigate to the domestic trade growth data
#============================================

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic trade_growth TextViz ']//span[@class='option-label']"))
trade_growth_xpath = "//div[@class='topic trade_growth TextViz ']//span[@class='option-label']"
trade_growth = driver.find_element('xpath',trade_growth_xpath)
trade_growth.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
trade_growth_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
trade_growth_data = driver.find_element('xpath',trade_growth_data_xpath)
trade_growth_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\trade_growth\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\trade_growth")
    
driver.quit()

#============================================
# Connect to the webpage for industry data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\emp_industry'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

industry_url = 'https://datausa.io/profile/geo/stillwater-ok#tmap_ind_num_emp'

driver.get(industry_url)

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic tmap_ind_num_emp TextViz ']//span[@class='option-label']"))
industry_xpath = "//div[@class='topic tmap_ind_num_emp TextViz ']//span[@class='option-label']"
industry = driver.find_element('xpath',industry_xpath)
industry.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
industry_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
industry_data = driver.find_element('xpath',industry_data_xpath)
industry_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\emp_industry\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\emp_industry")
    
driver.quit()

#============================================
# Connect to the webpage for age data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\age_nativity'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

age_nativity_url = 'https://datausa.io/profile/geo/stillwater-ok#age_nativity'

driver.get(age_nativity_url)

#============================================
# Navigate to the age data
#============================================

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic age_nativity TextViz ']//span[@class='option-label']"))
age_nativity_xpath = "//div[@class='topic age_nativity TextViz ']//span[@class='option-label']"
age_nativity = driver.find_element('xpath',age_nativity_xpath)
age_nativity.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
age_nativity_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
age_nativity_data = driver.find_element('xpath',age_nativity_data_xpath)
age_nativity_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\age_nativity\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\age_nativity")
    
driver.quit()

#============================================
# Connect to the webpage for enrollment data and setup download directory
#============================================

download_directory = r'C:\Users\roedj\Documents\GitHub\homework_MSIS5193\project-deliverable-1-orange-intelligence-bureau\data\raw\enrollment_status'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(profile,executable_path=r'C:\Users\roedj\Documents\geckodriver.exe')

enrollment_status_url = 'https://datausa.io/profile/university/oklahoma-state-university-main-campus#enrollment_status'

driver.get(enrollment_status_url)

#============================================
# Navigate to the enrollment data
#============================================

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//div[@class='topic enrollment_status TextViz ']//span[@class='option-label']"))
enrollment_status_xpath = "//div[@class='topic enrollment_status TextViz ']//span[@class='option-label']"
enrollment_status = driver.find_element('xpath',enrollment_status_xpath)
enrollment_status.click()

WebDriverWait(driver, timeout=10).until(lambda d: d.find_element('xpath',"//button[@class='bp3-button bp3-icon-download bp3-minimal']"))
enrollment_status_data_xpath = "//button[@class='bp3-button bp3-icon-download bp3-minimal']"
enrollment_status_data = driver.find_element('xpath',enrollment_status_data_xpath)
enrollment_status_data.click()

sleep(5)

with zipfile.ZipFile(f"data\\raw\\enrollment_status\\{os.listdir(download_directory)[0]}", 'r') as zip_ref:
    zip_ref.extractall("data\\raw\\enrollment_status")
    
driver.quit()