
class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def solve(pos):
            if pos == len(empty):
                return True

            best = pos
            best_options = None

            for k in range(pos, len(empty)):
                i, j = empty[k]
                b = (i // 3) * 3 + j // 3

                options = [
                    num for num in '123456789'
                    if num not in rows[i]
                    and num not in cols[j]
                    and num not in boxes[b]
                ]

                if best_options is None or len(options) < len(best_options):
                    best = k
                    best_options = options

                if len(best_options) == 0:
                    return False

            empty[pos], empty[best] = empty[best], empty[pos]

            i, j = empty[pos]
            b = (i // 3) * 3 + j // 3

            for num in best_options:
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[b].add(num)

                if solve(pos + 1):
                    return True

                board[i][j] = '.'
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[b].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        solve(0)
