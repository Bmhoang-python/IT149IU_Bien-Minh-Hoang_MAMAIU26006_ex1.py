import matplotlib.pyplot as plt
o = float(input("Enter original wage:"))
reviews = input("Enter reviews:").split(",")
wage = o
wages = [wage]
for review in reviews:
    review = review.strip()
    if review == "good":
        wage *= 1.03
    elif review == "bad":
        wage *= 0.97
    wages.append(wage)
print("Final wage:", wage)
plt.plot(range(len(wages)), wages)
plt.xlabel("Year")
plt.ylabel("Wage")
plt.title("The Wage Growth")
plt.show()