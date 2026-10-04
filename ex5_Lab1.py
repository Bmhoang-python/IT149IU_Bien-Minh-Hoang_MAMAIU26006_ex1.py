for i in range(1, 11):
    if i % 2 == 0:
        print(f"if i= {i}, {i} is even")
    else: 
        print(f"if i= {i}, {i} is odd")

import pandas as pd
df = pd.DataFrame({'Name':["A", "B", "C", "D", "E"], 'score':[8, 9, 7, 6, 10]})
print("Original DataFrame:")
print(df)

print("\nEven index :")
print(df[df.index % 2 == 0])

print("\nOdd index :")
print(df[df.index % 2 == 0])
