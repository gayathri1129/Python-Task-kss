import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales, profit and product data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

# Line Graph 
plt.figure()
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Product Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Bar Chart 
plt.figure()
plt.bar(df["Product"], df["Sales"])
plt.title("Product vs Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Pie Chart 
plt.figure()
plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
plt.title("Sales Contribution by Product")
plt.show()

#  Histogram
plt.figure()
plt.hist(df["Profit"], bins=5)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
