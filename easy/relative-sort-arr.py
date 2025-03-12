class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        l = []
        r = []

        for i in arr1:
            if i in arr2:
                l.append(i)
            else:
                r.append(i)
        
        r.sort()
        res = []
        for i in arr2:
            for j in l:
                if i == j:
                    res.append(j)
        res += r
        return res

s = Solution()
print(s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])) 
        