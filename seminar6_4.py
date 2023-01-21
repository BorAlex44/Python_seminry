def name_second_name_dict(my_list):
    my_dict = {}
    for elem in my_list:
        name, second_name = elem.split()
        if not my_dict.get(second_name[0]):
            my_dict[second_name[0]] = {name[0]: [elem]}
        elif not my_dict[second_name[0]].get(name[0]):
            (my_dict[second_name[0]])[name[0]] = [elem]
        else:
            (my_dict[second_name[0]])[name[0]].append(elem)
    return my_dict


name_list = ["Ivan Sergeev", "Inna Serova", "Petr Alekssev", "Ilya Ivanov", "Anna Saveleva", "Juno Vetryakova",
             "Boris Arkadev", "Anton Serov", "Pavel Anisimov"]
sort_name_dict = name_second_name_dict(name_list)
print(sort_name_dict)
