class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        l = []
        
        for i in heights:
            l.append(i)

        l.sort()

        count = 0
        for i in range(len(heights)):
            if heights[i] != l[i]:
                count += 1
        return count
    
s = Solution()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
        