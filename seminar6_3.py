def name_dict(my_list):
    my_dict = {}
    for elem in my_list:
        key = elem[0].capitalize()
        my_dict.setdefault(key, []).append(elem)
    return dict(sorted(my_dict.items()))


name_list = ["Ivan", "Mariya", "Petr", "Ilya", "Marina", "Pasha", "Alina", "Boris"]
sort_name_dict = name_dict(name_list)
print(sort_name_dict)
