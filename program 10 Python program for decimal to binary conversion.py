#Python program for decimal to binary conversion anmol jain
def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")


decimal_num = 21
convertBinary(decimal_num)