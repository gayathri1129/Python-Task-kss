import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print(df)

# Plot bar graph
plt.bar(df["Name"], df["Marks"])

# Add labels
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

# Show graph
plt.show()
