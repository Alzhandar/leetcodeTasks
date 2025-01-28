class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = int(num1)
        n2 = int(num2)

        res = n1 * n2

        return str(res)
    
s = Solution()
print(s.multiply("2", "3"))  