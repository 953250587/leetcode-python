# -*- coding: UTF-8 -*-
"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.


Example 1:
Input: [1,2,3,3]
Output: 3
Example 2:
Input: [2,1,2,5,3,2]
Output: 2
Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""


class Solution(object):
    # python
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        480 ms
        13 MB
        """
        lists = [0 for i in range(10000)]
        for i in A:
            lists[i] += 1
            if lists[i] > 1:
                return i
        return

    # python3
    def repeatedNTimes_1(self, A: List[int]) -> int:
        """
        56 ms
        14 MB
        :param A:
        :return:
        """
        return int((sum(A) - sum(set(A))) // (len(A) // 2 - 1))

    # python3
    def repeatedNTimes_2(self, A: List[int]) -> int:
        """
        48 ms
        14.2 MB
        :param A:
        :return:
        """
        unique = set()  # empty set
        for i in A:
            if i in unique:  # if 'i' element already exists then it is a duplicate
                return i  # loop is exited as value is directly returned
            unique.add(i)  # this can be kept in else: part but not required


if __name__ == '__main__':
    print(Solution().repeatedNTimes_1([1,2,3,3]))
    print(Solution().repeatedNTimes_1([2,1,2,5,3,2]))
    print(Solution().repeatedNTimes_1([5,1,5,2,5,3,5,4]))
    # print(Solution().repeatedNTimes([1, 2, 3, 3]))