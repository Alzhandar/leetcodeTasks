class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        result = ""
        for char in chars:
            result += char * freq[char]
        
        return result
    
s = Solution()
print(s.frequencySort("tree")) 