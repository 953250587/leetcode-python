"""
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        316 ms
        """
        import bisect
        a = sorted(A)
        result = []
        for b in B:
            p = bisect.bisect(a, b)
            if p < len(a):
                result.append(a[p])
                a.pop(p)
            else:
                result.append(a[0])
                a.pop(0)
        return result

    def advantageCount_1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        220ms
        """
        l = len(A)
        res = [0] * l
        idx = range(l)
        idx.sort(key=lambda x: B[x])
        A.sort()
        left = 0
        right = l - 1
        for i in range(l):
            if (A[i] <= B[idx[left]]):
                res[idx[right]] = A[i]
                right -= 1
            else:
                res[idx[left]] = A[i]
                left += 1
        return res


import bisect
print(bisect.bisect([0,0,1,2,3,4], 5))
print(Solution().advantageCount(A = [2,7,11,15], B = [1,10,4,11]))
print(Solution().advantageCount(A = [12,24,8,32], B = [13,25,32,11]))