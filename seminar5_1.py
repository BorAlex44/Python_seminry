import random


def random_list(num):
    rand_list = [("".join(random.sample('abc', 3))) for _ in range(num)]
    return rand_list


def find_word(new_list):
    find_list = [(new_list[i]) for i in range(len(new_list)) if new_list[i] != 'abc']
    return find_list


my_num = int(input("enter the number of words: "))
my_list = random_list(my_num)
print(my_list)
filter_list = find_word(my_list)
print(list(filter_list))
