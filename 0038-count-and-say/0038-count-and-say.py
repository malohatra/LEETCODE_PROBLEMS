class Solution:
    def countAndSay(self, n: int) -> str:

        ans = "1"

        for _ in range(n - 1):

            result = []
            count = 1

            for i in range(1, len(ans)):

                if ans[i] == ans[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(ans[i - 1])
                    count = 1

            # Last group
            result.append(str(count))
            result.append(ans[-1])

            ans = "".join(result)

        return ans