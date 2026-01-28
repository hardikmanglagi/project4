import numpy as np
import pandas as pd

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects2.csv")
# display top 10 row of dataset
print(data.head(10))

# dispplay last 10 row of dataset
print(data.tail(10))

# find shape of our dataset (number of rows and number of column)
print("Number of rows:", data.shape[0])
print("Number of column:", data.shape[1])

#  gettting information about our dataset like total number rows, total number of column , dataset of each column and memory requirement
print(data.info())

# check null values
print(data.isnull().sum())

# drop id, notes, agency ,status columns
print(data.drop(['Id', 'Notes','Agency','Status'],axis=1))

#  get overall statistics about the dataframe in all column using include='all'
print(data.describe(include='all'))

#  find occurrence of the employee names(top 5)
print(data['EmployeeName'].value_counts().head(5))

#  find the number of unique job titles
print(data['JobTitle'].nunique())

# total number of job title contain captain
print("comntain captain")
print(len(data[data['JobTitle'].str.contains('CAPTAIN', case=False)]))
print(data[data['JobTitle'].str.contains('CAPTAIN', case=False)].count())

# display all the employee names from fire depatment
print(data[data['JobTitle'].str.contains('fire', case=False)]['EmployeeName'])

# find minimum, maximum and average basepay
print('max and amiin')
print(data['BasePay'].describe())

# replace not provided in employeeName column to NaN
print(data['EmployeeName'].replace('Not provided', "NaN"))

#  drop the rows having 5 missing values
# print(data.drop(data.isnull().head(5)))

# find job title of albert pardini
print(data[data['EmployeeName']=='ALBERT PARDINI']['JobTitle'])

# how much albert pardini make(include benefit)?
print(data[data['EmployeeName'] == 'ALBERT PARDINI']['TotalPayBenefits'])

#  display name of the person having the higest basepay
# print(data[data['BasePay'].max() == data['BasePay']]['EmployeeName']) 

# find average basepay of all employee per yera
# print(data.groupby('Year').mean(numeric_only=True)['BasePay'])

#  find average basepay of all employee per jobtitle
# print(data.groupby('JobTitle').mean()['BasePay'])

#  find average basepay of employee having job title accountant 
print("acc job")
print(data[data['JobTitle'] == 'ACCOUNTANT']['BasePay'].mean())

#  find top 5 most common jobs
print(data['JobTitle'].value_counts().head())

