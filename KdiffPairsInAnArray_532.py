"""
 Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].

"""
from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        59ms
        """
        #
        sum=0
        if k > 0:
            # print(set(nums))
            # print(set(n + k for n in nums))
            # print(set(nums) & set(n + k for n in nums))
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            for i in [v > 1 for v in Counter(nums).values()]:
                if i==True:
                    sum+=1
            return sum
        else:
            return 0

    def findPairs_1(self, nums, k):
        sum=0
        if k==0:
            for i in [v > 1 for v in Counter(nums).values()]:
                if i==True:
                    sum+=1
            return sum
        if k>0:
            l2=sorted(list(set(nums)))
            k1=0
            for i in range(len(l2)):
                k1=max(i+1,k1)
                for j in range(k1,len(l2)):
                    if l2[j]==l2[i]+k:
                       sum+=1
                       k1=j
                       break
                    elif l2[j]>l2[i]+k:
                       k1=j
                       break
        return sum




print(Solution().findPairs_1([1,3,1,5,6],0))
print(Solution().findPairs_1([3, 1, 4, 1, 5],2))
print(Solution().findPairs_1([1,2,3,4,5],1))
