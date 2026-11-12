
class Solution:
    def solveNQueens(self, n):
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                safe = True

                for i in range(row):
                    if board[i][col] == 'Q':
                        safe = False

                    if abs(row - i) == abs(col - (board[i].index('Q'))):
                        safe = False

                if safe:
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return result
