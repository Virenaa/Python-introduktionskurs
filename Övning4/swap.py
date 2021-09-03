def swap(list):
    if len(list) % 2 == 0:
        half=int(len(list)/2)
        A=list[:half]
        B=list[half:]
        add=B+A
        return add

print(swap([1,2,3,4])) 


