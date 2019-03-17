"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.

Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        1589ms
        """
        import collections
        l = len(A)
        dicts = []
        a = collections.defaultdict(int)
        dicts.append(a)
        ans = 0
        for i in range(1, l):
            new_dict = collections.defaultdict(int)
            for j in range(i):
                cur_value = A[i]
                before_value = A[j]
                key = cur_value - before_value
                value = dicts[j][key]
                ans += value
                new_dict[key] += value + 1
            dicts.append(new_dict)
        for i in range(len(dicts)):
            print(dicts[i])
        return ans

    def numberOfArithmeticSlices_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        925ms
        """
        if len(A) < 3:
            return 0

        dp = [{} for _ in range(len(A))]
        rv = 0
        for i in range(len(A)):
            for j in range(i):
                x = A[i] - A[j]
                dp[i][x] = dp[i].get(x, 0) + 1
                if x in dp[j]:
                    dp[i][x] += dp[j][x]
                    rv += dp[j][x]

        return rv
print(Solution().numberOfArithmeticSlices([2,2,4,6,8,10]))

from collections import defaultdict
from itertools import ifilter


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        292ms
        """

        pre = defaultdict(int)
        post = defaultdict(int)
        pos = defaultdict(list)
        seq = [defaultdict(int) for _ in range(len(A))]

        for i, a in enumerate(A):
            post[a] += 1
            pos[a].append(i)

        for i, a in enumerate(A):
            post[a] -= 1
            for b in pre:
                c = (a << 1) - b
                if c in post and post[c] > 0:
                    n = pre[b]
                    if b in seq[i]:
                        n += seq[i][b]
                    for j in pos[c]:
                        if j > i:
                            seq[j][a] += n
            pre[a] += 1

        return sum([sum(p.values()) for p in seq])
