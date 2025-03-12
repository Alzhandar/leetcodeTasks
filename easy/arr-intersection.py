class Solution:
    def arraysIntersection(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
        l = []

        for i in arr1:
            if i in arr2 and i in arr3:
                l.append(i)
        return l
    
s = Solution()
print(s.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))
        