class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        n = len(nums) // 2
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
    
s = Solution()
print(s.shuffle([2,5,1,3,4,7], 3))
        