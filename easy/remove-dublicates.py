from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = sorted(set(nums))
        # for i in range(len(unique_nums)):
        #     nums[i] = unique_nums[i]
        
        diff_count = len(nums) - len(unique_nums)
        l = len(unique_nums)
        list = []
        for i in range(diff_count):
            list.append("_")

        # return f'{l}, nums = {unique_nums + list}'
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1
        return length

    
s = Solution()
print(s.removeDuplicates([1,1,2]))

# runtime 2ms 