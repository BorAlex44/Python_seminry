number = float(input("Введите любое дробное число: "))
sum_numbers = 0
n = len(str(number))
number = int(number*10**(n-2))
while number != 0:
    sum_numbers = sum_numbers + number % 10
    number = number // 10
print(f"Сумма цифр числа равна {sum_numbers}")


