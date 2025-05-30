class Solution:
    def numSquares(self, n):
        
        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count
        return n

s = Solution()
print(s.numSquares(12))  