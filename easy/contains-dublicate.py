class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        l2 = list(set(nums))

        if len(l2) == len(nums):
            return False
        else:
            return True


s = Solution()
print(s.containsDuplicate([3,1]))
print(s.containsDuplicate([3,3,1]))