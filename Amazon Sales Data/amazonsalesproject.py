# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 00:17:31 2024
Questions to be answered

- How many sales have they made with amounts more than 1000
- How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
- The Total Sales by Category
- Average Amount by Category and Status
- Total Sales by Fulfillment and Shipment Type

@author: Akash Rana
"""

import pandas as pd

#load sales data from excel file
sales_data = pd.read_excel('sales_data.xlsx')

# =============================================================================
# Exploring the Data
# =============================================================================
#get summary of sales data
sales_data.info()
sales_data.describe()

#check the columns
print(sales_data.columns)

#have a look at first few data
print(sales_data.head())

#check the data types of column
print(sales_data.dtypes)

# =============================================================================
# Cleaning the data
# =============================================================================

#check for the null value. here it shows null value total count in each column
print(sales_data.isnull().sum())

#drop or reomve all null/Nan value from the dataframe
sales_data_droppped = sales_data.dropna()

#drop only rows with the missing amount from amount columns
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

#check for the null value in sales_data_cleaned. here it shows null value total count in each column
print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and Filtering Data
# =============================================================================

#select subsetof the data based upon the category column
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)

#Question 1:How many sales have they made with amounts more than 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

#Question 2:  How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
filtered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)]

# =============================================================================
# Aggregating Data
# =============================================================================

#Question 3: The Total Sales by Category
category_total = sales_data.groupby('Category')['Amount'].sum()
category_total = sales_data.groupby('Category',as_index=False)['Amount'].sum()
category_total = category_total.sort_values('Amount', ascending=False)

# Average Amount by Category and Fulfilment
fulfilment_average = sales_data.groupby(['Category','Fulfilment'],as_index=False)['Amount'].mean()
fulfilment_average = fulfilment_average.sort_values('Amount', ascending=False)

# Question 4: Average Amount by Category and Status
status_average = sales_data.groupby(['Category','Status'],as_index=False)['Amount'].mean()
status_average = status_average.sort_values('Amount', ascending=False)

# Question 5: Total Sales by Fulfillment and Shipment Type
total_sales_by_shipmentandfulfil = sales_data.groupby(['Courier Status','Fulfilment'],as_index=False)['Amount'].sum()
total_sales_by_shipmentandfulfil = total_sales_by_shipmentandfulfil.sort_values('Amount', ascending=False)

total_sales_by_shipmentandfulfil.rename(columns = {'Courier Status':'Shipment'}, inplace = True)

# =============================================================================
# Exporting Data
# =============================================================================

status_average.to_excel('average_sales_by_Category_and_Status.xlsx', index=False)
total_sales_by_shipmentandfulfil.to_excel('total_sales_by_shipmentandfulfil.xlsx', index=False)







