for hour in range(1, 10):
    bacteria = 100*2**hour
    print(f"{hour:>8} | {bacteria:>15}")

max_hour = int(input("Enter the maximum hour: "))
print(f"{'Hour':>8} | {'Bacteria':>15}")
print("-" * 26)
for hour in range(max_hour + 1): 
    bacteria = 100*2**hour
    print(f"{hour:>8} | {bacteria:>15}")

import pandas as pd 
max_hour = int(input("Enter the maximum hour: "))
data = []
for hour in range(max_hour + 1):
    bacteria = 100*2**hour
    data.append({'Hour': hour, 'Bacteria': bacteria})
df = pd.DataFrame(data)
print(df)
df.to_csv('bacteria_growth.csv', index=False)
print("CSV file created!")
df.to_excel('bacteria_growth.xlsx', index=False)