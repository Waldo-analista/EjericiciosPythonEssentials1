my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=[]

for i in range(len(my_list)): 
    auxiliar=my_list[:]
    del auxiliar[i]
    if my_list[i] not in auxiliar:
        new_list.append(my_list[i])
    auxiliar.insert(i,my_list[i])
my_list=new_list

print("The list with unique elements only:")
print(my_list)
