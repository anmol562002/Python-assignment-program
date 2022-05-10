# Python program to print fibonacci series up to n-th term

# take input
num = int(input('Enter number of terms: '))

# print fibonacci series
a, b = 0, 1
i = 0
    
# check if the number of terms is valid
if num <= 0:
    print('Please enter a positive integer.')

elif num == 1:
    print('The Fibonacci series: ')
    print(a)

else:
    print('The Fibonacci series: ')
    while i < num:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        i = i+1