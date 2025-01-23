class Solution:
  
  def majorityElement(self, nums: list[int]) -> int:
    ans = None
    count = 0

    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)

    return ans
  
  def majorityElement2(self, nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]

  

  
s = Solution()
print(s.majorityElement([3,2,3]))