class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row, column in enumerate(zip(*matrix)):
            matrix[row] = list(reversed(column))
        return matrix

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
        