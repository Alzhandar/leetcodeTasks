class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return i

s = Solution()
print(s.singleNumber([1,2,3,4,4,5,2,3]))