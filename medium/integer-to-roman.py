class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ''
        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value
                
        return result

s = Solution()
print(s.intToRoman(3))  
print(s.intToRoman(58))  
print(s.intToRoman(1994))  