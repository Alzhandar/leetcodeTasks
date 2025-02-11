class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l1 = []
        l2 = []

        for i in nums:
            if i % 2 == 0:
                l1.append(i)
            else:
                l2.append(i)
        return l1 + l2
    
s = Solution()
print(s.sortArrayByParity([3,1,2,4]))
        