beatles=list()
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
for i in range(0,2):
    name=input('Ingresa nombre de Beatle a anexar a la lista')
    beatles.append(name)
del beatles[-1]
del beatles[-1]
beatles.insert(0,'Ringo Starr')
print(beatles)