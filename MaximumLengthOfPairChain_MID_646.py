"""
 You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:

    The number of given pairs will be in the range [1, 1000].

"""
import numpy as np
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        89ms
        """
        p = sorted(pairs, key = lambda a:(a[1], a[0]))
        temp = p[0]
        count = 1
        for i in p[1:]:
            if i[-1] > temp[-1] and i[0] > temp[-1]:
                count += 1
                temp = i
        return count

    def findLongestChain_1(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        78ms
        """
        if not pairs:
            return 0
        pairs.sort(key=lambda x: x[1])
        count = 1
        prev = pairs[0][1]
        for i in xrange(1, len(pairs)):
            if pairs[i][0] < prev + 1:
                continue
            else:
                count += 1
                prev = pairs[i][1]
        return count

pairs = [[1,2], [2,3], [3,4]]
print(Solution().findLongestChain(pairs))


