from collections import Counter
class Solution():
    def validanagram(self, s: str, t: str) -> bool:
        #approach 1
        #one line of code using collections module
        # return Counter(s) == Counter(t)

        #approach 2
        # sorting is also a solution
        # return sorted(s) == sorted(t)

        #approach 3
        if len(s) != len(t):
            return False
        counterS , counterT = {}, {}

        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        for c in counterS:
            if counterS[c] != counterT.get(c, 0):
                return False
        return True




sol = Solution()

s = "anagram"
t = "naaagrm"
print(sol.validanagram(s,t))
