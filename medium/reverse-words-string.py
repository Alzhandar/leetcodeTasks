class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        l = word[::-1]
        res = ' '.join(l)
        return res
    
s = Solution()
print(s.reverseWords("the sky is blue"))