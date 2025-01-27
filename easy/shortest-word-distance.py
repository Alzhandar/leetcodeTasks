class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        pos1 = wordsDict[0]
        pos2 = wordsDict[0]
        l = []
        l2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
                l.append(pos1)
            if wordsDict[i] == word2:
                pos2 = i
                l2.append(pos2)
        # res = pos_1 - pos_2
        # if res < 0:
        #     res = -1 * res
        # return res
        min_distance = float('inf')
        for i in l:
            for j in l2:
                min_distance = min(min_distance, abs(i - j))
        return min_distance
        
s = Solution()
print(s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
        