from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount

        target = Counter(words)

        ans = []

        for offset in range(wordLen):

            left = offset
            seen = defaultdict(int)
            count = 0

            for right in range(offset, len(s)-wordLen+1, wordLen):

                word = s[right:right+wordLen]

                if word in target:

                    seen[word] += 1
                    count += 1

                    while seen[word] > target[word]:

                        leftWord = s[left:left+wordLen]
                        seen[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    if count == wordCount:

                        ans.append(left)

                        leftWord = s[left:left+wordLen]
                        seen[leftWord] -= 1
                        left += wordLen
                        count -= 1

                else:

                    seen.clear()
                    count = 0
                    left = right + wordLen

        return ans