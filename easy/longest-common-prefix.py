from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""

        for i in range(len(strs[0])):
            chr = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != chr:
                    return result
            result += chr
        return result

# runtime: 3ms 

input = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(input)) 


class Solution2(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

s2 = Solution2()
print(s2.longestCommonPrefix(input))