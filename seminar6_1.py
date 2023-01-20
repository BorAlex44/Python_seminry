from random import sample


def random_list(num):
    return [i for i in sample(range(1, 20), num)]


def sort_list(unsort_list):
    return [unsort_list[i] for i in range(1, len(unsort_list)) if unsort_list[i] > unsort_list[i-1]]


my_list = random_list(int(input("Enter the length of the list: ")))
print(my_list)
print(sort_list(my_list))
