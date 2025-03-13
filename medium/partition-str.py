class Solution(object):
    def partitionString(self, s):
        d = [0] * 26
        res = 1
        for c in s:
            i = ord(c) - ord('a')
            if d[i] == res: res += 1
            d[i] = res

        return res
    
s = Solution()
print(s.partitionString("abacaba"))