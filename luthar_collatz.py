c0=int(input('Ingresa un numero entero'))
contador=0
while c0!=1 and c0>=1:
    if c0%2==0:
        c0=c0/2
    else:
        c0=3*c0+1
    contador+=1
    print(c0)
print('El numero de pasos para llegar a 1 fue de:'+str(contador))
