"""
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)



Example 1:

Input: [0]
Output: 1
Explanation:
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation:
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation:
The possible results are 1, 2, 3, 4, 6, and 7.


Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9
"""


class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        total_s = []
        s = set()
        s.add(A[0])
        total_s.append(s)
        for i in range(1, l):
            next_s = set()
            next_s.add(A[i])
            for value in total_s[i - 1]:
                next_s.add(value | A[i])
            total_s.append(next_s)
        ans = set()
        for s in total_s:
            ans = ans.union(s)
        return len(ans)

    def subarrayBitwiseORs_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        B[i][j] = A[i] | A[i+1] | ... | A[j]
        Hash set cur stores all wise B[0][i], B[1][i], B[2][i], B[i][i].
        Normally this part is easy.
        But for this problem, time complexity matters a lot.

        The solution is straight forward,
        while you may worry about the time complexity up to O(N^2)
        However, it's not the fact.
        This solution has only O(30N)

        The reason is that, B[0][i] >= B[1][i] >= ... >= B[i][i].
        B[0][i] covers all bits of B[1][i]
        B[1][i] covers all bits of B[2][i]
        ....

        There are at most 30 bits for a positive number 0 <= A[i] <= 10^9.
        So there are at most 30 different values for B[0][i], B[1][i], B[2][i], ..., B[i][i].
        Finally cur.size() <= 30 and res.size() <= 30 * A.length()

        In a worst case, A = {1,2,4,8,16,..., 2 ^ 29}
        And all B[i][j] are different and res.size() == 30 * A.length()
        """
        cur = set() #
        res = set() #
        for a in A:
            before = set()
            for i in cur:
                before.add(i | a)
            before.add(a)
            cur = before
            res = res.union(cur)
        return len(res)

    def subarrayBitwiseORs_2(self, A):
        """
         1076 ms
        :param A:
        :return:
        """
        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)

    def subarrayBitwiseORs_3(self, A):
        """
        :type A: List[int]
        :rtype: int
        600ms
        """
        ansset = set()
        prev = set([0])
        for a in A:
            prev = {a | prev_v for prev_v in prev}
            prev |= {a}
            ansset |= prev
        return len(ansset)

import numpy as np
print(Solution().subarrayBitwiseORs_1([0])) # 1
print(Solution().subarrayBitwiseORs_1([1,1,2])) # 3
print(Solution().subarrayBitwiseORs_1([1,2,4])) # 6
print(Solution().subarrayBitwiseORs_1(list(np.random.randint(0 ,high=10**9, size=5000))))