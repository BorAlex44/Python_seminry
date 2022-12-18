num = int(input("Введите число: "))
pos_1 = int(input("Введите позицию 1: "))
pos_2 = int(input("Введите позицию 2: "))
num_list = []
for i in range(-num, num+1):
    num_list.append(i)
print(num_list)
if pos_1 > (num*2+1) or pos_2 > (num*2+1):
    print("Ошибка!!!!! Одна из позиций превышает длину списка")
else:
    result = (num_list[pos_1-1])*(num_list[pos_2-1])
    print(result)
