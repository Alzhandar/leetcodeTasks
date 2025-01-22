from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target < nums[i]:
                right = i -1
                return right
            else:
                left = i + 1
        return left
    
s = Solution()
print(s.searchInsert([1,3,5,6],7))
