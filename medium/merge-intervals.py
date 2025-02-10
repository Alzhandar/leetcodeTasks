class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Сортировка остается той же
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[i][0] > intervals[j][0]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        
        # Добавляем логику объединения интервалов
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

s = Solution()
print(s.merge([[1,3], [2,6], [8,10], [15,18]]))  # исправлен формат входных данных