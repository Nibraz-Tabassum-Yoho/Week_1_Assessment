import pandas as pd
import numpy as np

df=pd.read_csv("employees.csv")

print('\n',df.info()) #The info() function displays information about a DataFrame
print('\n',df.describe()) #Used to generate statistical information about a DataFrame

names=df.loc[df["department"]=="IT","name"]
print("\nIT:",",".join(names))
print()
print(df.iloc[0:3, 1:3])


departments = pd.DataFrame({
    'department': ['Sales', 'HR', 'IT', 'Finance', 'Legal'],
    'head': ['Anita Sharma', 'Rahul Verma', 'Priya Nair','Amit Kumar', 'Neha Rao'],
    'budget': [500000, 300000, 800000, 600000, 200000]
})

departments.to_csv('departments.csv', index=False)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())


median_salary = df['salary'].median()
df['salary'] = df['salary'].fillna(median_salary)
print("\nMedian salary:", median_salary)

df = df.drop_duplicates()

# Correct data types
df['id'] = df['id'].astype('int64')
df['name'] = df['name'].astype('string')
df['department'] = df['department'].astype('string')
df['salary'] = df['salary'].astype('int64')
df['city']=df['city'].astype('string')


print("\nCleaned dataset:")
print(df)

print("\nCorrected data types:")
print(df.dtypes)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicates after cleaning:",df.duplicated().sum())

df.to_csv('employees_cleaned.csv', index=False)

dpt=pd.read_csv("departments.csv")

department_stats = df.groupby('department').agg(
    headcount=('id', 'count'),
    average_salary=('salary', 'mean'),
    maximum_salary=('salary', 'max')
).reset_index()
print(department_stats)

inner_merge = pd.merge(dpt,df,on='department', how='inner')
print("\nInner Merge:")
print(inner_merge)


dpt = pd.merge(
    departments,
    department_stats,
    on='department',
    how='left'
)

# print("\nMerged DataFrame:")
# print(dpt)

left_merge = pd.merge(dpt,df,on='department', how='left')
print("\nLeft Merge:")
print(left_merge)

outer_merge = pd.merge(dpt,df,on='department', how='outer')
print("\nOuter Merge:")
print(outer_merge)

empty_departments = dpt.loc[
    dpt["headcount"].isna(), "department"
]
print("\nDepartments with no employees listed:")
print(empty_departments)