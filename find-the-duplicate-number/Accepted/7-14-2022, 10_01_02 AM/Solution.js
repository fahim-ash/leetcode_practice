// https://leetcode.com/problems/find-the-duplicate-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let list=[];
    for (let i =0;i<nums.length;i++){
        for (let j=i+1;j<nums.length;j++){
            if (nums[i]===nums[j]){
                return nums[i];
                
                };
        };
      
}; };