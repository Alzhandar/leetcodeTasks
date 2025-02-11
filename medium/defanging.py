class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = []
        s = 0
        for char in address:
            if char == '.':
                char = '[.]'
            l.append(char)

        for i in l:
            s += 1
            if s == len(l):
                return ''.join(l)
    

s = Solution()
print(s.defangIPaddr("1.1.1.1"))