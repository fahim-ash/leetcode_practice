// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        indx=0
        for i in range (len(nums)):
            if nums[i]==key:
                indx=i
                break
        List=[]
        
        
        for i in range(indx+1,len(nums)):
        
            List.append(nums[i])
        
        List.sort(reverse=True)
        
        
        counter = 0
        new=0

        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency > counter):
                counter = curr_frequency
                new = i
                
       
        return new


        