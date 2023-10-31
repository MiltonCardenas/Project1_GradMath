
""" Estatistical analysis file
    

"""

import numpy as np
import pandas as pd
import scipy as sc
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

if "df" not in locals():
    df =  pd.read_csv('../Datasets/project_dataset.csv')



# =============================================================================
# FACTOR 1 MEAN WORK TIME (reminder = plot the groupped data)

# Data into two groups: below and above the median "Mean work time"
median = df['Mean usual hours (Men+Women)'].median()                      
below_median = df[df['Mean usual hours (Men+Women)'] < median]['deaths']
above_median = df[df['Mean usual hours (Men+Women)'] >= median]['deaths']

# Two-sample t-test
t_stat, p_value = ttest_ind(below_median, above_median)                         # t-test
alpha = 0.05                                                                    # significance level

# Results
if p_value < alpha:
    result = "statistically significant"
else:
    result = "not statistically significant"

print(f"The t-statistic is {t_stat:.2f} and the p-value is {p_value:.4f}. The impact of higher work time on COVID deaths is {result}.")

# ==============================================================================
# FACTOR 2 AGRICULTURAL SECTOR FACTOR

df['Percentage'] = df['2020 16+ civilian employed in: Agriculture, forestry, fishing, and hunting)'] / df['Total 2020 16+ civilian employed']

median = df['Percentage'].median()                      
below_median = df[df['Percentage'] < median]['deaths']
above_median = df[df['Percentage'] >= median]['deaths']

# Two-sample t-test
t_stat, p_value = ttest_ind(below_median, above_median)                         # t-test
alpha = 0.05                                                                    # significance level

# Results
if p_value < alpha:
    result = "statistically significant"
else:
    result = "not statistically significant"

print(f"The t-statistic is {t_stat:.2f} and the p-value is {p_value:.4f}. The impact of work in Agriculture-related sectors on COVID deaths is {result}.")

# ================== GRAPHIC CONFIGURATION =====================================

plt.figure(figsize=(8, 6))  

mean_hours = df['Mean usual hours (Men+Women)']

# Box Plot
ax = plt.boxplot(x=mean_hours)

# Quartiles
q1 = mean_hours.quantile(0.25)
q2 = mean_hours.median()
q3 = mean_hours.quantile(0.75)

# Display quartile values on the plot
plt.text(0.7, q1, f'Q1 = {q1}', verticalalignment='center')
plt.text(1.1, q2, f'Median = {q2}', verticalalignment='center')
plt.text(0.7, q3, f'Q3 = {q3}', verticalalignment='center')

plt.ylabel('Mean work time (h/week)')
plt.title('Mean work time distribution')
plt.show()






