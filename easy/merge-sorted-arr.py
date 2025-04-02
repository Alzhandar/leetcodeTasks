class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()
        
    
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)  