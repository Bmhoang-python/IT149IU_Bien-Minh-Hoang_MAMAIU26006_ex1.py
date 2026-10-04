A = float(input('running 1 time:'))
B = float(input('running 2 time:'))
C = float(input('running 3 time:'))

if A <= B and A < C:
    print('Running 1 won')
elif B <= A and B < C:
    print('Running 2 won')
elif C <= A and C < B:
    print('Running 3 won')
else:
    print('There is a tie')