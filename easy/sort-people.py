class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        heights.sort()
        names.sort()
        return [names[i] for i in range(len(names))]
    
s = Solution()
print(s.sortPeople(["John", "Alice", "Bob"], [5, 6, 4]))

        