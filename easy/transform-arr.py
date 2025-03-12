class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        l = []

        for i in nums:
            if i % 2 == 0:
                l.append(0)
        
        for i in nums:
            if i%2 == 1:
                l.append(1)
        return l
    
s = Solution()
print(s.transformArray([4,3,2,1]))
        