class Solution:
    def fractionAddition(self, expression: str) -> str:
        s = '+'
        m = '-'
        l1 = []  
        l2 = []  
        nums = []  
        
        if expression[0] not in ['+', '-']:
            expression = '+' + expression
            
        for i in expression:
            if i == s or i == m:
                l1.append(i)
            else:
                l2.append(i)
        
        current = ''
        for c in l2:
            if c == '/':
                nums.append(int(current))
                current = ''
            else:
                current += c
        nums.append(int(current))
        
        if l1[0] == '+':
            result_num = nums[0]
        else:
            result_num = -nums[0]
        result_den = nums[1]
        
        for i in range(2, len(nums), 2):
            num = nums[i]
            den = nums[i+1]
            idx = i//2
            
            new_num = result_num * den
            if l1[idx] == '+':
                new_num += num * result_den
            else:
                new_num -= num * result_den
            result_den *= den
            result_num = new_num
        
        def gcd(a, b):
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a
            
        d = gcd(result_num, result_den)
        
        return f"{result_num//d}/{result_den//d}"

s = Solution()
print(s.fractionAddition("-1/2+1/2"))