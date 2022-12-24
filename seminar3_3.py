def convert_binary(num):
    bin_list = []
    while num > 0:
        temp = num % 2
        num = num // 2
        bin_list.append(temp)
    bin_list.reverse()
    number = int(''.join(map(str, bin_list)))
    print(number)


convert_binary(int(input("Введите число: ")))
