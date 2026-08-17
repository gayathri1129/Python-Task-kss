Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> temps = np.array([28, 31, 35, 27, 40, 22])
>>> high_temps = temps[temps > 30]
>>> print("Temperatures above 30°C:", high_temps)
Temperatures above 30°C: [31 35 40]
