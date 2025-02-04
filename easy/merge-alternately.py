class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = max(len(word1),len(word2))
        for i in range(n):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        
        return "".join(res)


s = Solution()
print(s.mergeAlternately("abc","pqr"))