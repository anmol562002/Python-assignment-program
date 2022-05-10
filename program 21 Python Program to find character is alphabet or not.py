# Python Program to find character is alphabet or not

# user input
ch = input("Insert any character: ")

# basic logic
if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print("The inserted character", ch, "is an Alphabet")
else:
    print("The inserted character", ch, "is not an Alphabet")