class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        l = []
        for num in nums1:
            if num not in nums2:
                l.append(num)
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                l.append(nums2[i])
        
        l1 = []
        l2 = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                l1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                l2.append(nums2[i])

        s = set(l1)
        l1 = list(s)
        s = set(l2)
        l2 = list(s)
        return [l1, l2]
       
        
    
s = Solution()
print(s.findDifference([1, 2, 3], [2, 4, 6])) 
        