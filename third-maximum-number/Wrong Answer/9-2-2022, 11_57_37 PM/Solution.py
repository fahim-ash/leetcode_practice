// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        obj={}
        for i in nums:
            obj[i]=1
        list=[]
        list.sort(reverse=True)
        for i in obj:
            list.append(i)
        if len(list)<3:
            return list[0]
      
        else:
            return list[2]