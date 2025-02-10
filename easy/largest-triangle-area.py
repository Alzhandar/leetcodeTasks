class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        max_s = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    s = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    max_s = max(max_s, s)
        return max_s
    
s = Solution()
print(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))

        