import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Product and sales data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Plot bar chart
plt.bar(df["Product"], df["Sales"])

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")

# Show graph
plt.show()
