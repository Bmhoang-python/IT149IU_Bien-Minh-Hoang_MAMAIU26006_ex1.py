y=-5
print("-5/2=", y/2)
print("-5//2=", y//2)

x = 49
print("Square root of 49 =", x**0.5)

print(f"{'Number' :<10}{'Square' :<10}{'Square root' :<15}")
for i in range(1,6):
    print(f"{i:<10}{i**2:<10}{i**0.5:<15.2f}")
