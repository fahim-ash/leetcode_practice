// https://leetcode.com/problems/check-if-n-and-its-double-exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (j*2)==i:
                    return True
                
        return False
        