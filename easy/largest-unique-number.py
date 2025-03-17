class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        for i in sorted(set(nums), reverse=True):
            if nums.count(i) == 1:
                return i
        return -1
s = Solution()
print(s.largestUniqueNumber([5,7,3,9,4,9,8,3,1])) 
        