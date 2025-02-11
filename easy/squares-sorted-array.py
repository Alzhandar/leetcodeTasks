class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = len(nums)
        for i in range(l):
            nums[i] = pow(nums[i], 2)
        nums.sort()
        return nums

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
        