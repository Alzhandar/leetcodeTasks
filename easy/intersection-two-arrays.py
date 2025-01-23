class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))

s = Solution()
print(s.intersection([1,2,2,1],[2,2]))



