import numpy as np 
height = 7
width = 6

def displayBoard(): # to display board 
   board = np.zeros((width, height))
   return board
 
isGameOver = False   # to keep the game running
turns = 0

board = displayBoard()
print(board)

# Checking if the top of the board is empty or not
def IsEmpty(board,col):
   return board[5][col] == 0

def getOpenRow(board, col):
   for r in range(width):
      if board[r][col] == 0:
         return r

def putPiece(board, row, col, piece):
   board[row][col] = piece

while not isGameOver:
   if turns == 0: 
         choice = int(input("Player 1, What column do you want to put your piece?"))
         if IsEmpty(board, choice):
            row = getOpenRow(board, choice)
            putPiece(board, row, choice, 1)  

   else:
         choice = int(input("Player 2, What column do you want to put your piece?"))
         if IsEmpty(board, choice):
            row = getOpenRow(board, choice)
            putPiece(board, row, choice, 2)  
            
   
   print(board)
   turns += 1
   turns = turns%2 


