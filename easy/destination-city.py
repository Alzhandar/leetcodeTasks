class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        city_from = []
        city_to = []
        for i in paths:
            city_from.append(i[0])
            city_to.append(i[1])
        for i in city_to:
            if i not in city_from:
                return i
        return None
    
    
s = Solution()
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

        