d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    for elemento in item:
        d3[elemento]=item[elemento]
 
print(d3)