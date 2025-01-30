class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = {}
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in magazine_counts or magazine_counts[char] == 0:
                return False
            magazine_counts[char] -= 1
            
        return True
    
