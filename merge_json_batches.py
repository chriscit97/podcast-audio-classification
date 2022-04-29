#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:49:15 2022

This script is to merge json files with batches of features into one finaliaed dataframe that can be worked with and dumped

Is used with local files repeatedly with different parameters

@author: chris
"""

import json
import pandas as pd
 
with open('time_experiments/baseline_pop_leading_5min_train_500.json') as f1:               # open the file
    df1 = json.load(f1)
    
df1.pop("title")
df1 = pd.DataFrame.from_dict(df1)
print('loaded df1')

with open('time_experiments/baseline_pop_leading_5min_train_500_2500.json') as f2:               # open the file
    df2 = json.load(f2)
    
df2.pop("title")
df2 = pd.DataFrame.from_dict(df2)
print('loaded df2')

with open('time_experiments/baseline_pop_leading_5min_train_2500_3000.json') as f3:              # open the file
    df3 = json.load(f3)

df3.pop("title")
df3 = pd.DataFrame.from_dict(df3)
print('loaded df3')

with open('time_experiments/baseline_pop_leading_5min_train_3000_3905-003.json') as f4:              # open the file
    df4 = json.load(f4)
    
df4.pop("title")
df4 = pd.DataFrame.from_dict(df4)
print('loaded df4')

# Export full df
df3 = pd.concat([df1, df2, df3, df4])         # Concat DataFrames
df3.reset_index(inplace=True) 
df3.to_json("lead_baseline_pop_train_features_rec.json", orient='records', lines=True)


