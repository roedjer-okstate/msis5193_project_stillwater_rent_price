# Project Title - Rental Trend for City of Stillwater
*From Orange Intelligence Bureau*
*`Divya Pamu`, `Isabella Lieberman`, `Omkar Patade`, `Roe Djer Tan`*<br><br>

## Executive Summary

Since coronavirus pandemic has happened all over the globe with numerous lockdowns being enforced, the global economy and property market have been seriously affected as human activities have changed drastically, for example, remote learning and work from home have been a norm. The United States including Oklahoma is also one of the heavily stricken regions. Consequently, as students from Oklahoma State University, a few concerns come to our attention: 
- Has rental rate in Oklahoma especially Stillwater (Payne County) changed?
- Has the demographics of Stillwater changed?

Our main idea is to show trend on rent prices as well demographics variable (without biasing races) in Stillwater, Payne County, Oklahoma. Having access to a rent price trend can help realtors and investors as well as incoming college students and adults in decision making for investment or residing in Stillwater in near future as duration for it to remain affordable could be forecasted.<br>

### Business opportunity
1. Charles (2022) states that several rent and utilities financial aids have been offered to mitigate economic impact caused by the pandemic. Since economy is in a recovery phase, prediction for Stillwater rent prices is crucial to provide interested parties insights for a better financial and risk management. 
2. “Stillwater ranked No. 9 and Norman landed at No. 11 for most affordable rents in a survey of cities large and small by Rent.com” (Mize, 2022). Having access to a rent price trend can help realtors and investors as well as incoming college students and adults in decision making for investment or residing in Stillwater in near future as duration for it to remain affordable could be forecasted.<br><br>



## Statement of Scope
### Project Objectives
- To provide trend of rent prices (in US Dollars) in Stillwater
- To show changes in Stillwater demographics (without biasing races) including population age, household counts and income, university enrollment, property counts and values, and household ownerships.
- To show relationship between trend of rent prices and demographic variables in Stillwater.

### Unit of Analysis
Rent price is the unit of analysis.<br><br>

## Project Schedule
The team estimates that a timeframe of 12-14 weeks to extract, transform, and load data as well as visualize data with insights finding. The schedule is as shown below: <br>

![gantt_chart](assets/miscellaneous/gantt_chart.png)<br><br>

## Data Preparation
Our data preparation overview can be categorized into 3 parts: Extract, Transform, and Load.
### Extract
Raw data (external sources) will be extracted from websites through Python Selenium. 
### Transform
Raw data requires data processing or cleaning before it can be applied for intended use. Data transformation includes, but not limited to, columns and rows selection(e.g., keep only observations related to Stillwater/Payne County), keys (`Year` as primary key in this case) generation to facilitate joining processes,deriving new columns by calculations, removing null or duplicated values, data aggregations and summarizations, sorting and ordering, column splitting, and data transposing.
### Load
The cleaned data will be loaded into a GitHub repository that is accessible to every member in the team to facilitate version control and visualization process. The benefits of using GitHub repository: it ensures that everyone has the latest cleaned data from the same source (data quality and consistency) as data cleaning may be a recurring process, every update history is recorded, it is well-organized, and it facilitates future analytics processes.<br>

### Sources for our data
1. [datauso.io (Stillwater, Ok)](https://datausa.io/profile/geo/stillwater-ok)<br>
- Stillwater/Payne County – housing and property values over time, homeownership, age distribution, household income, employment by industry, domestic trade data<br>
Raw tables:
[property_value](data/raw/property_value), [Rent vs Own](data/raw/rent_own/Rent%20vs%20Own.csv), [Age by Nativity](data/raw/age_nativity/Age%20by%20Nativity.csv), [Household Income](data/raw/datausa_hh_income/Household%20Income.csv), [Employment by Industries](data/raw/emp_industry/Employment%20by%20Industries.csv), [Domestic Trade Growth](data/raw/trade_growth/Domestic%20Trade%20Growth.csv).

2. [Rent Price in Payne County from Census Bureau](https://data.census.gov/cedsci/table?q=Renter%20Costs&g=0400000US40_0500000US40119&tid=ACSDT1Y2021.B25031)<br>
- Census data for median rent prices in Oklahoma as well as Payne County over the years.<br>
Raw tables: *`census_rent_2015` to `census_rent_2021`* from [census_rent](data/raw/census_rent) folder.

3. [datauso.io (Oklahoma State University)](https://datausa.io/profile/university/oklahoma-state-university-main-campus)<br>
- Oklahoma State University's data that has values for number of students enrolled over a Year over Year (YoY) basis.<br>
Raw table: [Full-Time vs Part-Time Enrollment](data/raw/enrollment_status/Full-Time%20vs%20Part-Time%20Enrollment.csv)<br><br>

### Files and Folder Directory
* `/assets`: Contans image files, pdf, and other non-programming files.<br>
* `/code`: Python script files are stored here.<br>

| Coding File | Description |
| :--- |:---|
| [rent_price.py](code/rent_price.py) | Scraping and transformation of rent data (response variable).  |
| [independent_variables.py](code/independent_variables.py) | Scraping of all predictor data. |
| [IV_transformation.py](code/IV_transformation.py) | Transformation of all predictor data. |
| [data_consolidation.py](code/data_consolidation.py) | Consolidation of all potential data into [final_rent.csv](data/consolidated/final_rent.csv). |<br>

* `/data`: Contains Datasets.

| Folder | Description |
| :--- |:---|
| [raw](data/raw) | Storing scraped raw dataset csv files. |
| [transformed](data/transformed) | Storing cleaned, transformed, and reduced dataset csv files. |
| [consolidated](data/consolidated) | Storing consolidated dataset csv file. |
<br>


## Data Access

### Rent prices
- Website: [Rent Price in Payne County from Census Bureau](https://data.census.gov/cedsci/table?q=Renter%20Costs&g=0400000US40_0500000US40119&tid=ACSDT1Y2021.B25031)<br>
- Brief Description: Census data for median rent prices in Oklahoma as well as Payne County over the years.<br>
- Code: [rent_price.py](code/rent_price.py)
- Raw Tables: *`census_rent_2015` to `census_rent_2021`* from [census_rent](data/raw/census_rent) folder.<br>

Steps:<br>
1. `webdriver.Firefox` from Selenium is used to navigate to the website mentioned. The interface of the website is as shown:<br>
![rent_01](assets/data_access/rent_01.png)<br>

This website shows the median rent by bedrooms in Oklahoma and Payne County in 2021. We are interested in the data on the right. There are 3 columns we are interested in: `Label`, `Oklahoma Estimates`, and `Payne County Estimates`.

2. After using browser developer mode, XPath for `Label` column is located - `//span[@class='ag-group-value']`. Then, we apply `find_elements` to extract all elements in `Label` column. Then, `for` loop is used to assign each of the element into a list to facilitate dataframe forming process.

3. The same process in step 2 is applied to other interested columns with different XPath as shown below:<br>
- Oklahoma Estimates: `//div[@class='ag-center-cols-container']/div/div[1]`
- Payne County Estimates: `//div[@class='ag-center-cols-container']/div/div[3]`

4. We are done scraping rent information for 2021. For 2020 rent information, we locate the XPath for the dropdown list (dropdown list is located above the table with text of `2021: ACS 1-Year Estimates Detailed Tables` in the website interface) which is `//div[@class='aqua-flex nowrap']` and Selenium's `click` is applied to click on the dropdown list. The dropdown list is as shown:<br>
![rent_02](assets/data_access/rent_02.png)

5. Then, we locate the XPath for 2020 rent information with text of `2020: ACS 5-Year Estimates Detailed Tables` which is `//div[@class='aqua-menu-item px-3 py-2']//span[@class='data-opt-ACSDT1Y2019.B25031']` and Selenium's `click` is applied to navigate into the website containing 2020 rent information.

6. The same processes in step 2 and 3 are applied to scrape 2020 rent information. After scraping, the same processes in step 4 and 5 are applied to navigate to the next webpage containing 2019 rent information. We iterated and scraped rent information from year 2020 to 2015 with the same processes above.

7. After preliminary data transformation (for more details please refer to data transformation section) to ease dataframe forming, we exported the file to [census_rent](data/raw/census_rent) as csv and define it as raw file.

*Note that only 2020 rent information is 5-year estimates while the other years are 1-year estimates. It happens due to inavailability of the census data that may be resulted from coronavirus outbreak*<br><br>

### Other variables from datausa.io
- Website: [datauso.io (Stillwater, Ok)](https://datausa.io/profile/geo/stillwater-ok)<br>
- Detailed Website (click to navigate):
    - [Household Income Webpage](https://datausa.io/profile/geo/stillwater-ok#household_income)
    - [Property Value Webpage](https://datausa.io/profile/geo/stillwater-ok#property_value)
    - [Rent vs Own Webpage](https://datausa.io/profile/geo/stillwater-ok#rent_own)
    - [Domestic Trade Growth Webpage](https://datausa.io/profile/geo/stillwater-ok#trade_growth)
    - [Employment by Industry Webpage](https://datausa.io/profile/geo/stillwater-ok#tmap_ind_num_emp)
    - [Age By Nativity Webpage](https://datausa.io/profile/geo/stillwater-ok#age_nativity)
    - [Enrollment Data Webpage](https://datausa.io/profile/university/oklahoma-state-university-main-campus#enrollment_status)

- Brief Description: Stillwater/Payne County – housing and property values over time, homeownership, age distribution, household income, employment by industry, domestic trade data<br>
- Code: [independent_variables.py](code/independent_variables.py)
- Raw Tables: [property_value](data/raw/property_value), [Rent vs Own](data/raw/rent_own/Rent%20vs%20Own.csv), [Age by Nativity](data/raw/age_nativity/Age%20by%20Nativity.csv), [Household Income](data/raw/datausa_hh_income/Household%20Income.csv), [Employment by Industries](data/raw/emp_industry/Employment%20by%20Industries.csv), [Domestic Trade Growth](data/raw/trade_growth/Domestic%20Trade%20Growth.csv), [Full-Time vs Part-Time Enrollment](data/raw/enrollment_status/Full-Time%20vs%20Part-Time%20Enrollment.csv).<br>

Steps:<br>
1. We change `webdriver.Firefox` download directory to allow to downloaded csv file be directed into our preferred destination. 

2. `webdriver.Firefox` from Selenium is used to navigate to the website containing data for `household income`. The interface of the website is as shown:<br>
![IV_01](assets/data_access/IV_01.png)<br>

3. We locate the XPath for clickable `View Data` which is `//div[@class='topic household_income TextViz ']//span[@class='option-label']` and Selenium's `click` is applied. The interface is as shown: <br>
![IV_02](assets/data_access/IV_02.png)<br>

4. Then, we locate the XPath for clickable `Download as CSV` which is `//button[@class='bp3-button bp3-icon-download bp3-minimal` and Selenium's `click` is applied. Then, the zip file will be downloaded to set directory.

5. `extractall` from `zipfile` is applied to extract and obtain the csv file for `Household income` containing the data we are interested.

6. The same processes from step 1 to 5 are spplied to rest of the data from datausa.io.

*Note that we applied `Download as CSV` instead of directly scrape the table using XPath to locate the elements. This is because whenever we try to scroll down the table using Selenium, the previous information in the table is removed from the html and we are not able to have all elements from the table to be in its html at once*<br><br>


## Data Cleaning
Before cleaning and transforming, we apply `.info()` to check the structure and details of dataframe. For example,<br>
![Cleaning_00](assets/data_cleaning/Cleaning_00.png)

We also apply `.head()` to check how the first few observations looked like. For example,<br>
![redundant%20column](assets/data_access/redundant%20column.png)<br>


### Dropping column with only 1 unique value
Code: [IV_transformation.py](code/IV_transformation.py)<br>
We use `.nunique()` to check the value uniqueness in every column. If columns containing only 1 unique value and providing no useful information, they will be dropped by using `for` loop to iterate. 

Before dropping: <br>
![clean_01](assets/data_cleaning/clean_01.png)<br>

After dropping: <br>
![clean_02](assets/data_cleaning/clean_02.png)<br>


### Dropping Duplicates
Code: [IV_transformation.py](code/IV_transformation.py)<br>
`.drop_duplicates()` is used to drop any rows that are duplicated as duplicated rows will result into erroneous analysis such as aggregation and visualization. The sample code for dropping duplicates is as shown:<br>

`property_value_df = property_value_df.drop_duplicates()`<br>

### Dropping unnecessary columns
Code: [IV_transformation.py](code/IV_transformation.py)<br>
After dropping columns containing only 1 unique value and providing no useful information, we also observe that there are a lot of unneccessary columns based on business sense or perceiving that information in columns are duplicated.

For example for `rent_own_df`, columns of `ID Year`, `Household Ownership Moe`, `ID Geography`, `Slug Geography` are unnecessary columns.

Those columns that provide no values for analysis are dropped with following code:<br>
`rent_own_df=rent_own_df.drop(['ID Year', 'Household Ownership Moe', 'ID Geography', 'Slug Geography'], axis=1)`<br>

### Data type conversion
Code: [rent_price.py](code/rent_price.py)<br>
After checking with `.info()`, we find that data scraped from census bureau are all in `string` type, we need convert the median rent prices into `float` for imputation of null values 
as well as for the analysis and visualization. The example code to convert them from `string` to `numeric` is as shown below: <br>

`overall_census_rent_df[['Total','No bedroom','1 bedroom','2 bedrooms','3 bedrooms','4 bedrooms','5 or more bedrooms']] = overall_census_rent_df[['Total','No bedroom','1 bedroom','2 bedrooms','3 bedrooms','4 bedrooms','5 or more bedrooms']].apply(pd.to_numeric).astype('Float64')`<br>

### Null imputation
Code: [rent_price.py](code/rent_price.py)<br>

We check if dataframe containing nulls using `isnull().sum()`. The only dataframe with nulls is rent price. It is as shown below:<br>
![clean_03](assets/data_cleaning/clean_03.png)<br>

Before moving on into imputation, we check if the skewness of the affected columns is between -2 and 2 (if it is, it is close to normal). This will guide us on method of imputation. The skewness inspection is as shown:<br>
![clean_04](assets/data_cleaning/clean_04.png)<br>

If the skewness shows that the distribution is close to normal, we use mean imputation as follows:<br>
![clean_05](assets/data_cleaning/clean_05.png)<br>



## Data Transformation:
Raw data requires data processing or cleaning before it can be applied for intended use. Data transformation may include, but not limited to, columns and rows selection(e.g., keep only observations related to Stillwater/Payne County), keys (`Year` as primary key in this case) generation to facilitate joining processes, deriving new columns by calculations, data aggregations and summarizations, column splitting, and data transposing.


### Punctuation removal
Code: [rent_price.py](code/rent_price.py)<br>
Data containing punctuation will be considered as `string` in Python. Therefore, punctuation is removed to facilitate data type conversion (into numeric). We assign all possible punctuation to `punc` and then we use `for` loop to iterate through every character in every cell and `.replace()` is applied to replace all punctuation with nothing.<br>
Before removal:<br>
![Transformation_01](assets/data_transformation/Transformation_01.png)<br>

After removal: <br>
![Transformation_02](assets/data_transformation/Transformation_02.png)<br>


### Transposing Dataframe
Code: [rent_price.py](code/rent_price.py)<br>
Transposing is applied to convert row values into columns, we applied that on rent price data to ensure that every row contains value of just respective years. The example is as shown below: <br>

![Transformation_9](assets/data_transformation/Transformation_9.png)<br>

### Restructuring Columns using `groupby`
Code: [IV_transformation.py](code/IV_transformation.py)<br>
Some raw dataframes are not well-structured. Therefore, we restructure them using `groupby` function. Below is the example of usage of `groupby` function:<br>

![Transformation_4](assets/data_transformation/Transformation_4.png)<br>


### Constructing Population Dataframe from `stillwater_age_population` Csv File
Code: [IV_transformation.py](code/IV_transformation.py)<br>
Stillwater population data for each year is derived from [stillwater_age_population.csv](data/transformed/age_population/stillwater_age_population.csv) using the following codes:<br>

`population_df = age_df.drop(['Age_Min','Age_Max'], axis=1).groupby(['Year']).sum()`<br>

### Splitting interval columns for further calculation
Code: [IV_transformation.py](code/IV_transformation.py)<br>
We convert some interval variables to 2 columns to lay a foundation to calculate median for data consolidation where each year will be consolidated to one row. <br>

For example, we converted the interval `Age` in age dataframe into columns `Age_Min` and `Age_Max` using regular expression using the code below:<br>

![Transformation_8](assets/data_transformation/Transformation_8.png)<br>

Result:<br>
![Transformation_6](assets/data_transformation/Transformation_6.png)<br>

### Renaming column
Code: [IV_transformation.py](code/IV_transformation.py)<br>
Some column headers from raw files are misleading. Therefore, we rename the column headers prevent confusion. The example code and result are as shown below:<br>
![Transformation_5](assets/data_transformation/Transformation_5.png)<br>

### Sorting columns
Code: [IV_transformation.py](code/IV_transformation.py)<br>
Sorting columns mainly on `Year` variable are done to maintain consistency of dataframes and ease of viewing. The example is shown below:<br>
![Transformation_7](assets/data_transformation/Transformation_7.png)<br>

### Median (Grouped Data)
Code: [data_consolidation.py](code/data_consolidation.py)<br>
Some of the independent variables, such as age, household income and property value, had many bins for the same year. So, in order to consolidate these rows, we calculated median value for age, household income, and property value and used those statistics as our representative value for that year. Median (for grouped data) is calculated using the following function:<br>
![Transformation_10](assets/data_transformation/Transformation_10.png)<br>



## Data Reduction
Code: [IV_transformation.py](code/IV_transformation.py)<br>
Since we have removed unnecessary columns and duplicated values, for this section, we only focus on reducing rows to keep worthy data in our dataframe.<br>

We keep the data related to Oklahoma State University because our main idea is to display trend of rent prices in Stillwater, Payne County, Oklahoma.<br>

The code that we used with regular expression is:<br>
`enrollment_df = enrollment_df[enrollment_df['University'].str.contains('(?:Oklahoma State)')]`<br>


The data frame before data reduction.<br>
![Before_filter](assets/data_reduction/Before_filter.png)<br>

The data frame after data reduction.<br>
![After_filter](assets/data_reduction/After_filter.png)<br>



## Data Consolidation
Every transformed csv file were consolidated into a year a row to avoid complexity of final csv file.

### Filtering using regular expression
Code: [data_consolidation.py](code/data_consolidation.py)<br>
Some of the dataframes contain data that is not suitable for final csv file, for example, `Geography` in `rent_own_df` other than `Payne County`. However, those data is still valuable and worth keeping for the other analysis and visualization. Therefore, for final csv file, we select only data that is related using regular expression, for example, geography location of Stillwater/Payne County. The example code is as shown below:<br>

`rent_own_df = rent_own_df[rent_own_df['Geography'].str.contains('(?:Payne)')]`<br>

### Merging and Joining
Code: [data_consolidation.py](code/data_consolidation.py)<br>
After making sure every potential dataframe is consolidated, we merge them together using inner join on `Year` key. The example code is as shown below:<br>

![consolidation_02](assets/data_consolidation/consolidation_02.png)<br>

Merged data is output as [final_rent.csv](data/consolidated/final_rent.csv)<br>


## Data Dictionary

### Consolidated csv file ([final_rent.csv](data/consolidated/final_rent.csv)):<br>

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | The year for which the observation is for | integer | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 2021 |
| Median Age | The median age of the population | float | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 23.67671095791405 |
| Population | Population of the area | integer | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 47523 |
| Median Household Income | Median household income for the area | float | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 	32241.652466367712 |
| Household Counts | Number of Housholds | integer | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 18080 |
| Median Property Value | Median Property valuation of houses | float | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 	185317.81187410586 | 
| Property Counts | Number of properties in the area | integer | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 6752 | 
| University | University Name | string | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | Oklahoma State University-Main Campus	 | 
| Enrollment | Number of students enrolled in University | integer | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 25930 | 
| Household Ownership | Total Number of houses owned in the city | integer | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 15152 | 
| Household Ownership Share | Share of house owned by individuals ( Ranges from 0 to 1) | float | https://datausa.io/ | [final_rent.csv](data/consolidated/final_rent.csv) | 0.502320647129028 | 
| Overall Median Rent | Overall median price rent | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| No Bedroom | Median rent price for property without a bedroom |  float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| 1 Bedrooms | Median rent price for property with 1 bedroom | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| 2 Bedrooms | Median rent price for property with 2 bedrooms | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| 3 Bedrooms | Median rent price for property with 3 bedrooms | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| 4 Bedrooms | Median rent price for property with 4 bedrooms | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
| 5 or more bedrooms | Median rent price for property with 5 or more bedrooms | float | https://data.census.gov/ | [final_rent.csv](data/consolidated/final_rent.csv) | 779.0 |
<br>

### Age and Population ([stillwater_age_population.csv](data/transformed/age_population/stillwater_age_population.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [stillwater_age_population.csv](data/stillwater_age_population.csv) | 2020 | 
| Age | Age range of bucket | integer | https://datausa.io/  | [stillwater_age_population.csv](data/stillwater_age_population.csv) | 18 to 24 years |
| Age_Min | Minimum age within age bucket | integer | https://datausa.io/ | [stillwater_age_population.csv](data/stillwater_age_population.csv) | 18 |
| Age_Max | Maximum age within age bucket | float (because contain `inf`) | https://datausa.io/ | [stillwater_age_population.csv](data/stillwater_age_population.csv) | 24.0 |
| Population | Number of people in Stillwater, Oklahoma that fit within the given age range during a specified year | integer | https://datausa.io/ | [stillwater_age_population.csv](data/stillwater_age_population.csv) | 18484 |<br><br>

### Employment by Industry ([emp_industry.csv](data/emp_industry.csv))
| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [emp_industry.csv](data/emp_industry.csv) | 2020
| Industry | Industry Name | string | https://datausa.io/ | [emp_industry.csv](data/emp_industry.csv) | Education |
| Workforce | Number of People in the Industry | integer | https://datausa.io/ | [emp_industry.csv](data/emp_industry.csv) | 2451 |
<br>

### Student Enrollment ([enrollment.csv](data/enrollment.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | http://www.company.org | [enrollment.csv](data/enrollment.csv) | 2020 |
| University | Name of University | string | https://datausa.io/ | [enrollment.csv](data/enrollment.csv) | Oklahoma State University - Main Campus |
| Enrollment | Number of Students Enrolled | integer | https://datausa.io/ | [enrollment.csv](data/enrollment.csv) | 24512 |<br>

### Household Income ([household_income.csv](data/household_income.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [household_income.csv](data/household_income.csv) | 2020 |
| Household Income Bucket | Household Income Bucket | string | https://datausa.io/ | [household_income.csv](data/household_income.csv) | $10,000-$14,999 |
| Household_Income_Min | Household Income Bucket Minimum Value | integer | https://datausa.io/ | [household_income.csv](data/household_income.csv) | 10000 |
| Household_Income_Max | Household Income Bucket Maximum Value | float (because contain `inf`) | https://datausa.io/ | [household_income.csv](data/household_income.csv) | 14999.0 |
| Geography | Location | string | https://datausa.io/ | [household_income.csv](data/household_income.csv) | Stillwater, OK |
| Household Counts | Number of Households in the Specified Bin | integer | https://datausa.io/ | [household_income.csv](data/household_income.csv) |<br>

### Property Value ([property_value.csv](data/property_value.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [property_value.csv](data/property_value.csv) | 2020 |
| Value Bucket | Property Value Bin | string | https://datausa.io/ | [property_value.csv](data/property_value.csv) | $10,000 to $14,999 |
| Value_Min | Property Value Bin Minimum Value | integer | https://datausa.io/profile/ | [property_value.csv](data/property_value.csv) | 10000 |
| Value_Max | Property Value Bin Maximum Value | float (because contain `inf`) | https://datausa.io/ | [property_value.csv](data/property_value.csv) | 14999.0 |
| Geography | Location | string | https://datausa.io/ | [property_value.csv](data/property_value.csv) | Stillwater, OK |
| Property Counts | Number of properties in specified location within the specified bin | string | https://datausa.io/ | [property_value.csv](data/property_value.csv) | 103 |

### Rent and Own Levels ([rent_own.csv](data/rent_own.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [rent_own.csv](data/rent_own.csv) | 2020 |
| Household Ownership | Number of household ownerships | integer | https://datausa.io/ | [rent_own.csv](data/rent_own.csv) | 16201 |
| Geography | Location | string | https://datausa.io/ | [rent_own.csv](data/rent_own.csv) | Stillwater, OK |
| Share | Percent of households that are owned | float | https://datausa.io/ | [rent_own.csv](data/rent_own.csv) | 0.5168442544503286 |

### Domestic Trade Levels ([trade_growth.csv](data/trade_growth.csv))

| Attribute Name | Description | Data Type | Source | Data | Example |
| :--- |:--- | :--- |:--- | :--- |:--- |
| Year | Year | integer | https://datausa.io/ | [trade_growth.csv](data/trade_growth.csv) | 2020 |
| Millions of Dollars | Monetary value of imported goods (in millions) | float | https://datausa.io/ | [trade_growth.csv](data/trade_growth.csv) | 2727737.5 |
| Thousands of Tons | Weight of imported goods (in tons) | float | https://datausa.io/profile/ | [trade_growth.csv](data/trade_growth.csv) | 3025587.0 |
| Origin | Where the shipment originated | string | https://datausa.io/ | [trade_growth.csv](data/trade_growth.csv) | Oklahoma |
| Timeframe | Past or Future date | string | https://datausa.io/ | [trade_growth.csv](data/trade_growth.csv) | Past |

## Conclusion and Discussion

### Issues and Challenges

1. Only 6 rows of data (data from year 2015 to 2020) are available in consolidated csv file [final_rent.csv](data/consolidated/final_rent.csv).

2. Some useful websites for example https://www.rentdata.org/ and https://www.apartments.com/ are blocked from scraping due to legal issue. Using `website/robots.txt` allows us to check if a website is blocked from scraping.

3. Dataset like [employment by industries](data/transformed/emp_industry/emp_industry.csv) are tough to consolidate and merge into 1 table without making the consolidated data too complex to analyse due to multiple nominal categories.<br>

### Recommended Solutions

1. For Issue 1:
- Some websites store data with a timeframe of only up to a few years. We should start collecting data early before the websites removing the older data. Perhaps, manual data collection like surveys can be done. However, this solution will be extremely time-consuming.
- If the project objectives are more general, datasets with older observations can be easily found and scraped. So, we can provide more insights from the dataset; yet, it sacrifices specificity of objectives.

2. For Issue 2:
- Contacting the owner or manager of blocked websites are one of the ways to scrape blocked websites. However, risk of being rejected or delayed in response cannot be ignored especially with tight timeframe.
- Some websites, though blocked, have their data collected from general or public source like census data. Locating the public source could be another way to bypass blocked websites.

3. For Issue 3:
- Thorough investigation on necessity of the mentioned data could be conducted to see if the data is necessary for the analysis. This could avoid wasting time on unnecessary dataset.
- If it turns out significant, we could try separate to data from the master table and design an entity relationship diagram to connect the tables. If analysis is required, we could join the data using primary and foreign key into a dataframe and analyze it. <br>

### Goals and Implications of this Project

1. Incoming Students, Existing Students, People of Stillwater <br>
- To gain information on housing demand and expected housing expenses for financial management
2. Statisticians and Analysts, Real Estate & Housing Businesses, City of Stillwater <br>
- To maintain competitiveness in rent prices, to prevent overpricing in rent, and to plan housing development efficiently according to forecasted demand.<br>
3. Overall Public<br>
- To have a big picture of demographics and property/rent information of Payne County. <br>

### References 
Charles, Michelle. *City of Stillwater Continues COVID Assistance with Phase 3 Rent and Utility Aid.* Stillwater News Press, 24 Mar. 2022, https://autos.yahoo.com/city-stillwater-continues-covid-assistance-050400868.html.<br>

Mize, Richard. *It's Not Bedlam, but Stillwater Beats Norman When It Comes to Apartment Living.* The Oklahoman, Oklahoman, 11 Aug. 2022, https://www.oklahoman.com/story/business/real-estate/2022/08/11/oklahoma-college-towns-stillwater-norman-among-cheapest-rent/65398735007/.