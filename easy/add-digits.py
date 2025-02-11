class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        l = []
        s = str(num)
        for i in s:
            l.append(int(i))
        for i in l:
            res += i
        if res > 9:
            return self.addDigits(res)
        return res
    
    
s = Solution()
print(s.addDigits(38))


 

        