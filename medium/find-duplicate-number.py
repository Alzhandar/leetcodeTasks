class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        duplicates = []

        for i in nums:
            if i in seen:
                duplicates.append(i)
            else:
                seen.add(i)

        return duplicates[0]

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))