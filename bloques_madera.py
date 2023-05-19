blocks = int(input("Enter the number of blocks: "))


for i in range(1,999999999):
    if blocks>=i:
        height=i
        blocks-=i
    else:
        height=i-1
        break


print("The height of the pyramid:", height)