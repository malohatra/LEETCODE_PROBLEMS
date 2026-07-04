class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []
        path = []

        def backtrack(start, target):

            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Optimization
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # Move to next index (cannot reuse)
                backtrack(i + 1, target - candidates[i])

                path.pop()

        backtrack(0, target)

        return result