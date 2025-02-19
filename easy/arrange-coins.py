class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = []
        i = 1
        while n >= i:
            l.append(i)
            n -= i
            i += 1
        return len(l)
    
# Тесты
s = Solution()
print(s.arrangeCoins(5))