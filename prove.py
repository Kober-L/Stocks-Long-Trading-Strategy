import pandas as pd

#create an ascending series

asc = {}
first = 100
i = 1
asc[i] = first

for i in range(3000):
  i += 1
  second = first + ((first / 100) * 5.2)
  asc[i] = second
  first = second

ser = pd.Series(data=asc, index=list(asc.keys()))
print(ser)