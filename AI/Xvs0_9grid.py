board=[[[1,2,3],[4,5,6],[7,8,9]],
       [[10,11,12],[13,14,15],[16,17,18]],
       [[19,20,21],[22,23,24],[25,26,27]],
       [[28,29,30],[31,32,33],[34,35,36]],
       [[37,38,39],[40,41,42],[43,44,45]],
       [[46,47,48],[49,50,51],[52,53,54]],
       [[55,56,57],[57,58,59],[60,61,62]],
       [[63,64,65],[66,67,68],[69,70,71]],
       [[72,73,74],[75,76,77],[78,79,80]]]

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
    for i in range (9):
        for p in range(3):
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
    for i in range (9):
        for p in range(3):
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