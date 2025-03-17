class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        l = []
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        return l
    
s = Solution()
print(s.targetIndices([2,7,11,15], 2))
print(s.targetIndices([2,3,4], 6))

        