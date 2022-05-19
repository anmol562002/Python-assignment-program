from collections import Counter
a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2,2]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:1 , 6:1}
print(c.subtract(sub))
print(c.most_common())