# -*- coding: utf-8 -*-
"""

@author: Stylianos Argyrou

"""

import pandas as pd
import datetime

# Variables that include the start and end of each COVID-19 lockdown in London

first = datetime.datetime(2020, 3, 26)
first_end = datetime.datetime(2020, 5, 10)
second = datetime.datetime(2020, 11, 5)
second_end = datetime.datetime(2020, 12, 12)
third = datetime.datetime(2021, 1, 6)
third_end = datetime.datetime(2021, 7, 19)

# Dataset
data = pd.read_excel('../Crime/Borough Daily 2018-20.xlsx')
data2021 = pd.read_excel('../Crime/Borough Daily Data 2021.xlsx')
df = pd.concat([data, data2021])

# Fill each empty value with the corresponding mean of each variable.
df = df.fillna(df.mean())

# Renamed the column for easier use and then sort the dataframe
df = df.rename(columns={'Date - Daily Data': 'date'})
df = df.sort_values(by="date")

# Initialise values for the arrays so that the data for each lockdown can be 
# included in each corresponding file
lock_list1 = []
lock_list2 = []
lock_list3 = []
before_lock_list = []
all = []

# Iterate over all the entries of the dataframe to split the rows into 
# the different lockdowns
for i, row in df.iterrows():
    date = row["date"]
    row["date"] = row["date"].strftime('%Y%m%d')
    
    
    if (date < first):
        before_lock_list.append(row)
    
    if (date > first) and (date < first_end):
        lock_list1.append(row)
        
    if (date > second) and (date < second_end):
        lock_list2.append(row)
        
    if (date > third) and (date < third_end):
        lock_list3.append(row)
    
    all.append(row)
    
# Put the lists into dataframe objects
data_lock1 = pd.DataFrame(lock_list1)
data_lock2 = pd.DataFrame(lock_list2)
data_lock3 = pd.DataFrame(lock_list3)
before_lock = pd.DataFrame(before_lock_list)

# Used for the interactive graph
all1 = pd.DataFrame(all).groupby(by="date").sum()
all1 = all1.astype(int)
all1.to_csv("data.tsv", sep = "\t")


# Used to store the number of crimes for each category for each borough in 
# different files.

# data_lock1.to_csv("Lockdown1.csv", index = False)
# data_lock2.to_csv("Lockdown2.csv", index = False)
# data_lock3.to_csv("Lockdown3.csv", index = False)
# before_lock.to_csv("Before_Lockdown.csv", index = False)

# data_lock1.to_csv("Lockdown1.tsv", sep="\t")
# data_lock2.to_csv("Lockdown2.tsv", sep="\t", index = False)
# data_lock3.to_csv("Lockdown3.tsv", sep="\t", index = False)
# before_lock.to_csv("Before_Lockdown.tsv", sep="\t", index = False)




