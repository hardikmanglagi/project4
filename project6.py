import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects6.csv")
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

# check null values
print(data.isnull().sum())

# check for duplicate data and drop them
print("Before removing duplicates:")
print(data.duplicated().any())
data = data.drop_duplicates()
print("After removing duplicates:")
print(data.duplicated().any())

# find out number of courses per subjects
print(data['subject'].value_counts())

# for which levels, udemy courses provinding the courses
print(data['level'].value_counts())

#  display the count of paid and free courses
print(data['is_paid'].value_counts())

# which course has more lectures(free or paid
# print(data.groupby(['is_paid']).mean())

# which couses have a higher number of subscribers free or paid?

# find most popular course title
print(data[data['num_subscribers'].max() == data['num_subscribers']])

#  display 10 most popular courses ad per number of subscribers
print(data.sort_values(by='num_subscribers', ascending=False).head(5))

# find total number of courses relater to python
print(data['course_title'].str.contains('python', case=False))

#  display 5 most popular python courses as per number of subscribers
print(data[data['course_title'].str.contains('python', case=False)].sort_values(by='num_subscribers',ascending=False).head(5))

# in which yeqr the higest number of courses were posted?
# print(data['published_timestamp'].dt.year)

# display catrgory-wise coujnt of posted subjects[year wise]
print(data.groupby('year')['subject'].value_counts())
