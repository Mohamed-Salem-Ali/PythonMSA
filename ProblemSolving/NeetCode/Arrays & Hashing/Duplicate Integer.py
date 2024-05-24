"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""


class Solution:
    def hasDuplicate1(self, nums: list[int]) -> bool:
        nums1 = set(nums)
        result = len(nums1) != len(nums)
        return result

    def hasDuplicate2(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def main():
    s=Solution()
    list1=[1,2,3,4,5]
    list2=[1,2,3,4,5,5]
    print(s.hasDuplicate2(list1))
    print(s.hasDuplicate2(list2))

main()