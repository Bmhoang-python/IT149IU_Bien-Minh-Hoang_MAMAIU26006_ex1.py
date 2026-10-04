import matplotlib.pyplot as plt

max_hour = int(input("Enter the maximum hour: "))
step = int(input("Enter step size: "))

hour_list = []
bacteria = []

for hour in range(0, max_hour + 1, step):
    population = 100 * (2 ** hour)

    print(f"Hour: {hour:2}, {population}")

    hour_list.append(hour)
    bacteria.append(population)
    
plt.plot(hour_list, bacteria, marker='o')
plt.xlabel('Hour')
plt.ylabel('Number of Bacteria')
plt.title('Bacteria Growth Curve')
plt.grid(True)
plt.show()