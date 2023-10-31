
""" Data_extraction file

    In this python file is contained all the process to convert the raw datasets
    into organized datasets following some criteria to extract the information
    
    Initial and final dataset names:
        
    from 
        us-counties-2020.csv
        Industry_Dataset2020.csv
        2020_MeanWorkTime.csv    
       
    to:
        project_dataset.csv  (Filtered and organized final dataset)
    
    Features:
    
    - Division of all names into counties and states
    - Extraction of information related to the top 6 agricultural employment states
    - Elimination of unuseful columns
    - Change of the column_names for non-coded names
    - Convertion of all numeric information into integer types
    - Creation of a new name column in the covid database to differentiate equal county names
    from differents states
    
"""


import pandas as pd

Top_states  = ["California", "Texas", "Florida", "Pennsylvania", "New York", "Indiana"]

# df1 = Top 5 states data of COVID cases
if "df1" not in locals():
    df1 = pd.read_csv('../Datasets/us-counties-2020.csv')
    df1['county'] = df1['county'] + ' County'
    df1['county'] = df1['county'].replace('New York City County', 'New York County')
    df1['NAME'] = df1['county'] + ', ' + df1['state']                           # Create a new NAME column to avoid similar county names
    df1 = df1[df1['state'].isin(Top_states)]                          # Extract data of the selected states
    df1 = df1[df1['county'] != 'Unknown County']  # Delete unknown data
    covid_data = df1.groupby('NAME')['deaths'].sum().reset_index()    # Deaths per country

# df2 = Top 5 states data of mean work time
if "df2" not in locals():
    useful_col2 = ['NAME', 'B23020_001E']                                       
    df2 = pd.read_csv('../Datasets/2020_MeanWorkTime.csv', usecols=useful_col2) # Take useful columns of the dataset
    df2['state']  = df2['NAME'].str.split(', ').str[-1]                         # Split the column "Name and create a new column "state"
    df2['county'] = df2['NAME'].str.split(', ').str[0]                          # Split the column "Name and create a new column "county"
    df2['B23020_001E'] = pd.to_numeric(df2['B23020_001E'], errors='coerce')     # Convert the column to numeric, replacing non-numeric values with NaN
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

county_list = meantime_data['NAME'].unique()
df = covid_data.merge(meantime_data, on='NAME', how='outer')
df = df.merge(industry_data, on='NAME', how='outer')
df = df.fillna(0)                                             # Fill miss values with 0
df = df[df['Mean usual hours (Men+Women)'] >= 10]                            # Delete data outliers (not possible a mean below 10 h /week)

columns_to_delete = ["state_x", "state_y", "county_x", "county_y"]
df = df.drop(columns=columns_to_delete, axis=1)
df.to_csv("../Datasets/project_dataset.csv", index=False)
