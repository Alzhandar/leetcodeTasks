class Solution:
    def clearDigits(self, s: str) -> str:
        for chr in s:
            if not chr.isdigit():
                s = s.replace(chr, '')
        return s
    
s = Solution()
print(s.clearDigits("cb34"))
        