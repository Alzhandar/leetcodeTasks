class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2: 
                return float('inf')
            return (y2 - y1) / (x2 - x1)
        
        max_points = 1
        for i in range(n):
            slopes = {} 
            same_points = 1 
            
            for j in range(n):
                if i != j:
                    if points[i] == points[j]:
                        same_points += 1
                        continue
                        
                    s = slope(points[i], points[j])
                    slopes[s] = slopes.get(s, 1) + 1
            
            if slopes:
                max_points = max(max_points, max(slopes.values()) + same_points - 1)
            else:
                max_points = max(max_points, same_points)
        
        return max_points
    
s = Solution()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))