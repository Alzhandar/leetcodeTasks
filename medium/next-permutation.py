class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i + 1:] = reversed(nums[i + 1:])
                return nums
        nums.reverse()
        return nums

s = Solution()
print(s.nextPermutation([1,2,3]))
print(s.nextPermutation([3,2,1]))