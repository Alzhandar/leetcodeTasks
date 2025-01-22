from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        plus = 1

        for i in range(len(digits)):
            integer += digits[i] * 10 ** (len(digits) - i -1)
    
        res = integer + plus
        l = []
        s = str(res)

        for i in s:
            l.append(int(i))

        return l


s = Solution()
print(s.plusOne([1,2,3]))
