class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        l = []
        
        for i in range(len(s)):
            l.append(i)
            
        for i in range(len(indices)):
            l[indices[i]] = s[i]
        return "".join(l)
    
s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3])) 
        