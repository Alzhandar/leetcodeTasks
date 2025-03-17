class Solution:
    def isConsecutive(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                return False
        return True
    
s = Solution()
print(s.isConsecutive([0,1,2,3,4]))
        