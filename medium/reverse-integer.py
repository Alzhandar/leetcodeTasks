class Solution:
    def revers2(self, x: int) -> int:

        s = str(x)
        
        if s[0] == '-':
            return  int(s[:0:-1]) * -1

        else:
            for i in s:
                return int(s[::-1])
            
    def reverse3(self, x: int) -> int:
        if x < 0:
            return self.revers2(x)
        else:
            return self.revers2(x)

    def reverse(seelf, x: int) -> int:
        s = str(abs(x))

        reversed_number = int(s[::-1])
        if reversed_number > 2147483647:
            return 0
        
        return reversed_number if x > 0 else (reversed_number * -1)
            

s = Solution()
print(s.revers2(-123))    


