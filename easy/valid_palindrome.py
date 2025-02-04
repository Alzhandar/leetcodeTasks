class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char for char in s if char.isalpha()]
        l = letters[::-1]
        l.lower()
        return letters, l
s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))
