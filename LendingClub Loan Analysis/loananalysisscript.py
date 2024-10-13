# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:16:27 2024

@author: Akash Rana
"""

#import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset in file
loan_data = pd.read_excel('loandataset.xlsx')
customer_data = pd.read_csv('customer_data.csv', sep=';')

#Display first few rows of dataset
print(loan_data.head())
print(customer_data.head())

#Merging two dataframe
complete_data = pd.merge(loan_data,customer_data, left_on='customerid', right_on='id')

#Check for missing data
complete_data.isnull().sum()

#Remove rows with missing data
complete_data = complete_data.dropna()

#Check for duplicate data
complete_data.duplicated().sum()

#Dropping duplicates
complete_data = complete_data.drop_duplicates()

#Function in python
#Create a function to categorize purpose into broader categories
def categorize_purpose(purpose):
    if purpose in ['credit card','debt_consolidation']:
        return 'Financial'
    elif purpose in ['educational', 'small_business']:
        return 'Educational/Business'
    else:
        return 'Others'
    
categorize_purpose('credit card')
complete_data['purpose_category'] = complete_data['purpose'].apply(categorize_purpose)

#Create a new function based on criteria
#If the dti ratio is more than 20 and the delinq.2years is greater than 2 and the revol.util>60 then the borrower is high risk
def assess_risk(row):
    if row['dti'] > 20 and row['delinq.2yrs'] > 2 and row['revol.util'] > 60:
        return 'High Risk'
    else:
        return 'Low Risk'

complete_data['Risk'] = complete_data.apply(assess_risk, axis=1)


#Creates a function to categorize FICO scores
def categorize_fico(fico_score):
    if fico_score >= 800 and fico_score <= 850:
        return 'Excellent'
    elif fico_score >= 740 and fico_score < 800:
        return 'Very Good'
    elif fico_score >= 670 and fico_score < 740:
        return 'Good'
    elif fico_score >= 580 and fico_score < 670:
        return 'Fair'

complete_data['fico_category'] = complete_data['fico'].apply(categorize_fico)

#Identify with more than average inquiries and derogotary records within function
def identify_high_inq_derg(row):
    average_iq = complete_data['inq.last.6mths'].mean()
    average_derog = complete_data['pub.rec'].mean()
    
    if row['inq.last.6mths'] > average_iq and row['pub.rec'] > average_derog:
        return True
    else:
        return False

complete_data['High_Inqury_and_Public_Records'] = complete_data.apply(identify_high_inq_derg, axis=1)

#Create Data Analysis class to calculate summary statistics
class DataAnalysis:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
    
    def calculate_mean(self):
        return self.df[self.column_name].mean()
        
    def calculate_median(self):
        return self.df[self.column_name].median()

analysis = DataAnalysis(complete_data, 'fico')
mean_fico = analysis.calculate_mean()
meadian_fico = analysis.calculate_median()

#Data Visualization
#Bar plot to show distribution of loan by purpose



















