from random import sample


def prod_num(num):
    new_list = sample(range(1, num+1), k=num)
    print(new_list)
    i = 0
    prod_list = []
    if num % 2 != 0:
        while i < int(num/2):
            prod = new_list[i] * new_list[num - 1 - i]
            prod_list.append(prod)
            i += 1
        prod_list.append(new_list[int(num/2)])
    else:
        while i < int(num/2):
            prod = new_list[i] * new_list[num - 1 - i]
            prod_list.append(prod)
            i += 1
    print(prod_list)


prod_num(int(input("Введите число: ")))
