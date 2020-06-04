#using sets
def RemoveDuplicate(a):
    b = set(a) 
    print("Using SET : ",b)

#without using set
def RemoveDuplicateWithoutSet(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i) 
    print("Without Using SET : ",b)


list_a = [1,2,3,4,5,6,1,2,3]
RemoveDuplicate(list_a)
RemoveDuplicateWithoutSet(list_a)