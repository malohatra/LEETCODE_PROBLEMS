class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        n = len(words)

        while i < n:
            line = []
            letters = 0

            # Collect words for current line
            while i < n and letters + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                letters += len(words[i])
                i += 1

            # Last line or single word
            if i == n or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                ans.append(s)
            else:
                spaces = maxWidth - letters
                gaps = len(line) - 1

                even = spaces // gaps
                extra = spaces % gaps

                s = ""

                for j in range(gaps):
                    s += line[j]
                    s += " " * (even + (1 if j < extra else 0))

                s += line[-1]
                ans.append(s)

        return ans