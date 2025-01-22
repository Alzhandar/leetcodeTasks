class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        l = len(haystack) - len(needle) + 1

        for i in range(l):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
    
s = Solution()
print(s.strStr("leetcode","leeto"))  