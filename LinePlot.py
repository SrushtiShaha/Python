import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Bags': [2000, 2500, 3000, 2800, 3500, 4000],
    'Notebooks':[2200,2500,1500,3000,2250,4000]
}

df = pd.DataFrame(data)

print(df)

# Create Line Plot
plt.plot(df['Month'], df['Bags'])
plt.plot(df['Month'], df['Notebooks'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Line Plot")
plt.show()
