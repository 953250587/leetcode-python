"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[i for i in range(len(numbers))]
        dicts=dict(zip(numbers[:],l[:]))
        for i in numbers:
            t=target-i
            if t in dicts.keys():
                if t==i:
                   return [dicts[i],dicts[t]+1]
                else:
                    return [dicts[i]+1,dicts[t]+1]
            else:
                continue

    def twoSum_1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(numbers):
            if (target - num) in num_dict:
                return [num_dict[target - num], i + 1]
            num_dict[num] = i + 1

a=Solution()
number=[0, 0, 3, 4]
print(a.twoSum(numbers=number,target=0))

