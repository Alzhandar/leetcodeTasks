class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
        return nums
    
s = Solution()
print(s.runningSum([1,2,3,4]))
        