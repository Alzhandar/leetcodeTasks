class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char.lower() for char in s if char.isalnum()]
        l = letters[::-1]
        return letters == l
s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))
