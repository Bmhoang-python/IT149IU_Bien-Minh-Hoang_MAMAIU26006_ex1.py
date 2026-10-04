total_seconds = int(input("Enter seconds (>3600): "))
while total_seconds < 3600:
    total_seconds = int(input("Enter a number greater than 3600: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
check = hours * 3600 + minutes * 60 + seconds
print("check:", check== total_seconds)

