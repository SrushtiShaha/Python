import pandas as pd
import numpy as np

# A. Employee DataFrame
data = {
    "Name": ["Vighnesh", "Prathamesh", "Srushti", "Pavan", "Nikita"],
    "Age": [25, np.nan, 30, 28, np.nan],
    "Salary": [30000, 45000, np.nan, 50000, 35000]
}

df_emp = pd.DataFrame(data)
print("\nEmployee DataFrame:\n", df_emp)
print("\nSummary Statistics:\n", df_emp.describe())
print("\nNull values:\n", df_emp.isnull().sum())

# Replace missing values (Correct way)
df_emp["Age"] = df_emp["Age"].fillna(df_emp["Age"].mean())
df_emp["Salary"] = df_emp["Salary"].fillna(df_emp["Salary"].median())

print("\nAfter replacing missing values:\n", df_emp)

# B. Products.csv
df_prod = pd.read_csv("C:/Vighnesh Kadam/products.csv")

print("\nProducts Summary:\n", df_prod.describe())
print("\nNull values:\n", df_prod.isnull().sum())

# Replace missing price
df_prod["Price"] = df_prod["Price"].fillna(df_prod["Price"].mean())

print("\nAfter replacing missing values:\n", df_prod)
