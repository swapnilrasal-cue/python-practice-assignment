import sys

def createMatrix(input_list):
    matrix = []
    try:
        for i in range(int(input_list[0])):
            row = []
            for j in range(int(input_list[1])):
                value = i * j
                row.append(value)
            matrix.append(row)   
            # print(matrix,end=',')
    except:
        print("Please Enter Integers Only")
        sys.exit(1)

    else:
        print("Successfully Completed")
        
    print(matrix)
    
user_input = str(input("Enter Number of Rows And Columns :"))
input_list = user_input.split (",")
createMatrix(input_list)