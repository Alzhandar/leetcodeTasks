class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l2 = []

        for i in range(len(nums) - k):
             l2.append(nums[i])
        missing = list(set(nums) - set(l2))

        return missing + l2

s = Solution()
print(s.rotate([1,2,3,4,5,6,7],3))