x= int(input("Enter a number between 1 and 10: "))
if x<1 or x>10:
    print("Error: The number is out of range")
else:
    for x in range(1,x+1):
     print(x, "squared is", x**2)
