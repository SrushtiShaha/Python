import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# 1. Create DataFrame for 5 Students and Display it
# -------------------------------------------------------

data = {
    'Name': ['Vighnesh', 'Prathamesh', 'Srushti', 'Pavan', 'Nikita'],
    'Gender': ['M', 'M', 'F', 'M', 'F'],
    'Age': [16, 17, 16, 18, 17],
    'Maths': [80, 70, 78, 92, 88],
    'Science': [80, 95, 55, 89, 84],
    'English': [78, 88, 72, 91, 85]
}

df = pd.DataFrame(data)
print("Student DataFrame:\n")
print(df)

# -------------------------------------------------------
# 2. Bar Chart – Average Marks by Subject
# -------------------------------------------------------

avg_marks = df[['Maths', 'Science', 'English']].mean()

avg_marks.plot(kind='bar',
               color=['Red', 'orange', 'Green'],
               title='Average Marks by Subject')
plt.ylabel('Average Marks')
plt.show()

# -------------------------------------------------------
# 3. Pie Chart – Average Marks by Subject
# -------------------------------------------------------

avg_marks.plot(kind='pie',
               autopct='%1.1f%%',
               startangle=90,
               colors=['gold', 'lightgreen', 'skyblue'],
               title='Average Marks by Subject')
plt.ylabel('')
plt.show()

# -------------------------------------------------------
# 4. Histogram – Age Distribution
# -------------------------------------------------------

df['Age'].plot(kind='hist',
               bins=5,
               color='lightgreen',
               edgecolor='black',
               title='Age Distribution')
plt.xlabel('Age')
plt.show()

# -------------------------------------------------------
# 5. Scatter Plot – Maths vs Science Marks
# -------------------------------------------------------

plt.figure(figsize=(7, 5))
plt.scatter(df['Maths'], df['Science'], color='teal', s=100)

plt.title('Maths vs Science Marks', fontsize=14)
plt.xlabel('Maths Marks', fontsize=12)
plt.ylabel('Science Marks', fontsize=12)
plt.grid(True)

# Add student names on the points
for i, name in enumerate(df['Name']):
    plt.text(df['Maths'][i] + 0.5, df['Science'][i] + 0.5, name, fontsize=9)

plt.show()
