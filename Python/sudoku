import random


# Generate an empty board
board = [['' for _ in range(9)] for _ in range(9)]

def get_square_number(line, column):
  ''' Get the square number for a given cell. Squares are numbered from 0 to 8, from left to right and top to bottom. '''

  return (3*(line//3)) + (column//3)

def get_square(square_number):
  ''' Get the cells for a given square number, as a list. The cells are ordered from left to right and top to bottom. '''

  line_start = 3 * (square_number//3)
  column_start = 3 * (square_number%3)
  
  # Extract the cells from the board and concatenate them to form the square
  return board[line_start][column_start:column_start+3] + \
         board[line_start+1][column_start:column_start+3] + \
         board[line_start+2][column_start:column_start+3]

def get_column(column):
  ''' Get the values for a given column as a list. The values are ordered from top to bottom. '''

  return [board[row][column] for row in range(len(board))]

def get_valid_numbers(line=0, column=0):
  ''' Get a list of valid numbers that can be placed in a given cell. '''

  # The valid numbers are those that don't appear in the cell's row, column or square
  return [x for x in range(1, 10) if x not in get_column(column) and \
          x not in get_square(get_square_number(line, column)) and x not in board[line]]

def recursive_fill(line=0, column=0):
  ''' Recursively fill the board with valid numbers. '''

  valid_numbers = get_valid_numbers(line, column)
  random.shuffle(valid_numbers)

  # If there are no valid numbers, return False to indicate that the current path doesn't lead to a solution
  if valid_numbers == []:
    return False

  # Try each valid number in a random order until a solution is found
  while valid_numbers:
    number = valid_numbers.pop(0)
    board[line][column] = number

    # If this is the last cell, we have found a solution and can stop searching
    if line == 8 and column == 8:
      return True

    # Otherwise, move to the next cell and continue the search
    next_line, next_column = (line, column + 1) if column != 8 else (line + 1, 0)
    if recursive_fill(next_line, next_column):
      return True

  # If none of the valid numbers led to a solution, backtrack and try again
  board[line][column] = ''
  return False

# Fill the board recursively and print the result
recursive_fill()
for line in board:
  print(line)

