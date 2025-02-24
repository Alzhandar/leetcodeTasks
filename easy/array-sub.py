class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        subarrays = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if i + 1 == j:
                    subarrays.append([nums[i]])
                else:
                    subarrays.append(nums[i:j])        
        total_sum = 0
        for subarray in subarrays:
            total_sum += sum(subarray)
            
        return total_sum

s = Solution()
print(s.subarraySum([2, 3, 1]))