import pandas as pd

# -----------------------------
# A. Create Employee DataFrame
# -----------------------------
data = {
    "Name": ["Amit", "Sneha", "Rohit", "Priya", "Kunal", "Meera"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 40000, 55000, 60000, 42000, 58000]
}

df = pd.DataFrame(data)

# -----------------------------
# B. Display DataFrame
# -----------------------------
print("Employee DataFrame:\n", df)

# -----------------------------
# C. Split into groups (Department-wise)
# -----------------------------
grouped = df.groupby("Department")

# -----------------------------
# D. Display each group
# -----------------------------
print("\nGroups:")
for dept, group in grouped:
    print(f"\nDepartment: {dept}")
    print(group)

# -----------------------------
# E. Average Salary per Department
# -----------------------------
avg_salary = grouped["Salary"].mean()
print("\nAverage Salary per Department:\n", avg_salary)
