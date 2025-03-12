class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] > heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        return names[::-1]
    
s = Solution()
print(s.sortPeople(["John", "Alice", "Bob"], [5, 6, 4]))

        