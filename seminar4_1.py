from decimal import Decimal

number = Decimal(input("Enter a real number: "))
accuracy = input("Enter the required accuracy '0.0001': ")
print(number.quantize(Decimal(accuracy)))
