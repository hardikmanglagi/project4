import pandas as pd
data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\project folder\python\pythonlibrary\pandas_file\projects1.csv")
# display top 10 row of dataset
print(data.head(10))

# dispplay last 10 row of dataset
print(data.tail(10))

# check datatype for each column
data.dtypes

# check null values
print(data.isnull().sum())

# count no of row and column in dataset
print(data.info)
print(len(data.columns))
print(len(data))

# higest and loest purches price
print(data['Purchase Price'].max())
print(data['Purchase Price'].min())

# average purchase price
print(data['Purchase Price'].mean())

# fr language
print(data[data['Language'] == 'fr'].count())

# job title contains engineer
print(len(data[data['Job'].str.contains('engineer', case=False)]))

# find eamil of the persom with the ip addres: 132.207.160.22
print(data[data['IP Address']=="132.207.160.22"]['Email'])


# how many person have master card  as their creadit provider and made a purchase above 50?
print(len(data[(data['CC Provider'] == 'Mastercard')  &  (data['Purchase Price'] > 50)]))

6
# find eamil of the person with the following creadit card number:4664825258997302
print(data[data['Credit Card'] == 4664825258997302]['Email'])

# how many people purchase during the AM and How many people purchase durig PM
print(data['AM or PM'].value_counts())

#  how many people have a creadit card that expires on 2020?
print(len(data[data['CC Exp Date'].apply (lambda x:x[3:] == '20')]))

# top 5 most populor eamil providers(eg .gmail.com, yahoo.como, etc.....)
print(data["Email"].apply(lambda x:x.split('@')[1]).value_counts().head())