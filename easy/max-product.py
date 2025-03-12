class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = (nums[i] - 1) * (nums[j] - 1)
                if product > max_product:
                    max_product = product
        return max_product
    
s = Solution()
print(s.maxProduct([3, 4, 5, 2]))
        