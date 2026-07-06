class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        board = [["." for _ in range(n)] for _ in range(n)]

        col = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for c in range(n):
                if c in col or (row - c) in diag1 or (row + c) in diag2:
                    continue

                board[row][c] = "Q"
                col.add(c)
                diag1.add(row - c)
                diag2.add(row + c)

                backtrack(row + 1)

                board[row][c] = "."
                col.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)

        backtrack(0)
        return ans