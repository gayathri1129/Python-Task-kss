import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Temperature data
temps = np.array([28, 30, 32, 31, 29])

# Convert into Pandas Series
temperature = pd.Series(temps)

print(temperature)

# Plot line graph
plt.plot(temperature, marker="o")

# Add title
plt.title("Daily Temperature Trend")

# Add grid
plt.grid()

# Add labels
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

# Show graph
plt.show()
