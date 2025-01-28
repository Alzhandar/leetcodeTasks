import math

class Solution:
    def isPowerOfTwo2(self, n: int) -> bool:
        if n <= 0:
            return False
        try:
            return math.log(n, 2).is_integer()
        except:
            return False
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0
    
        
s = Solution()
print(s.isPowerOfTwo(536870912))  # True (2^29) but this is not a power of 2
print(s.isPowerOfTwo(0))          
print(s.isPowerOfTwo(-16))      
print(s.isPowerOfTwo(1))          