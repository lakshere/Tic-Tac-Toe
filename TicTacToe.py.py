#Tic Tac Toe Game

#create board
board=["" for x in range(9)]

#define board
def printboard():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
#define player moves
def playermove(icon):
    if icon=="X":
        number=1 
    if icon=="O":
        number=2 
    print("Your turn, player {}".format(number))
    choice=int(input("Enter your move(1-9):").strip())
    if board[choice-1]=="":
        board[choice-1]=icon
    else:
        print()
        print("That space is taken!Choose again!")
        return playermove(icon)
        
#check for victory
def isvictory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
          return True
    else:
        return False
        
#check for draw
def isdraw():
    if "" not in board:
        return True
    else:
        return False 
        
while True:
    printboard()
    playermove("X")
    printboard()
    
    if isvictory("X"):
        print("X wins! Congratulations!")
        break
    
    elif isdraw():
        print("It's a draw!")
        break
    
    playermove("O")
    if isvictory("O"):
        print("O wins! Congratulations!")
        break
    
    elif isdraw():
        print("It's a draw!")
        break