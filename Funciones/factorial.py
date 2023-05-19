def factorial(n):
    bool_n=type(n)==int and n>=0
    if bool_n==False:
        print('Ingresa numeros enteros mayor o iguales a 0')
        return ''
    else:
        if n==0:
            return 1
        else:
            return n*factorial(n-1)

for n in range(1, 6): # testing
    print(n, factorial(n))