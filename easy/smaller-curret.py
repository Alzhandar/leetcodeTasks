class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        l = []

        for i in nums:
            if i in nums:
                l.append(i)
            
        l.sort()
        res = []
        for i in range(len(nums)):
            res.append(l.index(nums[i]))
        return res
    
    
s = Solution()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
        
        