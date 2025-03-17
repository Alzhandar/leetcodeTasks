class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        s = set(nums)
        freq = []
        for i in s:
            freq.append((i, nums.count(i)))
        freq.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for i in freq:
            res.extend([i[0]] * i[1])
        return res
    
    def frequencySort2(self, nums: list[int]) -> list[int]:
        l = len(nums)
        for i in range(l):
            nums[i] = (nums[i], nums.count(nums[i]))
        nums.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for i in nums:
            res.extend([i[0]] * i[1])
        return res
    
    
s = Solution()
print(s.frequencySort([1,1,2,2,2,3]))
print(s.frequencySort2([1,1,2,2,2,3]))