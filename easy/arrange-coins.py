class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = []
        i = 1
        for i in range(1, n+1):
            n -= i
            if n < 0:
                return i - 1
# Тесты
s = Solution()
print(s.arrangeCoins(5))