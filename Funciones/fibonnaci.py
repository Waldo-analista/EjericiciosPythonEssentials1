def fibonaci(n):
    bool_n=type(n)==int and n>=1
    if bool_n==False:
        print('Ingresa numeros enteros mayor o iguales a 0')
        return ''
    else:
        if n==1:
            return 1
        if n==2:
            return 1
        else:
            return fibonaci(n-1)+fibonaci(n-2)
        
for n in range(1, 10): # testing
    print(n, "->", fibonaci(n))

print('---------------------------')
def fibonaci2(n):
    bool_n=type(n)==int and n>=1
    if bool_n==False:
        print('Ingresa numeros enteros mayor o iguales a 0')
        return ''
    else:
        if n==1 or n==2:
            return 1
        n1=1
        n2=1
        suma=0
        for i in range(3,n+1):
            suma=n1+n2
            n1,n2=n2,suma
        return suma
        
for n in range(1, 10): # testing
    print(n, "->", fibonaci2(n))
