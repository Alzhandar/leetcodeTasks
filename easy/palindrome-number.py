class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
a = int(input())

s = Solution()
print(s.isPalindrome(a))
# runtime: 1ms beats 92.5% of Python3 submissions