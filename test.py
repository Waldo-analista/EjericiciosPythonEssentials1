'''lista=[1,2,7,8,5]
def show(lista):
    contador=0
    while contador<len(lista):
        if lista[contador]==8:
            return lista[contador]
        contador+=1
    return lista    
        
print(show(lista))
'''
n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")
