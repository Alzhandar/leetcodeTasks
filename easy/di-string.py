class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        min_val, max_val = 0, n  
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(min_val)  
                min_val += 1  
            else:
                perm.append(max_val) 
                max_val -= 1  
        
        perm.append(min_val)  
        
        return perm

s = Solution()
print(s.diStringMatch("IDID"))
