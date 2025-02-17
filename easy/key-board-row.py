class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        l = []
        for word in words:
            for row in rows:
                if all([char.lower() in row for char in word]):
                    l.append(word)
                    break
        return l
    
s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(s.findWords(["adsdf","sfd"]))
print(s.findWords(["omk"]))

        