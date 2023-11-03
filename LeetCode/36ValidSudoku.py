class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [False, False, False, False, False, False, False, False, False]
        c = [False, False, False, False, False, False, False, False, False]
        b = [False, False, False, False, False, False, False, False, False]
        x = 0  # To add to number for counting sub-boxes
        y = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if j % 3 + x == 0 and j != 0:
                    y += 1

                print(board[y % 9][(j % 3) + (x % 9)])

            x += 3