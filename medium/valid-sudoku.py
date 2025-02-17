class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board, i):
                return False
            if not self.isValidColumn(board, i):
                return False
            if not self.isValidSquare(board, i):
                return False
        return True

    def isValidRow(self, board: list[list[str]], row: int) -> bool:
        return self.isValidSet(board[row])
    
    def isValidColumn(self, board: list[list[str]], column: int) -> bool:
        return self.isValidSet([board[i][column] for i in range(9)])
    
    def isValidSquare(self, board: list[list[str]], square: int) -> bool:
        row = square // 3
        column = square % 3
        return self.isValidSet([board[row * 3 + i][column * 3 + j] for i in range(3) for j in range(3)])
    
    def isValidSet(self, s: list[str]) -> bool:
        s = [c for c in s if c != '.']
        return len(s) == len(set(s))
    

s = Solution()
print(s.isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])) 
        