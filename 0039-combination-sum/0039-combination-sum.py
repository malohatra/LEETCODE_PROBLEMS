class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []

        def backtrack(start, target):

            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])

                # Same index because reuse is allowed
                backtrack(i, target - candidates[i])

                path.pop()

        backtrack(0, target)

        return result