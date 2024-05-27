"""
Two Integer Sum
Solved 
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10000 <= nums[i] <= 10000
-10000 <= target <= 10000

"""




class Solution:
    
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        # Get the length of the array
        n = len(nums)
        
        # Iterate through each element using two nested loops
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of the two elements is equal to the target
                if nums[i] + nums[j] == target:
                    # Return the indices of the two elements
                    return [i, j]
        
        # If no solution is found, return an empty list (this shouldn't happen as per the problem statement)
        return []


    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        # Create a list of tuples where each tuple is (num, index)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort the list based on the numbers
        indexed_nums.sort()
        
        # Initialize two pointers
        left = 0
        right = len(indexed_nums) - 1
        
        # Iterate with the two pointers until they meet
        while left < right:
            left_num, left_index = indexed_nums[left]
            right_num, right_index = indexed_nums[right]
            
            current_sum = left_num + right_num
            
            if current_sum == target:
                # Return the original indices in ascending order
                return sorted([left_index, right_index])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        # If no solution is found, return an empty list (this shouldn't happen as per the problem statement)
        return []




def main():
    s = Solution()
    number_array=[1,2,3,4,5]
    target= 9
    print(s.twoSum1(number_array,target))
    print(s.twoSum2(number_array,target))
    print(s.twoSum3(number_array,target))



main()