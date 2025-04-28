class Solution:
    def calculate(self, s: str) -> int:
        l = ['(', ')', '+', '-', '*', '/']
        stack = []
        num = 0
        sign = '+'
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                continue
            if s[i] in l:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = s[i]
            else:
                num = num * 10 + int(s[i])
        if sign == '+':
            stack.append(num)
        elif sign == '-':
            stack.append(-num)
        elif sign == '*':
            stack[-1] *= num
        elif sign == '/':
            stack[-1] = int(stack[-1] / num)
        return sum(stack)

s = Solution()
print(s.calculate("3+2*2"))
        