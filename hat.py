lista=[1,2,3,4,5]
numero=int(input('Ingresa número a reemplazar en la mitad de la lista'))
lista[2]=numero
del lista[-1]
print('El largo de la lista ahora es: '+str(len(lista)),lista)