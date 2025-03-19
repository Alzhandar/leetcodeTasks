class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        n = len(word)
        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= l or j >= w or board[i][j] != word[k]:
                return False
            if k == n - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res
        for i in range(l):
            for j in range(w):
                if dfs(i, j, 0):
                    return True
        return False
    
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
        