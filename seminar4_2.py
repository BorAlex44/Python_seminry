number = int(input("Input number: "))
prime_factors = []
i = 2

while i <= number:
    if number % i == 0:
        prime_factors.append(i)
        number //= i
    else:
        i += 1

print(prime_factors)
