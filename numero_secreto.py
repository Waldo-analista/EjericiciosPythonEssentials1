secret_number = 777

print(
'''
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
''')

numero=int(input('Ingresa un numero entero'))

while numero!=secret_number:
    print('Ha ha! You\'re stuck in my loop!')
    numero=int(input('Ingresa un numero entero'))
print(f'Has adivinado el número secreto que es:{numero}')
print('Well done, muggle! You are free now.')