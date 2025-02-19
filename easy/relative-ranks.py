class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        d = {}

        for i in range(len(sorted_score)):
            if i == 0:
                d[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                d[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                d[sorted_score[i]] = "Bronze Medal"
            else:
                d[sorted_score[i]] = str(i + 1)
        
        return [d[score[i]] for i in range(len(score))]

s = Solution()
print(s.findRelativeRanks([10,3,8,9,4]))
        