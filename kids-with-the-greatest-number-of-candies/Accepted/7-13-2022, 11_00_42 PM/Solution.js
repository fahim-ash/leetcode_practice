// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let a=Math.max(...candies);
    let b=[];
    for (let i of candies){
        if (i+extraCandies>=a){
            b.push(true);
        }else{
            b.push(false);
        }
    }return b;
    

    
};