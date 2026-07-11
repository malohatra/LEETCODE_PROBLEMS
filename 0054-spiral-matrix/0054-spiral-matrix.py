class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []

        while top <= bottom and left <= right:

            # Traverse Left -> Right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            # Traverse Top -> Bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Traverse Right -> Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            # Traverse Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans