eggs = int(input('Enter number of eggs:'))
per_box = int(input('Enter eggs of per box:'))
boxes = eggs // per_box
remaining_eggs = eggs % per_box
print(f"nNumber of boxes: {boxes}")
print(f"Remaining eggs: {remaining_eggs}")
print("nBoxes:")
for i in range(boxes):
    print('+------+')
    print('|   o  |')
    print('+------+')
if remaining_eggs > 0:
    print(f"\nRemaining eggs: {'O ' * remaining_eggs}")
