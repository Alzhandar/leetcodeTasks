class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            d[n] = i
        return False
    
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))