import random
board=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(board)):
    print(board[i])



def human(board):
    new_board=board
    move=int(input("Enter the number where you want to make the move:"))
    #Searching algorithm
    for i in range (len(board)):
        for p in range(len(board)):
            if(board[i][p]==move):
                print("Number",move,'found!')
                new_board[i][p]='X'

    #return new_board
    robot(new_board)


def robot(new_board):
    new_board2=new_board
    move=random.randint(1,9)
    print('Robot chooses',move)
    #Searching
    for i in range (len(board)):
        for p in range(len(board)):
            if(new_board2[i][p]==move):
                print("Number",move,'found!')
                new_board2[i][p]='O'
                move_index=[i]
                move_index2=[p]
            else:
                print('Not found current is',new_board2[i][p])
    print(move_index)
    print('move index 2=',move_index2)

    # if move!=board.index(move_index):
    #     robot(new_board)
    print(new_board2)


human(board)