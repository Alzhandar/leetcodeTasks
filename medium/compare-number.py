class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = version1.split('.')
        num2 = version2.split('.')
        n1 = len(num1)
        n2 = len(num2)
        n = max(n1, n2)
        for i in range(n):
            v1 = int(num1[i]) if i < n1 else 0
            v2 = int(num2[i]) if i < n2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
    
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = int(version1)
        num2 = int(version2)

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        else:
            return 0
        

        
s = Solution()
print(s.compareVersion("1.0", "1"))  