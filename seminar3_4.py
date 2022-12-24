from random import uniform


def rand_list(num):
    new_list = []
    for i in range(num):
        temp_num = round(uniform(0, 10), 2)
        new_list.append(temp_num)
    return new_list


def transform_list(my_list):
    for i in range(len(my_list)):
        my_list[i] = round(my_list[i] % 1, 2)
    return my_list


def difference_min_max(num_list):
    min_num = 1
    max_num = 0
    for i in range(len(num_list)):
        if num_list[i] > max_num:
            max_num = num_list[i]
        elif num_list[i] < min_num:
            min_num = num_list[i]
    print(f'maximum number - {max_num}\nminimum number - {min_num}')
    print(f"Difference = {max_num - min_num}")


rand_list = rand_list(int(input("Input number: ")))
print(rand_list)
result = transform_list(rand_list)
print(result)
difference_min_max(result)
