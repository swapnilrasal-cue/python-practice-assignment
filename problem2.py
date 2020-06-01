str = str(input("Enter Number of Rows And Columns "))
list = str.split (",")

# print(list[0])
# print(list[1])
matrix = []
for i in range(int(list[0])):
    row = []
    for j in range(int(list[1])):
        value = i * j
        row.append(value)
    
    matrix.append(row)   
    # print(matrix,end=',')
print(matrix)