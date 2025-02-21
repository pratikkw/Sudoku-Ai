# Fixing the Sudoku

def fixing(board, row, col, num):
  # Check row
  for i in range(9):
    if(i == col):
      continue
    if(board[row][i] == num):
      board[row][i] = 0

  # Check column
  for i in range(9):
    if(i == row):
      continue
    if(board[i][col] == num):
      board[i][col] = 0

    
  # Check For 3 X 3 block
  start_row, start_col = (row // 3)*3, (col//3)*3
  
  for r in range(start_row, start_row + 3):
    for c in range(start_col, start_col + 3):
      if(r == row and c == col):
        continue
      if(board[r][c] == num):
        board[r][c] = 0

def check_sudoku(board):
  for i in range(9):
    for j in range(9):
      if(board[i][j] != 0):
        fixing(board, i, j, board[i][j])

  return board

def is_valid(board, row, col, num):
  # Check row
  if(num in board[row]):
    return False
  
  # Check column
  if(num in (board[i][col] for i in range(9))):
    return False
  
  # Check 3 X 3 block
  start_row, start_col = (row // 3)*3, (col // 3)*3

  for i in range(start_row, start_row + 3):
    for j in range(start_col, start_col + 3):
      if(board[i][j] == num):
        return False
      
  return True

def solver(board):
  board = check_sudoku(board)
  for r in range(9):
    for c in range(9):
      if(board[r][c] == 0):
        for num in range(1, 10):
          if(is_valid(board, r, c, num)):
            board[r][c] = num
            
            if(solver(board)):
              return True
            
            board[r][c] = 0
        return False
  return board

sudoku_board = [
 [3, 4, 0, 0, 6, 0, 2, 0, 9],
 [2, 0, 8, 4, 9, 0, 0, 0, 6],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 2, 0, 3, 1, 0, 0, 0, 0],
 [0, 0, 4, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 2, 5, 0, 4, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [9, 0, 0, 0, 5, 1, 4, 0, 3],
 [4, 0, 3, 0, 7, 0, 0, 6, 8]
 ]

print(solver(sudoku_board))

for i in sudoku_board:
  print(i)

