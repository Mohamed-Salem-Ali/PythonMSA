"""
Top K Elements in List
Given an integer array nums and an integer k, 
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.


"""

"""
My Solution 

1- Using Dictionary to get the frequency of each element 

"""

def countFrequency(x):
    countFreq ={}
    for element in x:
        if element not in countFreq:
            countFreq[element]=1
        else:
            countFreq[element]+=1
    return (countFreq)

def sortDict(X):
    sortedDict = sorted(X.items(), key=lambda item : item[1],reverse=True )
    return sortedDict

def TopKElement(x,k):
    x1=countFrequency(x)
    print(x1,)
    x2= sortDict(x1)
    print(x2)
    x3 = [item[0] for item in x2[:k]]
    print(x3)
    return x3


def topKFrequent( nums: list[int], k: int) -> list[int]:
    freqDict ={}
    for x in nums :
        if x not in freqDict:
            freqDict[x]=1
        else:
            freqDict[x] = freqDict[x] +1

    sortedDict= sorted(freqDict.items(),key= lambda item:item[1],reverse=True)

    Top_k_elements = [item[0] for item in sortedDict[:k] ]
    return Top_k_elements

def main():
    array1 = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,8]
    TopKElement(array1,1)


main()