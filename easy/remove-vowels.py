class Solution:
    def removeVowels(self, s: str) -> str:
        l = ['a', 'e', 'i', 'o', 'u']

        for i in s:
            if i in l:
                s = s.replace(i, '')
        return s
    
s = Solution()
print(s.removeVowels('leetcodeisacommunityforcoders')) 
        