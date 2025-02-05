class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for word in words:
            if word[:n] == pref:
                count += 1
        return count

s = Solution()
print(s.prefixCount(["pay","attention","practice","attend"],"at"))

    
        