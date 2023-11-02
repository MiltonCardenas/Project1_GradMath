# PROJECT 1, MATHEMATICAL METHODS

## 0. Organization

The present document is organized into the following folders:

### Datasets:
The purpose of this folder is to store all uncleaned datasets and tables with final data for the regression model. This folder contains all information related to the data.

### Executables:
The purpose of this folder is to house the executable codes that generate project results. There are two executables: the first one contains the code for data extraction from the databases in the previous folder. This code encompasses all the criteria used to clean the database and save the new clean dataset back into the datasets folder. The second file contains the executable for a Jupyter Notebook, which contains the code that generates the statistical results displayed in the project.

### Graphics and Results Storage:
The objective of this folder is to store all data for easy management and use for various purposes. This folder also supplies the graphics used in this document.

### Support Codes:
It contains a Python code with the same functionality and features as the Jupyter Notebook used in the project's development as a backup of information."

## OBJECTIVES:
The aim of this repository is to anwer the following questions related with the Covid-19 pandemic mortality:

### SINGLE FACTOR QUESTIONS:
 - Were counties with higher weekly working hours more likely to experience fatal outcomes during 2020?
 - Were counties with greater food and agriculture-related industry percentage more prone to experiencing fatal outcomes in the selected states in 2020?"

### DOUBLE FACTOR QUESTION:
Were workers in the food and agriculture sector in the Top 6 agricultural GDP states who spent more time at work more likely to experience fatal outcomes in 2020?


## POPULATION ANALIZED:
The population of workers in the agriculture sector of the 5 states with the most GDP and workers attributed to this sector was analyzed.
Selected states:
["California", "Texas", "Florida", "Pennsylvania", "New York", "Indiana"]

### The databases used were:
COVID DATABASE:
https://github.com/nytimes/covid-19-data/blob/master/us-counties-recent.csv

County-related information:
https://data.census.gov/table/ACSDT5Y2020.B23020?q=time&g=010XX00US$0500000
https://data.census.gov/table/ACSST5Y2020.S2404?q=Industry&g=010XX00US$0500000

## PRE-PROCESSING OF DATA:
- Elimination of unnecessary columns.
- Extraction of information of the top 6 agricultural employment states (Total GDP).
- Conversion of all numeric information into integer or float types.
- Organization of names. 
- Covid cases were grouped by county.

## Sort criteria:

Decendent's usual occupation:
Food / agriculture

Age range:
18 - 65 years


## RESULTS:

### FACTOR 1.

https://github.com/MiltonCardenas/Project1_GradMath/blob/main/Graphics%20and%20Results%20Storage/%20factor1_results.png

https://github.com/MiltonCardenas/Project1_GradMath/blob/main/Graphics%20and%20Results%20Storage/%20factor1_regression_summary.png

### FACTOR 2.

 https://github.com/MiltonCardenas/Project1_GradMath/blob/main/Graphics%20and%20Results%20Storage/%20factor2_results.png

https://github.com/MiltonCardenas/Project1_GradMath/blob/main/Graphics%20and%20Results%20Storage/%20factor2_regression_summary.png

## Double factor:

https://github.com/MiltonCardenas/Project1_GradMath/blob/main/Graphics%20and%20Results%20Storage/%20binary_regression_summary.png

## ANALYSIS OF RESULTS
 - It is not possible to conclude anything about the slopes of the groups because of the p-value. We cannot be confident about the difference between the groups (for both, factor 1 and factor 2).

 - If we adjust the significance level for the p-value of the regression concerning the impact of the percentage of workers in the agricultural industry on COVID-19 deaths, it might lead to accepting the null hypothesis.

 - There is no significant difference in the impact on COVID-19 cases for individuals who work longer hours. The p-value is significantly distant from the threshold, making it unlikely that this factor is associated with COVID-19 mortality.

 - There is no significance in the overall regression model of the double-factor analysis. 

## LIMITATIONS AND FUTURE ANALYSIS:
The COVID-19 deaths in the database were not directly linked to patient information, such as work-related details. A direct link would facilitate and improve the analysis.

Future analyses should investigate the influence of agricultural activity on mortality during documented pandemics to assess whether this population is susceptible to such events.

## CONCLUSIONS:
The p-value was significantly greater than the chosen significance level (e.g., 0.05). We find no statistically significant evidence that counties with higher weekly working hours were more likely to experience fatal outcomes in 2020.

While the p-value was close to the significance level, it did not meet the threshold for statistical significance. Therefore, we do not find sufficient evidence to conclude that counties with greater percentages of the food and agriculture-related industry were more prone to experiencing fatal outcomes in 2020. 

While the p-value was close to the significance level, it did not meet the threshold for statistical significance. Therefore, we do not find sufficient evidence to conclude that counties with greater percentages of the food and agriculture-related industry were more prone to experiencing fatal outcomes in 2020. 





