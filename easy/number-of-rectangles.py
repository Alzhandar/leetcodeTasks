class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        max_len = 0
        count = 0

        for rectangles in rectangles:
            side = min(rectangles)
            if side > max_len:
                max_len = side
                count = 1
            elif side == max_len:
                count += 1
        return count
    
    
s = Solution()
print(s.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))