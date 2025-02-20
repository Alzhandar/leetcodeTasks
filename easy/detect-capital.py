class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper = True
        all_lower = True
        first_upper = ord(word[0]) >= ord('A') and ord(word[0]) <= ord('Z')
        
        for i in range(len(word)):
            if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
                all_lower = False
                if i > 0:
                    first_upper = False
            else:
                all_upper = False
                
        return all_upper or all_lower or (first_upper and not all_upper)


s = Solution()
print(s.detectCapitalUse("USA"))      

