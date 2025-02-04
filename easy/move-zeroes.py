class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)  
s2 = Solution()
print(s2.moveZeroes([0,1,2,3,4]))