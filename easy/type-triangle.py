class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"

        return "scalene"
    
s = Solution()
print(s.triangleType([2,2,2]))
        