number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
numero_mas_grande=number1
if number2>numero_mas_grande:
    numero_mas_grande=number2
if number3>numero_mas_grande:
    numero_mas_grande=number3
print(numero_mas_grande)