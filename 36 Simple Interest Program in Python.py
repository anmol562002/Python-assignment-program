# Python program to calculate simple interest

# store the inputs
P = float(input('Enter principal amount: '))
R = float(input('Enter the interest rate: '))
T = float(input('Enter time: '))

# calculate simple interest
SI = (P * R * T) / 100

# display result
print('Simple interest = ',SI )
print('Total amount = ',( P + SI ))