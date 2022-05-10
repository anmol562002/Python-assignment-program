# Python program to find compound interest

# store the inputs
principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times t nterest is compounded per year: '))

# convert rate
rate = rate/100

# calculate total amount
amount = principal * pow( 1+(rate/number), number*time)
# calculate compound interest
ci = amount - principal

# display result
print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)