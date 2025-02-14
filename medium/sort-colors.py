class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l0 = []
        l1 = []
        l2 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                l0.append(nums[i])
            elif nums[i] == 1:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l = l0 + l1 + l2
        return l
    

s = Solution()
print(s.sortColors([2,0,2,1,1,0]))