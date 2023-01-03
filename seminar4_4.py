import random


def create_file(new_str):
    with open('seminar4.txt', 'a') as data:
        data.write(f'{new_str}\n')


def create_rand_list(num):
    rand_list = []
    for i in range(num+1):
        rand_list.append(random.randint(0, 9))

    return rand_list


def list_polynom(my_list):
    new_str = ''
    seq = '+-'
    if len(my_list) < 1:
        new_str += 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                new_str += f'{my_list[i]}*x^{len(my_list) - i - 1}'
                if my_list[i + 1] != 0:
                    new_str += ' ' + random.choice(seq) + ' '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                new_str += f'{my_list[i]}*x^1'
                if my_list[i + 1] != 0:
                    new_str += ' ' + random.choice(seq) + ' '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                new_str += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                new_str += ' = 0'
            else:
                if my_list[i] == 0 and i == 0:
                    new_str += ''
                elif my_list[i] == 0:
                    if my_list[i+1] != 0:
                        new_str += ' ' + random.choice(seq) + ' '
                else:
                    new_str += ''

    return new_str


k = int(input("Set the natural degree k: "))
res = create_rand_list(k)
print(res)
my_str = list_polynom(res)
print(my_str)
create_file(my_str)
