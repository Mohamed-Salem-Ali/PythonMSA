"""
Anagram Groups

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]
Output: [["x"]]

Example 3:

Input: strs = [""]
Output: [[""]]

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.


"""
from collections import defaultdict


class Solution:
    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:

        # Initialize a default dictionary where each value is a list
        anagrams = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:

            # Sort the characters in the string and use it as the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_str].append(s)

        # Return the values (lists of anagrams) from the dictionary
        return list(anagrams.values())
    
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


def main():
    s = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    print(s.groupAnagrams1(strs))
    print(s.groupAnagrams2(strs))

main()