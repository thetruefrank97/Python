import random

list1 = []
for i in range(20):
    list1.append(random.randint(1, 200))
print(list)

# More ranges
list2 = []
input = 10
for i in range(20):
    list2.append(input)
    input += 10
print(list2)

# removing duplicates
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

