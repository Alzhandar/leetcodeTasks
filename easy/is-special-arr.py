class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i - 1] % 2 == 0 and nums[i] % 2 != 0:
                return True
        return False

        
    
s = Solution()
print(s.isArraySpecial([2, 7, 4, 6, 9, 5])) 
        