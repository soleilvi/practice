'''
Python 3
https://leetcode.com/problems/valid-sudoku/

By Soleil Vivero
11/05/2023
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [False, False, False, False, False, False, False, False, False]
        c = [False, False, False, False, False, False, False, False, False]
        b = [False, False, False, False, False, False, False, False, False]
        x = 0  # For counting sub-boxes, add to j
        y = 0  # For counting sub-boxes, column place

        for i in range(9):

            # Mark if a number has already appeared in the current row,
            # column, or sub-block. If it has, return False.
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    y += 1

                # Rows
                if board[i][j] != '.':
                    if r[int(board[i][j]) - 1] == True:
                        return False
                    r[int(board[i][j]) - 1] = True

                # Columns
                if board[j][i] != '.':
                    if c[int(board[j][i]) - 1] == True:
                        return False
                    c[int(board[j][i]) - 1] = True
                
                # Sub-block
                if board[y][(j % 3) + (x % 9)] != '.':
                    if b[int(board[y][(j % 3) + (x % 9)]) - 1] == True:
                        return False
                    b[int(board[y][(j % 3) + (x % 9)]) - 1] = True

            # Reset list values
            for k in range(9):
                c[k] = False
                r[k] = False
                b[k] = False

            x += 3
            
            if i < 2:
                y = 0
            elif i < 5:
                y = 3
            else:
                y = 6

        return True
    
'''
After watching a video with another solution, here is what I learned:
- Instead of the x and y variables, I could have simply divided each
  index number by 3, which would have simulated a 3x3 board instead of
  a 9x9 board. This way, i could have taken each sub-box as if it were
  a cell in a 3x3 2D array. This implementation would require me to
  use a dictionary of sets.
- Using set dictionaries would have made things more readable
- The lookup time for a set is O(1), as they implement a hash table
  lookup algorithm
'''