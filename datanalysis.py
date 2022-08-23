# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:22:25 2022

@author: Aryan Chadha
"""
sum=0
count=0
val=0
import pandas as pd
df = pd.read_csv(r'C:\Users\Aryan Chadha\Downloads\final_df.csv')

def mean (database,columnname):
    count=0
    sum=0
    for i in range(len(database)):
        sum=sum+ database.loc[i,columnname]
    for i in range(len(database)):
        count=count+1
    print(sum/count)
def median (database,columnname):
    val=0
    for i in range(len(database)):
        val=val+1
    database[columnname].sort_values()

    if count //2 ==0:
        first= database.loc[val//2-1,columnname]
        second=database.loc[val//2, columnname]
        median=(first+second)/2
        print(median)
    else:
        median= database.loc[val//2,columnname]
        print(median)
median (df,"scan_height")

def mode(database,columnname):
    dict1={}
    list1=[]
    for i in database[columnname]:
        if i in dict1:
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1
    freq=0
    for i in dict1:
        if dict1[i]> freq :
            freq=dict1[i]
            mode=i
    list1.append(mode)
    for i in dict1 :
        if dict1[i]==freq and mode!=i:
            list1.append(i)
    list1.sort()
        
            
    print(list1)
mode (df,"scan_height")
print(df["scan_height"].mode())
        























