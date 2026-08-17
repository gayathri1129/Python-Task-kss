Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
>>> data=np.random.rand(8)
>>> print(data)
[0.04738874 0.2618927  0.23875083 0.66868288 0.52185328 0.40964418
 0.93728973 0.48869631]
>>> data=data*100
>>> print(data)
[ 4.73887379 26.18927013 23.87508318 66.8682883  52.18532849 40.96441835
 93.72897305 48.8696307 ]
>>> filtered=data[data>50]
>>> sorted_values=np.sort(filtered)
>>> print(sorted_values)
[52.18532849 66.8682883  93.72897305]
