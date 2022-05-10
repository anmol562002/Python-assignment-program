#Python Program for Calculating the length of string Without using length() function
#take user input
string = input('Enter the String :')
#initialize count variable
count = 0
#i is the iterator
#iterates through every element of string
for i in string:
    #increment in count variable 
    #to find number of iterators in string
    count+=1
print(count)