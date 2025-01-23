class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = nums1 + nums2
        l.sort()
        mid = int(len(l) / 2)
        for i in range(len(l)):
            if len(l) % 2 == 0:
                return (l[mid] + l[mid - 1]) / 2
            else: 
                return l[mid] 
            
s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))


        