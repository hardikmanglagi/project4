import pandas as pd

# Read CSV File
# df = pd.read_csv("data.csv", encoding="latin1")

# Read EXCEL file
# df = pd.read_excel("pdata.xlsa")

# Read json file
# df = pd.read_json("pdata.json")
# print(df)


sale_data = { 
    "Name": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
    "Age" : [10,20,30,40,50,60,70,80,90,100],
    "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
    "salery": [50000,60000,70000,80000,90000,100000,110000,120000,130000,140000],
    "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
    "Age" : [10,20,30,40,50,60,70,80,90,100],
    "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
    "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
    "Age" : [10,20,30,40,50,60,70,80,90,100],
    "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
    "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
    "Age" : [10,20,30,40,50,60,70,80,90,100],
    "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper']
} 

df = pd.DataFrame(sale_data)
print(df)

# SAVE FILE IN CSA FILE
# df.to_csv("pandasdata.csv", index= False)

# SAVE FILE IN EXCEL FILE
# df.to_excel("pdata.xlsx")

# SAVE FILE IN JSON FILE
# df.to_json("pdata.json")


# select multipal starting and ending row
print('Display First 10 line')
print(df.head())

print('Display Last 10 column ')
print(df.tail())

#  represent no of column and row of your data, and what datatype of data, and missing data
print('Displaying the info of data set')
print(df.info())


print(df)
print("DESCRIPTIVE STATISTICE")
print(df.describe())

# How big is your data
print("Display shape of data mean rows and column")
print(f'SHAPE: {df.shape}')

# What are the names of column
print("represent name of column")
print(f'Column Names: {df.columns}')


# filter and select column and combine multipal condition

# selesct single column
name = df["Name"]
print(name)

# select multipal column
subset = df[["Name","Age"]]
print(subset)

# apply single condition
high_salary = df[df["salery"] > 40000]
print('Employee list with salary  > 40000')
print(high_salary)

# filtering rows salary > 50 & age > 30
filtered = df[(df['salery'] > 50000) & (df['Age']> 30)]
print("multipal condition using and")
print(filtered)

#  using OR condition
filtered_or = df[(df['Age'] > 30 ) | (df['salery'] > 100000)]
print(' condition OR')
print(filtered_or)
































