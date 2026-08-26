import numpy as np
import matplotlib.pyplot as plt

# Expense data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create pie chart
plt.pie(
    expenses,
    labels=labels,
    autopct="%1.1f%%"
)

# Add title
plt.title("Monthly Expense Distribution")

# Show graph
plt.show()
