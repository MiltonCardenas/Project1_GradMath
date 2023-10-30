
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Top_states  = ["California", "Texas", "Florida", "Pennsylvania", "Ohio"]

# df1 = Top 5 states data of COVID cases
if "df1" not in locals():
    df1 = pd.read_csv('../Datasets/us-counties-2020.csv')
    df1['county'] = df1['county'] + ' County'
    covid_data = df1[df1['state'].isin(Top_states)]                              # Extract data of the selected states

# df2 = Top 5 states data of mean work time
if "df2" not in locals():
    useful_col2 = ['NAME', 'B23020_001E']                                       
    df2 = pd.read_csv('../Datasets/2020_MeanWorkTime.csv', usecols=useful_col2) # Take useful columns of the dataset
    df2['state']  = df2['NAME'].str.split(', ').str[-1]                         # Split the column "Name and create a new column "state"
    df2['county'] = df2['NAME'].str.split(', ').str[0]                          # Split the column "Name and create a new column "county"
    New_names2 = {'B23020_001E':'Mean usual hours (Men+Women)'}
    df2 = df2.rename(columns=New_names2)                                        # Rename columns
    meantime_data = df2[df2['state'].isin(Top_states)]                          # Extract data of the selected states
     
# df3 = Top 5 states data of workers in each industry
if "df3" not in locals():
    useful_col3 = ['NAME', 'S2404_C01_001E', 'S2404_C01_003E']                    
    df3 = pd.read_csv('../Datasets/Industry_Dataset2020.csv',usecols=useful_col3) # Take useful columns of the dataset
    df3['state'] = df3['NAME'].str.split(', ').str[-1]
    df3['county'] = df3['NAME'].str.split(', ').str[0] 
    df3['S2404_C01_001E'] = pd.to_numeric(df3['S2404_C01_001E'], errors='coerce') # Convert the column to numeric, replacing non-numeric values with NaN
    df3['S2404_C01_003E'] = pd.to_numeric(df3['S2404_C01_003E'], errors='coerce')
    
    # Rename the column according to the dataset information
    New_names3 = {'S2404_C01_001E': 'Total 2020 16+ civilian employed',          # Rename columns
                 'S2404_C01_003E': '2020 16+ civilian employed in: Agriculture, forestry, fishing, and hunting)'}
    df3 = df3.rename(columns=New_names3)
    industry_data = df3[df3['state'].isin(Top_states)]                           # Extract data of the selected states
    
covid_data.to_csv("../Datasets/filtered_COVID.csv", index=False)                           # Save and exclude the index column
meantime_data.to_csv("../Datasets/filtered_meantime.csv", index=False)     
industry_data.to_csv("../Datasets/filtered_industry.csv", index=False)