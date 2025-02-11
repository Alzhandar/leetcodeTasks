class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1.lstrip('0') or '0'
        num2 = num2.lstrip('0') or '0'
        
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        
        carry = 0
        result = []
        
        for i in range(max_len - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))
        
        if carry:
            result.append(str(carry))
        
        return ''.join(result[::-1])


# Тест
s = Solution()
print(s.addStrings('2', '5'))  # Должно вывести "7"