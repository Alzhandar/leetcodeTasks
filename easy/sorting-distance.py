class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(' ')
        l.sort(key=lambda x: int(x[-1]))
        return ' '.join([i[:-1] for i in l])
    
s = Solution()
print(s.sortSentence("is2 sentence4 This1 a3"))