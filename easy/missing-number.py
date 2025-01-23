class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l = []
        nums.sort()

        for i in range(len(nums)+1):
            l.append(i)
        
        missing = list(set(l) - set(nums))

        return missing[0]

s = Solution()

print(s.missingNumber([9,6,4,2,3,5,7,0,1]))