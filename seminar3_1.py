from random import sample


def rand_list(num):
    new_list = sample(range(1, (num+1)*2), k=num)
    print(new_list)
    sum_num = 0
    for i in range(0, len(new_list), 2):
        sum_num += new_list[i]
    print(sum_num)


rand_list(int(input("Введите число: ")))
