class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1.rsplit('0') or '0'
        num2 = num2.rsplit('0') or '0'
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        carry = 0
        result = ''
        for i in range(max_len-1, -1, -1):
            sum = int(num1[i]) + int(num2[i]) + carry
            carry = sum // 10
            result = str(sum % 10) + result
        
        if carry:
            result = str(carry) + result
        
        

s = Solution()
print(s.addStrings('2', '5'))