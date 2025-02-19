class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        l = sorted(nums)
        sum = 0
        for i in range(0, len(l), 2):
            sum += l[i]
        return sum
    

s = Solution()
print(s.arrayPairSum([1, 4, 3, 2])) # 4
        