import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects5.csv")
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
print(data.describe(include='all'))

#  total number of app titles contain astrolofy
print(len(data[data['App'].str.contains('Astrology', case=False)]))

#  find average app rating
print(data['Rating'].mean())

# find total number of unique category
print(data['Category'].nunique())

# which caategory getting the higest aveerage rating?
print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False))

#  find total number of app having 5 star rating
print(len(data[data['Rating'] == 5.0]))

#  find average value of reviews
# print(data['Reviews'].mean())

# .find total number of free and paid apps
print(data['Type'].value_counts())

#  which app has maximum reviews?
print(data[data['Reviews'].max() ==data['Reviews']]['App'])

#  display top 5 apps having higest reviews
top5 = data.sort_values(by='Reviews', ascending=False).head(5)
print(top5[['App', 'Reviews']])


#  find average rating of free and paid apps
print(data.groupby('Type')['Rating'].mean())

# display top 5 app having maximum installs
top5_installs = data.sort_values(by='Installs', ascending=False).head(5)
print(top5_installs[['App', 'Installs']])
