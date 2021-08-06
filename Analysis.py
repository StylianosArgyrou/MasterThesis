# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:16:20 2021

@author: styar
"""

import pandas as pd
import datetime

first = datetime.datetime(2020, 3, 26)
first_end = datetime.datetime(2020, 5, 10)
second = datetime.datetime(2020, 11, 5)
second_end = datetime.datetime(2020, 12, 12)
third = datetime.datetime(2021, 1, 6)
third_end = datetime.datetime(2021, 7, 19)

# borough_months = pd.read_excel("../Crime/Borough Daily 2018-20.xlsx")

data = pd.read_excel('../Crime/Borough Daily 2018-20.xlsx')
data2021 = pd.read_excel('../Crime/Borough Daily Data 2021.xlsx')

df = pd.concat([data, data2021])
borough_months = df
borough_months = borough_months.fillna(borough_months.mean())


borough_months = borough_months.rename(columns={'Date - Daily Data': 'date'})
borough_months = borough_months.sort_values(by="date")
print(borough_months["date"].head())

# borough_months["Total Crimes"] = borough_months.sum(axis=1)

lock_list1 = []
lock_list2 = []
lock_list3 = []
before_lock_list = []
all = []

for i, row in borough_months.iterrows():
    # date = row["Month-Year"]
    date = row["date"]
    row["date"] = row["date"].strftime('%Y%m%d')
    # print(row["date"])
    
    if (date < first):
        # row["date"] = row["date"].strftime("%Y%m%d")
        before_lock_list.append(row)
    
    if (date > first) and (date < first_end):
        # row["date"] = row["date"].strftime("%Y%m%d")
        lock_list1.append(row)
        
    if (date > second) and (date < second_end):
        # row["date"] = row["date"].strftime("%Y%m%d")
        lock_list2.append(row)
        
    if (date > third) and (date < third_end):
        # row["date"] = row["date"].strftime("%Y%m%d")
        lock_list3.append(row)
    
    # row["date"] = row["date"].strftime("%Y%m%d")
    all.append(row)
    
data_lock1 = pd.DataFrame(lock_list1).groupby(by="date").sum()
data_lock2 = pd.DataFrame(lock_list2)
data_lock3 = pd.DataFrame(lock_list3)
before_lock = pd.DataFrame(before_lock_list)
all1 = pd.DataFrame(all).groupby(by="date").sum()
all1 = all1.astype(int)
all1.to_csv("data.tsv", sep = "\t")


# data_lock1.to_csv("Lockdown1.csv", index = False)
# data_lock2.to_csv("Lockdown2.csv", index = False)
# data_lock3.to_csv("Lockdown3.csv", index = False)
# before_lock.to_csv("Before_Lockdown.csv", index = False)

# data_lock1.to_csv("Lockdown1.tsv", sep="\t")
# data_lock2.to_csv("Lockdown2.tsv", sep="\t", index = False)
# data_lock3.to_csv("Lockdown3.tsv", sep="\t", index = False)
# before_lock.to_csv("Before_Lockdown.tsv", sep="\t", index = False)

print(all1["Domestic Abuse Hate Crime Offs"])





