class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


def main():
    s = Solution()
    str1="mohamedsalem"
    str2="salemmohamed"
    print(s.isAnagram1(str1,str2))
    print(s.isAnagram2(str1,str2))


main()
