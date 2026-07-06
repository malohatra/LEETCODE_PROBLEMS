class Solution:
    def totalNQueens(self, n: int) -> int:

        col = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for c in range(n):

                if c in col or (row - c) in diag1 or (row + c) in diag2:
                    continue

                col.add(c)
                diag1.add(row - c)
                diag2.add(row + c)

                backtrack(row + 1)

                col.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)

        backtrack(0)
        return count