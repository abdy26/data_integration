#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:52:23 2023

@author: manuelgutierrez
"""

import pandas as pd
try:
    # Load the CSV file into a pandas dataframe
    df_NETFLIX = pd.read_csv('NetFlix 2.csv')
    df_MOVIES = pd.read_csv('tmdb_5000_movies.csv')
    df_ROTTEN = pd.read_csv('rotten_tomatoes_top_movies 2.csv')
    df_MD = pd.read_csv('movies_metadata.csv')
except:
    print("I tried")


# Print the dataframe
#print(df_NETFLIX)
#print("")
#print(df_MOVIES)
#print("")
#print(df_ROTTEN)
#print("")
#print(df_MD)
#print("Hello world") 

#join them 

c1 = df_NETFLIX['title']
c2 = df_MOVIES['original_title']
c3 = df_ROTTEN['title']
c4 = df_MD['original_title']


print(c1)
print('')
print(c2)
print('')
print(c3)
print('')
print(c4)
print('')


column_set1 = set(c1)
column_set2 = set(c2)
column_set3 = set(c3)
column_set4 = set(c4)

print("setsss----------")
#print(column_set1)
#print(column_set2)
#print(column_set3)
#print(column_set4)

join = column_set1 & column_set2 & column_set3 & column_set4
print(join)


#df = df.sort_values('Name')
#NETFLIX
selected_rows = df_NETFLIX[df_NETFLIX['title'].isin(join)]
selected_rows = selected_rows.sort_values('title')
selected_rows.to_csv('GOOD_NETFLIX_ROWS', index=False)

#MOVIES
selected_rows = df_MOVIES[df_MOVIES['original_title'].isin(join)]
selected_rows = selected_rows.sort_values('original_title')
selected_rows.to_csv('GOOD_MOVIES', index=False)

#ROTTEN
selected_rows = df_ROTTEN[df_ROTTEN['title'].isin(join)]
selected_rows = selected_rows.sort_values('title')
selected_rows.to_csv('GOOD_ROTTEN', index=False)

#MMD
selected_rows = df_MD[df_MD['original_title'].isin(join)]
selected_rows = selected_rows.sort_values('original_title')
selected_rows.to_csv('GOOD_MD', index=False)



