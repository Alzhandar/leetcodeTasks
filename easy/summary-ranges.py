class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                continue
            
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            
            if i + 1 < len(nums):
                start = nums[i + 1]
                
        return result
    
s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))