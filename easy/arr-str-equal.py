class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s = ''.join(word1)
        t = ''.join(word2)
        return s == t

s = Solution()
print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))