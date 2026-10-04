weight = float(input('Enter weight(kg):'))
height = float(input('Enter height(m):'))
bmi = weight/height**2
if bmi < 18.5:
    print('Category: Underweight')
elif 18.5<bmi<25:
    print('Category: Normal')
elif 25<bmi<30:
    print('Category: Overwight')
else:
    print('Category: Obese')
print(f'BMI: {bmi:.1f}')