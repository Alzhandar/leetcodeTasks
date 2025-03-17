class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1 and i not in visited:
                    dfs(i)
        
        n = len(isConnected)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count

s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) 

        