class Solution:
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1 ]
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        s = {}
        for i, num in enumerate(numbers):
            if target - num in s:
                return [s[target - num] + 1, i + 1]
            s[num] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))        