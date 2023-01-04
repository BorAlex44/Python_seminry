import random
from collections import Counter

count = int(input("Enter the length of the list: "))
num_list = [random.randrange(1, 10, 1) for i in range(count)]
print(num_list)
new_list = (Counter(num_list))
only_elem = []
for item in new_list.items():
    if item[1] == 1:
        only_elem.append(item[0])
print(only_elem)
