number = int(input('Enter a three-digit number:'))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
sum_digits = hundreds + tens + units
reversed_number = units * 100 + tens * 10 + hundreds
print('Hundreds:', hundreds)
print('Tens:', tens)
print('Units:', units)
print('Sum of digits:', sum_digits)
print('Reversed number:', reversed_number)
if number ==reversed_number:
    print('The number is a palindrome.')
else:
    print('NOT a palindrome.')
    