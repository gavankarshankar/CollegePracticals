import random
import pandas as pd
import numpy as np

board=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(board)



def toss(choice):
    heads=1
    tails=0
    coin=random.randint(0,1)
    if coin==1 and choice == 'heads':
        print("It's heads")
        print('You have won! Make your first move.')
    if coin==0 and choice == 'tails':
        print("It's tails")
        print('You have won! Make your first move.')
    else:
        print("Computer has won the toss,it will make it's first move.")


#x=input("heads or tails:")
#toss(x)
    

def robot(current_board):
    number=random.randint(1,9)
    print('Computer chooses',number)
    indices = (current_board == number).any() #using any to find index positions
    boolean=(indices == True).any()
    if(boolean == True):
        new_board=current_board.replace(number,'O')
        print(new_board)
        print("\n")
        win_or_lose(current_board)
        human(new_board)
    else:
        numbers=[1,2,3,4,5,6,7,8,9]

        print(all(i in numbers for i in current_board))
                #end()

        robot(current_board)
        

def human(current_board):
    number=int(input("Enter number to make your move:"))
    new_board=current_board.replace(number,'X')
    print(new_board)
    print("\n")
    win_or_lose(current_board)
    robot(new_board)

def end():
    print("Game over")

def win_or_lose(current_board):
    if(current_board[0][0]==current_board[1][0]==current_board[2][0]=='X'
       or current_board[0][1]==current_board[1][1]==current_board[2][1]=='X'
       or current_board[0][2]==current_board[1][2]==current_board[2][2]=='X'
       or current_board[0][0]==current_board[0][1]==current_board[0][2]=='X'
       or current_board[1][0]==current_board[1][1]==current_board[1][2]=='X'
       or current_board[2][0]==current_board[2][1]==current_board[2][2]=='X'
       or current_board[0][0]==current_board[1][1]==current_board[2][2]=='X'
       or current_board[2][0]==current_board[1][1]==current_board[0][2]=='X'):
        print('X wins!')
        end()
        return None
    if(current_board[0][0]==current_board[1][0]==current_board[2][0]=='O'
       or current_board[0][1]==current_board[1][1]==current_board[2][1]=='O'
       or current_board[0][2]==current_board[1][2]==current_board[2][2]=='O'
       or current_board[0][0]==current_board[0][1]==current_board[0][2]=='O'
       or current_board[1][0]==current_board[1][1]==current_board[1][2]=='O'
       or current_board[2][0]==current_board[2][1]==current_board[2][2]=='O'
       or current_board[0][0]==current_board[1][1]==current_board[2][2]=='O'
       or current_board[2][0]==current_board[1][1]==current_board[0][2]=='O'):
        print('O wins!')
        end()
    else:
        return
    

human(board)
# for i in range(0,3):
#     print(board[i][2])
    
# numbers=[1,2,3,4,5,6,7,8,9]
# print(all(i in numbers for i in board))


# for col in board:
#     print(col)



  
# indices = np.where(board == 15)
# print(indices)
# # Extracting row and column indices
# row_indices, col_indices = indices[0], indices[1]
# print(row_indices, col_indices)
# # if(board[row_indices][col_indices]!='X'):
# #     print(board.replac)
