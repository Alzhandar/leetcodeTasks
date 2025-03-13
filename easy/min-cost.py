class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        odd = 0
        even = 0

        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)   

s = Solution()
print(s.minCostToMoveChips([1,2,3]))
        