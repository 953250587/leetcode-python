"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        32MS
        """
        l=len(A)
        count=1
        sum_1=0
        for i in range(0,l-2):
            if A[i]+A[i+2]==2*A[i+1]:
                sum_1+=count
                count+=1
            else:
                count=1
        return sum_1

    def numberOfArithmeticSlices_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        35MS
        """
        la, count = len(A), 0
        for i in range(la):
            start = i + 2
            while start < la and A[start] == A[i] + (start - i) * (A[i + 1] - A[i]):
                start += 1
                count += 1
        return count
A = [1, 2, 3, 4]
print(Solution().numberOfArithmeticSlices(A))
A = [1, 2, 3, 4, 8,12,16,20]
print(Solution().numberOfArithmeticSlices(A))
A = []
print(Solution().numberOfArithmeticSlices(A))

