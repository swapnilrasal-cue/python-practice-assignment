def drawHorizontalLine():
    print (" --- " * user_input)

def drawVerticalLine():
    print ("|    " * (user_input + 1))
    
if __name__ == "__main__":
    user_input = int(input("board size : "))

            
for i in range(user_input):
    drawHorizontalLine()
    drawVerticalLine()

drawHorizontalLine()
    
