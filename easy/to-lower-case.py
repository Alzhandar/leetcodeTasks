class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []

        for char in s:
            if 65 <= ord(char) <= 90:  
                result.append(chr(ord(char) + 32))  
            else:
                result.append(char)  
        
        return ''.join(result)  
    
s = Solution()
print(s.toLowerCase('LoWeR'))
