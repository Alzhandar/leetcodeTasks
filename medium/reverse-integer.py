class Solution:
    def revers2(self, x: int) -> int:

        s = str(x)
        
        if s[0] == '-':
            return  int(s[:0:-1]) * -1

        else:
            for i in s:
                return int(s[::-1])
    

s = Solution()
print(s.revers2(-123))


