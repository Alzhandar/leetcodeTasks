class Solution:
    def clearDigits(self, s: str) -> str:
        for char in s:
            if not char.isdigit():
                s = s.replace(char, '')
        return s
    

s = Solution()
print(s.clearDigits("a1b2c3d4"))
        