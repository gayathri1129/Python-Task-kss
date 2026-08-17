Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> Missing City Data (NaN Handling)A dataset contains city populations:cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}Scenario:You want data fo["Delhi", "Chennai", "Bangalore"TaskCreate a Series with the above index]● Identify which cities have missing values (NaN)
SyntaxError: invalid character '●' (U+25CF)
>>> import pandas as pd
>>> 
>>> cities={"delhi":2000000,"mumbai":3000000,"chennai":1500000}
>>> city_list=["delhi","chennai","bangalore"]
>>> pop=pd.Series(cities,index=city_list)
>>> print(pop)
delhi        2000000.0
chennai      1500000.0
bangalore          NaN
dtype: float64
>>> miss=pop[pop.isna()]
>>> print(miss)
bangalore   NaN
dtype: float64
