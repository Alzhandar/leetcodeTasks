class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = []
        for word in s:
            result.append(word[::-1])
        return ' '.join(result)
    
# Тесты
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))


            