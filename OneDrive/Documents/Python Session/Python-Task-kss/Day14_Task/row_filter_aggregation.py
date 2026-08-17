Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> import pandas as pd
>>> arr = np.array([
...     [100, 200],
...     [150, 250],
...     [80, 120],
...     [300, 400]
... ])
>>> df = pd.DataFrame(arr, columns=["Sales", "Profit"])
>>> filtered = df[df["Sales"] > 100]
>>> average_profit = filtered["Profit"].mean()
>>> print(filtered)
   Sales  Profit
1    150     250
3    300     400
>>> print("Average Profit:", average_profit)
Average Profit: 325.0
