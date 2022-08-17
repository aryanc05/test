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
# here I found the median of the manual weight column 
print(df["manual_weight"].median())
# now mode of scan_height column
print(df["scan_height"].mode())
# this gives all mathematical values
df.describe()
#
print(df["pose_score"].std())