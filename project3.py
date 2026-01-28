
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects3.csv")
# display top 10 row of dataset
print(data.head(10))

# dispplay last 10 row of dataset
print(data.tail(10))

# find shape of our dataset (number of rows and number of column)
print("Number of rows:", data.shape[0])
print("Number of column:", data.shape[1])

#  gettting information about our dataset like total number rows, total number of column , dataset of each column and memory requirement
print(data.info())

#  fetch random sample from the dataset(50%)
print(data.sample(frac=0.50,random_state=100))


# check null values
print(data.isnull().sum())
# print(sns.heatmap(data.isnull()))

#  perform data cleaning [Replace '?' with NaN]
print(data.isin(['?']).sum())
print(data.columns)
data['workclass']=data['workclass'].replace('?', np.nan)
print(data['workclass'])
data['occupation']=data['occupation'].replace('?', np.nan)
print(data['occupation'])
data['native-country']=data[ 'native-country'].replace('?', np.nan)
print(data[ 'native-country'])
print(data.isin(['?']).sum())
# print(data.isnull().sum())
# print(sns.heatmap(data.isnull()))

#  drop all the missing values
print(data.dropna(how='any', inplace=True))
print(data.shape)

#  check for duplicate data and drop them
print(data.drop_duplicates())
print(data.shape)

#  get overall statistics about the dataframe 
print(data.describe())

# drop the column education-num, capital-gain, capital-loss
print(data.drop(['educational-num','capital-gain',  'capital-loss'],axis=1))

#  what is the distrubutaion of age column?
print(data['age'].hist())

#  find total number of person having age between 17 to 48 using between method
print(sum(data['age'].between(17,48)))

#  replace salary values ['<= 50k' , '>50k'] with 0 andd 1
print(data.replace(to_replace=['<=50K','>50K'], value=[0,1], inplace=True))
print(data.head(1))

#  which workclass geetting the higest salery?
print(data.groupby('workclass')['income'].mean().sort_values(ascending=False))

# hoe has better chance to get salary > 50K male or female
print(data.groupby('gender')['income'].mean().sort_values(ascending=False))

# convert workclass columns datatype to category datatype
data['workclass'] = data['workclass'].astype('category')
print(data['workclass'])
print(data.info())