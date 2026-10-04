def score(name):
    total = 0

    for char in name:
        total += ord(char)
    return total
names = input("Enter names separated by commas: ").split(",")
names = [name.strip() for name in names]
print(f"nScores:")
for name in names:
    print(f"{name}: {score(name)}")
def winner(names_list):
    return max(names_list, key=score)
winning_name = winner(names)
print(f"\nThe winner is: {winning_name}")
print(f"Highest score: {score(winning_name)}")