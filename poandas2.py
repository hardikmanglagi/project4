import pandas as pd

# sale_data = { 
#     "Name": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
#     "Age" : [10,20,30,40,50,60,70,80,90,100],
#     "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
#     "salery": [50000,60000,70000,80000,90000,100000,110000,120000,130000,140000],
#     "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
#     "Age" : [10,20,30,40,50,60,70,80,90,100],
#     "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
#     "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
#     "Age" : [10,20,30,40,50,60,70,80,90,100],
#     "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
#     "Namme": ['ram', 'shyam', 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
#     "Age" : [10,20,30,40,50,60,70,80,90,100],
#     "city": ['ambala', 'kakrali', 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper']
# } 


# df = pd.DataFrame(sale_data)
# print(df)

# add new column 
# df['Bonus'] = df['salery'] * 0.1
# print(df)

# add new column in specefic location using insert() method
# df.inset(loc, "columnname" , some_data)
# df.insert(0, "Employee_id", [1,2,3,4,5,6,7,8,9,10])
# print(df)


# update a ram salery
# df.loc[0, 'salery'] = 550000
# print(df)

# increasing salery by 5%
# df['salery'] = df['salery'] * 1.05
# print(df)

#  Remove one column
# df.drop(columns=['city'], inplace=True)
# print(df)

# remove multipal column
# df.drop(columns=['city','Age'], inplace=True)
# print(df)



# sale_data = {
#     "Name": ['ram', None, 'sharma','hari','harpreet','hardik','aditi','anita','aman','anuj'],
#     "Age" : [10,None,30,40,50,60,70,80,90,100],
#     "city": ['ambala', None, 'toda','mouli','cant','barwala','natwal','batood','khanper','babalper'],
#     "salery": [50000,None,70000,80000,90000,100000,110000,120000,130000,140000]
# } 


# df = pd.DataFrame(sale_data)
# print(df)

# print True valuse is missing or Folse value is not missing
# sum() method represent a no of missing value in each column
# print(df.isnull().sum())

# dropna() drop a None vale in data and x =1 drop None column and x=0 drop None rows
# df.dropna(inplace=True)
# print(df)

#  fill a missing value in and default number
#  fillna(value , inplace=True)
# df.fillna(0, inplace=True)
# print(df)

# fill a missing vale after mean and calculation
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# df['salery'].fillna(df['salery'].mean(), inplace=True)
# print(df)


# interpolation fill a None vale and smooth trands folow and avoid data loss and data integrity
# df.interpolate( method="linear" , aixs=0, inplace = true
# print("After interpolation")
# df['Age'] = df['Age'].interpolate(method='linear')
# print(df)
# df['salery'] = df['salery'].interpolate(method='linear')
# print(df)


# PERFORM A SORTING 
# data = {
#     "Name": ['ram','hardik', 'aditi','sharma','hari','harpreet'],
#     "Age" : [10,40,30,50,60,80],
#     "salery": [50000,30000,10000,60000,90000,110000]
# }

# df = pd.DataFrame(data) 
# perform sorting in single column
# df.sort_values(by='Age', ascending=True, inplace=True)
# print(df)
# perform sorting in multipal column
# df.sort_values(by=['Age','salery'], ascending=[True,False], inplace=True)
# print(df)


# data = {
#     "Name": ['ram','hardik', 'aditi','aditi','hardik','harpreet'],
#     "Age" : [10,60,80,10,60,80],
#     "salery": [50000,30000,10000,60000,90000,110000]
# }

# df = pd.DataFrame(data) 

# FIND MEAN OF SPECEFIC COLUMN
# avg_salery = df['salery'].mean()
# print(avg_salery)

# find max salery of data
# max_sal =df['salery'].max()
# print(max_sal)

# find minimum salery of data
# min_sal = df['salery'].min()
# print(min_sal)

# sum all slaery
# sum_sal = df['salery'].sum()
# print(sum_sal)

#  perform count method
# count_sal = df['salery'].count()
# print(df)

# create a group after that calulate sum of every group salery
# grouped = df.groupby("Age")["salery"].sum()
# print(grouped)

#  create a group based on two column and calculate sum
# grouped = df.groupby(['Age','Name'])['salery'].sum()
# print(grouped)


#  merging a two file and enething else
#  syntax=  pd.merge(df1,df2, on="column_name", how="inner,outer,left,right,cross")
df_customer = pd.DataFrame({
    'customerID' : [1,2,3,4],
    'name' : ['hardik', 'aditi', 'anita', 'amit']
})

df_order = pd.DataFrame({
     'customerID' : [1,2,3,5],
     'salery' : [30000,40000,50000,60000]
})

# merge df_customer and df_order based on inner
# df_merged = pd.merge(df_customer , df_order, on="customerID", how='inner')
# print(df_merged)


# merge df_customer and df_order based on outer value does not match fill NAN vale
# df_merged = pd.merge(df_customer , df_order, on="customerID", how='outer')
# print(df_merged)


# merge df_customer and df_order based on left (mean df_customer)
# df_merged = pd.merge(df_customer , df_order, on="customerID", how='left')
# print(df_merged) 

# merge df_customer and df_order based on RIGHT (mean df_order)
# df_merged = pd.merge(df_customer , df_order, on="customerID", how='right')
# print(df_merged)


# concatenate vertically
# print(df_customer)
# print(df_order)
# df_concat = pd.concat([df_customer,df_order], axis=0,ignore_index=True)
# print(df_concat)


customer_profile = pd.DataFrame({
    'customerID' : [1,2,3,4],
    'Name':['Gopal','Raju','hardik','aditi']
})

transcation_history = pd.DataFrame({
    'customerID' :[1,2,3,5],
    'transcation_amount' : [200,300,400,500]
})

df_merged = pd.merge(customer_profile , transcation_history, on="customerID", how='outer')
print(df_merged)
df_concat = pd.concat([customer_profile,transcation_history], axis=1,ignore_index=True)
print(df_concat)