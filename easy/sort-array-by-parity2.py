class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        l = []
        r = []
        for i in nums:
            if i % 2 == 0:
                l.append(i)
            else:
                r.append(i)
                
        res = []
        for i in range(len(l)):
            res.append(l[i])
            res.append(r[i])
        return res

s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7])) 
        