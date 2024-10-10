# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 03:00:16 2024

@author: Akash Rana
"""

import pandas as pd
from datetime import datetime

#Export excel file
pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_size_df = pd.read_csv('pizza_size.csv')
pizza_category_df = pd.read_csv('pizza_category.csv')
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx')
pizza_sales_voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')

#Viewing top and bottom few rows of database
pizza_sales_df.head(10)
pizza_sales_df.tail(10)

#Describing the Data
pizza_description = pizza_sales_df.describe()

#Have a look at non null counts per columns
pizza_sales_df.info()

#Count the null value within data base
null_count = pizza_sales_df.isnull().sum()

#Check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()
print(duplicated_rows)

#To select the column
quantity_column = pizza_sales_df['quantity']
selected_column = pizza_sales_df[['order_id', 'quantity', 'unit_price']]

#get row with index label 3
row = pizza_sales_df.loc[3]

#get two rows with index label 3 and 5
rows = pizza_sales_df.loc[[3 , 5]]

#Get rows between index no 3 and 5 and specific column
subset = pizza_sales_df.loc[3:5, ['quantity', 'unit_price']]

#Set an index as comlumnin a data frame
pizza_sales_df.set_index('order_details_id', inplace=True)

#Reseting an index
pizza_sales_df.reset_index(inplace=True)

#Truncate dataframe before index 3
truncted_before = pizza_sales_df.truncate(before=3)

#truncate dataframe after index 5
truncted_after = pizza_sales_df.truncate(after=5)

#Truncating column
quantity_series = pizza_sales_df['quantity']

#Truncating series before index 3
truncated_series_before = quantity_series.truncate(before=3)

#Truncating series After index 5
truncated_series_after = quantity_series.truncate(after=5)

#Filterning the database
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

#Filtering on Data
pizza_sales_df['order_date'] = pizza_sales_df['order_date'].dt.date
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[pizza_sales_df['order_date'] > date_target]

#Filtering on multiple condition
#Using the and condition
bbq_chicken_rows = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

#Using the or condition
bbq_chicken_rows_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 20) | (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

#Filter a specific range
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & (pizza_sales_df['unit_price'] <= 20)]

#Dropping Null Values
pizza_sales_null_value_dropped = pizza_sales_df.dropna()
null_count = pizza_sales_null_value_dropped.isnull().sum()

#Replace null with a value
date_na_fill = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(date_na_fill)

#Deleting specific rows and columns in datagrame
filtered_rows_2 = pizza_sales_df.drop(2, axis=0)

#Delete rows 5, 7, 9
filtered_rows_5_7_9 = pizza_sales_df.drop([5,7,9], axis=0)

#Delete column by column name
filtered_unit_price = pizza_sales_df.drop('unit_price',axis=1)

#Delete multiple columns
filtered_unit_price_order_id = pizza_sales_df.drop(['unit_price', 'order_id'],axis=1)

#Sorting a dataframe in pandas

#sorting and accending order
sorted_df = pizza_sales_df.sort_values('total_price')

#sorting and decending order
sorted_df = pizza_sales_df.sort_values('total_price', ascending=False)

#sort dataframe by multiple columns
sorted_df = pizza_sales_df.sort_values(['pizza_category_id','total_price'], ascending=[True,False])

#Group by pizza size id and get count of sales or row counts
grouped_df_pizza_size = pizza_sales_df.groupby(['pizza_size_id']).count()

#Group by pizza size id and get the sum of total price
grouped_df_pizza_size_sum = pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()

#Group by pizza size id and get the sum total price and quantity
grouped_df_pizza_size_sale_sum = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

#Looking at different aggregation function

#count(): Count number of any no null value i each group
#sum(): Sum the value in each group
#mean(): Calculate the mean value in each group
#std(): Computes the standard deviation in each group.
#var(): Computes the standard variance in each group.
#min(): Finds the minimum values in each group.
#max(): Finds the maximum values in each group.
#prod(): Computes the product of values in each group.
#first(), last(): Gets the first and last values in each group.
#size(): Returns the size of each group (including NaN/NA values).
#nunique(): Counts the number of unique values in each group.

grouped_df_aggregation= pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].mean()

#Using agg to perform different aggregation on different column
aggregated_data = pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity': 'sum', 'total_price':'mean'})

#Merging pizza_sales_df and pizza_size_df
merged_df = pd.merge(pizza_sales_df,pizza_size_df, on='pizza_size_id')

#Merging pizza_sales_df and pizza_category_df by adding category
merged_df = pd.merge(merged_df,pizza_category_df, on='pizza_category_id')

# Concate two dataframe -  appending rows to data frame - vertically
concatenate_vertically = pd.concat([pizza_sales_df, another_pizza_sales_df])
concatenate_vertically = concatenate_vertically.reset_index()

# Concate two dataframe -  appending columns to data frame - horizontally
concatenate_horizontally = pd.concat([pizza_sales_df, pizza_sales_voucher_df], axis = 1)

#Coverting to lower text
#lower_text = pizza_sales_df['pizza_ingrd']

































