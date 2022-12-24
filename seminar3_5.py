def fibonacci_func(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci_func(n-1) + fibonacci_func(n-2)


def negafibonacci_func(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


fibonacci_list = [0]
userNumber = int(input('Enter any number: '))
for i in range(1, userNumber + 1):
    fibonacci_list.append(fibonacci_func(i))
    fibonacci_list.insert(0, negafibonacci_func(i))
print(fibonacci_list)
