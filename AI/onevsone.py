board=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(board)):
    print(board[i])

def check_win(board):
    if(board[0][0] == board[1][1] == board[2][2] or
       board[0][2] == board[1][1] == board[2][0] or
       board[0][1] == board[1][1] == board[2][1] or
       board[0][0] == board[1][0] == board[2][0] or
       board[0][0] == board[0][1] == board[0][2] or
       board[1][0] == board[1][1] == board[1][2] or
       board[2][0] == board[2][1] == board[2][2] or
       board[0][2] == board[1][2] == board[2][2] or
       board[0][1] == board[1][1] == board[2][1]):
        return 1
    else:
        return 0

def human1(board):
    new_board=board
    print('Player1:')
    move=int(input("Enter the number where you want to make the move:"))
    #Searching algorithm
    for i in range (len(board)):
        for p in range(len(board)):
            if(board[i][p]==move):
                print("Number",move,'found!')
                new_board[i][p]='X'

    for i in range(len(board)):
        print(board[i])
    
    win=check_win(new_board)
    if win==1:
        print('Player1 wins!')
    else:
        #return new_board
        human2(new_board)

def human2(board):
    new_board=board
    print('Player2:')
    move=int(input("Enter the number where you want to make the move:"))
    #Searching algorithm
    for i in range (len(board)):
        for p in range(len(board)):
            if(board[i][p]==move):
                print("Number",move,'found!')
                new_board[i][p]='O'

    for i in range(len(board)):
        print(board[i])
    win=check_win(new_board)
    if win==1:
        print('Player2 wins!')
    else:
        #return new_board
        human1(new_board)

human1(board)