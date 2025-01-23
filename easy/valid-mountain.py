from typing import List


class Solution:
    def validMountainArray1(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3:  
            return False

        peak = False 

        for i in range(1, N):
            if arr[i] == arr[i - 1]:  
                return False
            
            if not peak:
                if arr[i] < arr[i - 1]:  
                    peak = True
            else:
                if arr[i] >= arr[i - 1]:  
                    return False

        return peak

    def validMountainArray2(self, A):
        N = len(A)
        i = 0

        while i+1 < N and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == N-1:
            return False

        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
    
    def validMountainArray3(self, arr: List[int]) -> bool:

        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False

        is_increasing = True

        for i in range(0, len(arr) - 2):
            if is_increasing:
                if arr[i] >= arr[i + 1]:
                    is_increasing = False
            else:
                if arr[i] <= arr[i + 1]:
                    return False
        return True
s = Solution()
print(s.validMountainArray3([[3,5,5]]))