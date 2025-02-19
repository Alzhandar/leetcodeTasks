class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        l = []
        for i in range(len(nums)):
            if nums[i] == lower:
                lower += 1
            elif nums[i] > lower:
                l.append([lower, nums[i] - 1])
                lower = nums[i] + 1
        if lower <= upper:
            l.append([lower, upper])
        return l
    
s = Solution()
print(s.findMissingRanges([0, 1, 3, 50, 75], 0, 99)) 

        