def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

'''
El codigo muestra:
Print 1: [2,3]
Print 2: [2,3]
Print 3: [0,1]
Print 4: [2,3]
Print 5: [2,3]

'''






def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


'''
El codigo imprime:
Print 1: [2, 3]
Print 2: [2, 3]
Print 3: [3]
Print 4: [3]
Print 5: [3]




'''