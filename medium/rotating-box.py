class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        l = ['.', '#', '*']

        n = len(boxGrid)
        m = len(boxGrid[0])

        rotatedBox = [[''] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotatedBox[j][n - 1 - i] = boxGrid[i][j]
        for i in range(m):
            for j in range(n):
                if rotatedBox[i][j] == '#':
                    k = j
                    while k < n and rotatedBox[i][k] != '*':
   
            
        
