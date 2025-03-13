class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = list(s)
        stack = []
        count = 0
        for i in l:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return count + len(stack)
    
s = Solution()
print(s.minAddToMakeValid("())"))
        