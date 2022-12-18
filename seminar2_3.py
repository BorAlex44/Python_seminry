n = int(input("Введите число: "))
num_list = []
for n in range(1, n + 1):
    num_list.append(round((1 + 1/n) ** n, 3))
print(num_list)
