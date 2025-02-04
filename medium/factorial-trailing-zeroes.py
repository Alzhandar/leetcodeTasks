class Solution:
    def trailingZeroes(self, n: int) -> int:
        l = []
        for i in range(1, n + 1):
            l.append(i)
        
        res = 1
        for i in l:
            res *= i

        count = 0
        while res % 10 == 0:
            count += 1
            res //= 10
        return count
        
s = Solution()
print(s.trailingZeroes(7))