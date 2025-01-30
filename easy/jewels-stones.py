class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels) 
        count = sum(stone in jewels_set for stone in stones)  
        count2 = sum(1 for stone in stones if stone in jewels_set)
        return count
    
s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))