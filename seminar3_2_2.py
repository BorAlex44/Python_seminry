from random import sample


def list_rand_num(count: int) -> list:
    if count < 0:
        print("Negative value of the number of numbers")
        return []

    list_nums = sample(range(1, count*2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k -1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_rand_num(int(input("Number of numbers: ")))
print(all_list)
print(prod_pairs(all_list))
