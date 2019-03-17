"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        296 ms
        """
        new_A = [0 for _ in range(len(A))]
        odd, even = 0, 0
        for a in A:
            if a % 2 == 0:
                new_A[even * 2] = a
                even += 1
            else:
                new_A[odd * 2 + 1] = a
                odd += 1
        return new_A

    def sortArrayByParityII_1(A):
        """
        136ms
        :return:
        """
        s = [0] * len(A)
        e = 0
        o = 1
        for i in A:
            if i % 2 == 0:
                s[e] = i
                e += 2
            else:
                s[o] = i
                o += 2
        return s


print(Solution().sortArrayByParityII([4,2,5,7]))
# print(Solution().sortArrayByParityII([4,2,5,7]))