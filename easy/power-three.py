class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(1, n):
            if 3**i == n:
                return True
            elif 3**i > n:
                return False
        return False
    
s = Solution()
print(s.isPowerOfThree(27))  
