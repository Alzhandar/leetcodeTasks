class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return False
        
        def expandAroundCentre(left: int,right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        longest = ""

        for i in range(len(s)):
            odd_palindrome = expandAroundCentre(i, i)
            even_palindrome = expandAroundCentre(i, i+1)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
        


    
s = Solution()
print(print(s.longestPlaindrome('abbd')))