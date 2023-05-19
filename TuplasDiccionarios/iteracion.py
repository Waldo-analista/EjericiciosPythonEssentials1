dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']#'two'
 
for k in range(len(dictionary)):
    v = dictionary[v]#v='three'

'''
v='two'
0  v=dictionary['two']='three'
1  v=dictionary['three']='one'
2  v=dictionary['one']='two'


'''


print(v)