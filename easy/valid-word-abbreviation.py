class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pos = 0  
        num = 0      
        for char in abbr:
            if char.isdigit():
                if num == 0 and char == '0':
                    return False
                num = num * 10 + int(char)
                continue
            
            if num:
                word_pos += num
                num = 0
                
            if word_pos >= len(word) or word[word_pos] != char:
                return False
            word_pos += 1
        word_pos += num
        return word_pos == len(word)

s = Solution()
print(s.validWordAbbreviation("internationalization", "i12iz4n"))  
print(s.validWordAbbreviation("apple", "a2e"))                    
print(s.validWordAbbreviation("leetcode", "l3t2de"))             