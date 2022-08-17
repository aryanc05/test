# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:22:25 2022

@author: Aryan Chadha
"""
import pandas as pd
df = pd.read_csv(r'C:\Users\Aryan Chadha\Downloads\final_df.csv')
print(df.tail())
# bhaiya here I found the mean of one of the column 
print(df["manual_height"].mean()) 
# here I used total sum / total no of values 
mean=(df["manual_height"].sum())/(df["manual_height"].count())
print(mean)
# here I found the median of the manual weight column 
#print(df["manual_weight"].median())
# median :
x=df["manual_weight"].sort_values()
a=df["manual_weight"].count()
print(a)

if a //2 ==0:
    first= x[a//2]
    second=x[a//2-1]
    median=(first+second)/2
    print(median)
else:
    median= x[a//2]
    print(median)
    

# now mode of scan_height column
#print(df["scan_height"].mode())