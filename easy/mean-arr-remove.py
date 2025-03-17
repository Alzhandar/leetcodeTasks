class Solution:
    def trimMean(self, arr: list[int]) -> float:
        left = int(len(arr) * 0.05)
        right = int(len(arr) * 0.95)
        return sum(sorted(arr)[left:right]) / (right - left)
    
s = Solution()
print(s.trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,4])) 