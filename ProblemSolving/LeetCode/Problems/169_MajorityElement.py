"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

"""

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        m= defaultdict(int)
        for num in nums :
            m[num]+=1
        
        x= n // 2

        for key , value in m.items():
            if value > x :
                return key
            
        return 0
    
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        return (sorted(nums)[len(nums)//2])