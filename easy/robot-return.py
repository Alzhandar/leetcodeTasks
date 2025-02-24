class Solution:
    def judgeCircle(self, moves):
        if not moves:
            return True
        
        count_u = 0
        count_d = 0
        count_l = 0
        count_r =0

        for i in range(len(moves)):
            if moves[i] == 'U':
                count_u += 1
            elif moves[i] == 'D':
                count_d += 1
            elif moves[i] == 'L':
                count_l += 1
            elif moves[i] == 'R':
                count_r += 1

        return count_u == count_d and count_l == count_r
    
s = Solution()
print(s.judgeCircle("UD"))