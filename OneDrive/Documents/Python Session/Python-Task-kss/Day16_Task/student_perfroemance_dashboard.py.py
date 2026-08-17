import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student marks
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Convert to Pandas DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# Line Graph 
plt.figure()
plt.plot(df["Student"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart 
plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart 
pass_count = (marks > 50).sum()
fail_count = (marks <= 50).sum()

plt.figure()
plt.pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%"
)
plt.title("Pass vs Fail")
plt.show()

# Histogram 
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# Scatter Plot 
plt.figure()
plt.scatter(df.index, df["Marks"])
plt.title("Index vs Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()
