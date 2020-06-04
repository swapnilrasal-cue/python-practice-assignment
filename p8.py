print("Hello User 1")        
print("Hello User 2")

user1_input = input("what will you choose 'User1' rock , paper & scissors :")
user2_input = input("what will you choose 'User2' rock , paper & scissors :")        
        
def game(user1_input,user2_input):
    if user1_input == user2_input:
        print("Game is Tie")
    
    elif user1_input == 'rock':
        if user2_input == 'scissors':
            print("Winner is User1")
        elif user2_input == 'paper':
            print("Winner is User2")
            
    elif user1_input == 'paper':
        if user2_input == 'rock':
            print("Winner is User1")
        elif user2_input == 'scissors':
            print("Winner is User2")
    
    elif user1_input == 'scissors':
        if user2_input == 'paper':
            print("Winner is User1")
        elif user2_input == 'rock':
            print("Winner is User2")
    
    else:
        print("please choose valid option :")    
    
game(user1_input,user2_input)