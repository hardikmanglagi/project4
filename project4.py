import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects4.csv")
# display top 10 row of dataset
print(data.head(10))

# dispplay last 10 row of dataset
print(data.tail(10))

# find shape of our dataset (number of rows and number of column)
print(data.shape)
print("Number of rows:", data.shape[0])
print("Number of column:", data.shape[1])

#  gettting information about our dataset like total number rows, total number of column , dataset of each column and memory requirement
print(data.info())


#  get overall statistics about the dataframe 
print(data.describe())

#  data filtering
print(data[['Name','Age']])
print(data['Sex'] == 'male')
print(sum(data['Sex'] == 'male'))
# print all details of true value
print(data[data['Sex'] == 'male'].head())
#  check survived person
print(data['Survived']==1)
print(sum(data['Survived']==1))
print(data[data['Survived']==1])

# check null values
print(data.isnull().sum())
per_missing = data.isnull().sum()* 100/ len(data)
print(per_missing)

#  drop higest missing value column
print(data.drop('Cabin',axis=1))

# handle missing value
print(data['Embarked'].mode())
data['Embarked'] = data['Embarked'].fillna('S',inplace=True)
print(data['Embarked'])
print(data.isnull().sum())
# handle misssing value in age column
data['Age'] = data['Age'].fillna(data['Age'].mean(), inplace=True)
print(data['Age'])
print(data.isnull().sum())

#  categorical data encoding
print(data['Sex'].unique())
data['Gender'] = data['Sex'].map({'male':1, 'female': 0})
print(data['Gender'])
x = data['Sex'].map({'male':1, 'female': 0})
print(data.insert(5,"Gender_New", x))
print(data.columns)

# frint name and number of categoric
print(data['Embarked'].unique())
print(data['Embarked'].nunique())
#  real emnarked column is deleted and new number of categoric columns add in per categoric
print(pd.get_dummies(data,columns=['Embarked']))
#  real sex column is delete and new spacefic column like {sex_male and sex_female}
print(pd.get_dummies(data,columns=['Sex']))

#  what is univariate analyis?
# 1. how many people survived and how many died
print(data['Survived'].value_counts())

# 2. hoe many passengers were in first class, second class and third class?
print(data['Pclass'].value_counts())

# 3. number of malea and female passengers
print(data['Sex'].value_counts())
print(plt.hist(data['Age']))

# Feature Engineering
print(data.columns) 
data['Family_Size'] = data['SibSp'] + data['Parch']
print(data['Family_Size']) 
data['Fare_Per_Person'] = data['Fare'] / data['Family_Size'] + 1 
print(data['Fare_Per_Person'])
