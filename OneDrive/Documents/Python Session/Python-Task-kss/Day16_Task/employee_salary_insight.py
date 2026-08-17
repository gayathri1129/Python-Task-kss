import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

# Line Graph 
plt.figure()
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Bar Chart 
plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Month-wise Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#  Pie Chart 
plt.figure()
plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
plt.title("Monthly Sales Contribution")
plt.show()

# Histogram 
plt.figure()
plt.hist(df["Sales"], bins=5)
plt.title("Sales Value Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

#  Scatter Plot 
plt.figure()
plt.scatter(df.index, df["Sales"])
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
