class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        s = str(grid)
        l = s.split()
        return s.count('-')
    
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            for num in row:
                if num < 0:
                    count += 1
        return count
    
s = Solution()
print(s.countNegatives([[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]]))
        