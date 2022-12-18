import random

num = int(input("Введите число: "))
num_list = []
rand_list = []
j = 0
for i in range(num):
    num_list.append(i)
print(num_list)
while j < num:
    temp_num = random.choice(num_list)
    rand_list.append(temp_num)
    num_list.pop(num_list.index(temp_num))
    j += 1
print(rand_list)
