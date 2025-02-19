class Solution(object):
    def combinationSum(self, candidates, target):
        subsets = []
        candidates.sort()
        for idx, candidate in enumerate(candidates):
            left = target - candidate
            if left == 0:
                subsets.append([candidate])
            elif left > 0:
                for subset in self.combinationSum(candidates[idx:], left):
                    subsets.append([candidate] + subset)
            else:
                break
        
        return subsets
    
s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7)) 
        