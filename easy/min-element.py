class Solution:
    def minElement(self, nums: list[int]) -> int:
        if not nums:
            return 0

        min_sum = float('inf')
        for i in nums:
            res = 0
            k = str(i)
            for j in k:
                res += int(j)
            if res < min_sum:
                min_sum = res
        return min_sum

s = Solution()
print(s.minElement([[12,123,3]])) 

            
        