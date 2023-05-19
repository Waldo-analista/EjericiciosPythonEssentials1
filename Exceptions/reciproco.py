try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('Has ingresado un caracter no numerico o un numero no entero')
except ZeroDivisionError:
    print('Has ingresado un numero que no tiene reciproco')
except KeyboardInterrupt:
    print('Interrupcion de teclado')