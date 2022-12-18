num = int(input('Введите число: '))
new_num = 1
for i in range(1, num+1):
    new_num = i*new_num
    print(new_num, end=' ')
