# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:35:22 2024

@author: Akash Rana
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Set working directory
os.chdir('E:/Python Code/Source (Input) Data for the course/Ecommerce Orders Project')

#Check current working directory
print(os.getcwd())

# =============================================================================
# Loading Files
# =============================================================================

#load orders data
orders_data = pd.read_excel('orders.xlsx')

#load payments data
payments_data = pd.read_excel('order_payment.xlsx')

#load customers data
customers_data = pd.read_excel('customers.xlsx')

# =============================================================================
# Describing Data
# =============================================================================
orders_data.info()
payments_data.info()
customers_data.info()

#check missing data
orders_data.isnull().sum()
payments_data.isnull().sum()
customers_data.isnull().sum()

#filling missing value in orders data with default value
orders_data2 = orders_data.fillna('N/A')
orders_data2.isnull().sum()

#drop/delete rows with missing value in payments data
payments_data = payments_data.dropna()
payments_data.isnull().sum()

# =============================================================================
# Removing Duplicate Data
# =============================================================================
orders_data.duplicated().sum()

#remove deuplicate fro orders data
orders_data = orders_data.drop_duplicates()

#check duplicate from payments data
payments_data.duplicated().sum()
payments_data = payments_data.drop_duplicates()

# =============================================================================
# Filtering the data
# =============================================================================

#select a subset for orders data based on orders status
invoiced_orders_data = orders_data[orders_data['order_status'] == 'invoiced']
invoiced_orders_data = invoiced_orders_data.reset_index(drop=True)

#select subset of payments data where payment type is credit card and value is greater than 1000.
credit_card_payment_data = payments_data[(payments_data['payment_type'] == 'credit_card') & (payments_data['payment_value'] > 1000)]

#select subset of customer based on customer state = SP
SP_state_customer = customers_data[customers_data['customer_state'] == 'SP']

# =============================================================================
# Merge and Join dataframe
# =============================================================================

#Merge orders data with payments data on order id
merged_data = pd.merge(orders_data, payments_data, on='order_id')

#Join merge data with customer data on customer_id column
joined_data =pd.merge(merged_data, customers_data, on='customer_id')

# =============================================================================
# Data Visulization
# =============================================================================

#Create field call month_year from order_purchase_timestamp
joined_data['month_year'] = joined_data['order_purchase_timestamp'].dt.to_period('M')
joined_data['week_year'] = joined_data['order_purchase_timestamp'].dt.to_period('W')
joined_data['year'] = joined_data['order_purchase_timestamp'].dt.to_period('Y')

grouped_data = joined_data.groupby('month_year')['payment_value'].sum()
grouped_data = grouped_data.reset_index()

#convert month_year from period to string
grouped_data['month_year'] = grouped_data['month_year'].astype(str)

#Creating a Plot
plt.plot(grouped_data['month_year'] ,grouped_data['payment_value'], color='red', marker='o')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Month and Year')
plt.ylabel('Payment Value')
plt.title('Payment Value by Month and Year')
plt.xticks(rotation = 90, fontsize=8)
plt.yticks(fontsize=8)

#Scatter plot
#create dataframe 
scatter_df = joined_data.groupby('customer_unique_id').agg({'payment_value': 'sum', 'payment_installments' : 'sum'})

plt.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])
plt.xlabel('Payment Value')
plt.ylabel('Payment Installment')
plt.title('Payment Value by Payment Installment by Customer')

#Seaborn to create Scatter Plot
sns.set_theme(style='darkgrid') #options: whitegrid, dark, white
sns.scatterplot(data=scatter_df, x='payment_value', y='payment_installments')
plt.xlabel('Payment Value')
plt.ylabel('Payment Installment')
plt.title('Payment Value by Payment Installment by Customer')

#Creating Bar chart for payment value by payment type
bar_chart_df = joined_data.groupby(['payment_type', 'month_year'])['payment_value'].sum()
bar_chart_df = bar_chart_df.reset_index()

pivot_data = bar_chart_df.pivot(index='month_year', columns='payment_type', values='payment_value')
pivot_data.plot(kind='bar' , stacked='True')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Month of Payment')
plt.ylabel('Payment Value')
plt.title('Payment per Payment type by month')

#Creating a box plot
payment_values = joined_data['payment_value']
payment_types = joined_data['payment_type']

#Creating a seprate box plot for payment types
plt.boxplot ([
    payment_values[payment_types == 'credit_card'],
    payment_values[payment_types == 'boleto'],
    payment_values[payment_types == 'voucher'],
    payment_values[payment_types == 'debit_card'],
    ], labels=['Credit card box plot', 'Boleto box plot', 'Voucher box plot', 'Debit card box plot'])

#Set label and Titles
plt.xlabel('Payment Type')
plt.ylabel('Payment Value')
plt.title('Box plot showing Payment Value ranges by Payment Type')
plt.show()

#Creating a sub plots (3 in One)
fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(10,10))

#ax which is subplot
ax1.boxplot ([
    payment_values[payment_types == 'credit_card'],
    payment_values[payment_types == 'boleto'],
    payment_values[payment_types == 'voucher'],
    payment_values[payment_types == 'debit_card'],
    ], labels=['Credit card box plot', 'Boleto box plot', 'Voucher box plot', 'Debit card box plot'])

#Set label and Titles
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Payment Value')
ax1.set_title('Box plot showing Payment Value ranges by Payment Type')

#ax2 is stacked bar chart
pivot_data.plot(kind='bar' , stacked='True', ax=ax2)
ax2.ticklabel_format(useOffset=False, style='plain', axis='y')

#set label and title
ax2.set_xlabel('Payment Type')
ax2.set_ylabel('Payment Value')
ax2.set_title('Bar plot showing Payment Value ranges by Payment Type')

#ax3 is Scatter plot
ax3.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])

#set label and title
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installment')
ax3.set_title('Payment Value by Payment Installment by Customer')

fig.tight_layout()
