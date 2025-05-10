""""
import pandas as pd
data = {
    'Name':['Alice','Bob','Charlie'],
    'Age':[24,27,21],
    'city':['Borderland','Los Angles','USA']
}
df = pd.DataFrame(data)
print(df)
df.to_csv('employees.csv', index=False)
df.to_json('employees.json', orient='records')

import pandas as pd
data = {
    'emp_id':[5657,3690,1117],
    'emp_name':['John wick','Boogeyman','Bounty Hunter'],
    'emp_salary':[1000,20000,20000]
}
df = pd.DataFrame(data)
print(df)
df.to_csv('employees.csv', index=False)
df.to_json('employees.json', orient='records')


#To Read CSV Json Files
df_csv = pd.read_csv('employees.csv')
print(df_csv)
df_json = pd.read_json('employees.json')
print(df_json)


#Adding new record to the existing CSV file
new_data = pd.DataFrame([{'Name':'David','Age':25,'City':'San Francisco'}])
df_csv = pd.read_csv('employees.csv')
#pd.concat Append the new DataFrame to the existing one
df_csv = pd.concat([df_csv, new_data], ignore_index=True)
df_csv.to_csv('employees.csv', index=False)


#Adding new record to the existing JSon file
new_data_json = pd.DataFrame([{'': 25,'emp_name': 'David','City': 'San Francisco'}])
df_json = pd.read_json('employees.json')
#pd.concat Append the new DataFrame to the existing one
df_json = pd.concat([df_json, new_data_json], ignore_index=True)
df_json.to_json('employees.json', orient='records')

#Deleting Data from Csv FIle
df_csv = pd.read_csv('employees.csv')
df_csv = df_csv[df_csv['emp_name'] != 'John wick']
df_csv.to_csv('employees.csv', index=False)

# Deleting Data from JSON File
df_json = pd.read_json('employees.json')
df_json = df_json[df_json['emp_name'] != 'John wick']
df_json.to_json('employees.json', orient='records')

#Book Specification
import pandas as pd
data = {
    'Book_id':[69,96,99],
    'Book_Name':['Naruto','Onepiece','Bleach'],
    'Author':['Hashimoto','Jinhwoh','Eren Eager'],
    'Price':[999,888,777]
        }
df = pd.DataFrame(data)
print(df)
df.to_csv('Book.csv', index=False)

#Adding New Data to Existing File
new_data = pd.DataFrame([{'Book_id':7894,'Book_Name':'David Gogins','Author':'David','Price':99}])
df_csv = pd.read_csv('Book.csv')
df_csv = pd.concat([df_csv, new_data], ignore_index=True)
df_csv.to_csv('Book.csv', index=False)

#deleting Data from Existing File
df_csv = pd.read_csv('Book.csv')
df_csv = df_csv[df_csv['Book_Name'] != 'Onepiece' ]
df_csv.to_csv('Book.csv', index=False)
"""
import pandas as pd
import numpy as np
data = {
'Age': [25, 30, np.nan, 35, np.nan],
'Salary': [50000, 54000, 58000, np.nan, 62000],
'Gender': ['Male', 'Female', np.nan, 'Female', 'Male'],
'Department': ['HR', np.nan, 'IT', 'Finance', 'IT']
}
df = pd.DataFrame(data)
print(df)
print("\ncount of Missing Values in Each Column:\n",df.isnull().sum())
df_dropped = df.dropna()
print("\nDataFrame after Dropping Rows with Missing Values:\n", df_dropped)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after Filling 'Age' with Mean:\n", df)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
print("\nDataFrame after Filling 'Salary' with Median:\n", df)
df['Age'].fillna(df['Age'].mode()[0], inplace=True)
