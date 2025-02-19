class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        output_list = []
        
        for a in range(left, right+1):
            numbers = str(a)
            flag = 0
            
            for i in numbers:
                if int(i) == 0 or a % int(i) != 0:
                    flag = 1
                    break
                    
            if flag == 0:
                output_list.append(a)
            
        return output_list
                        

s = Solution()
print(list(s.selfDividingNumbers(1, 22))) 
