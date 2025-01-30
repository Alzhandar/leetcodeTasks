class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] <= k:
                    return True
                else:
                    return False
        