import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('2020_MeanWorkTime.csv') 
df['state'] = df['NAME'].str.split(', ').str[-1]
df['county'] = df['NAME'].str.split(', ').str[0]
pennsylvania_data = df[df['state'] == 'Pennsylvania']

counties = pennsylvania_data['county']
total_hours = pennsylvania_data['B23020_001E']

fig, ax = plt.subplots(figsize=(20, 6))
ax.bar(counties, total_hours, color='b', label="Data per county")
ax.set_title('Pennsylvanie Deaths in 2020')
ax.set_xlabel('Countie')
ax.set_ylabel('Deaths')


plt.xticks(rotation=90)

plt.tight_layout()
plt.gcf().autofmt_xdate()                                                  # Ensures labels fit nicely in the plot
plt.show()

