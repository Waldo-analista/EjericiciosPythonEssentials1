def is_prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True
        
        

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()