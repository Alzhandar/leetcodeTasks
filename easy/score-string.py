class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
    
s = Solution()
print(s.scoreOfString("hello"))
print(s.scoreOfString("zaz"))
        