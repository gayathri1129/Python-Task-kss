import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Temperature data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

# Line Graph 
plt.figure()
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

# Bar Chart
plt.figure()
plt.bar(df["Day"], df["Temperature"])
plt.title("Day-wise Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

#  Pie Chart 
high_count = (temps > 30).sum()
low_count = (temps <= 30).sum()

plt.figure()
plt.pie(
    [high_count, low_count],
    labels=["High (>30)", "Low (<=30)"],
    autopct="%1.1f%%"
)
plt.title("High vs Low Temperature")
plt.show()

#  Histogram 
plt.figure()
plt.hist(df["Temperature"], bins=5)
plt.title("Temperature Frequency")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot 
plt.figure()
plt.scatter(df.index, df["Temperature"])
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")
plt.show()
