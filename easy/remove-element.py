from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        l2 = len(nums)
        nums = [x for x in nums if x != val]
        l3 = len(nums)
        dif_count = l2 - len(nums)

        for i in range(dif_count):
            nums.append('_')
        return f'{l3} nums = {nums}'
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        count = 0  

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]  
                count += 1
        
        return count



s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))
print(s.removeElement2([0,1,2,2,3,0,4,2],2))
