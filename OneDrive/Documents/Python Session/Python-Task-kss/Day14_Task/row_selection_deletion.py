Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> df = pd.DataFrame({
...     "A": [10, 20, 30],
...     "B": [5, 15, 25]
... }, index=["x", "y", "z"])
>>> print(df.loc["y"])
A    20
B    15
Name: y, dtype: int64
>>> df=df.drop("")
KeyboardInterrupt
>>> df=df.drop("X")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df=df.drop("X")
  File "C:\Users\admin\AppData\Roaming\Python\Python314\site-packages\pandas\core\frame.py", line 6302, in drop
    return super().drop(
  File "C:\Users\admin\AppData\Roaming\Python\Python314\site-packages\pandas\core\generic.py", line 4632, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\admin\AppData\Roaming\Python\Python314\site-packages\pandas\core\generic.py", line 4674, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\admin\AppData\Roaming\Python\Python314\site-packages\pandas\core\indexes\base.py", line 7268, in drop
    raise KeyError(f"{labels[mask].tolist()} not found in axis")
KeyError: "['X'] not found in axis"
>>> df = df.drop("x")
>>> print(df)
    A   B
y  20  15
z  30  25
