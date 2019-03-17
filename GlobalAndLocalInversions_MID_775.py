"""
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

Note:

    A will be a permutation of [0, 1, ..., A.length - 1].
    A will have length in range [1, 5000].
    The time limit for this problem has been reduced.

"""


class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        287ms
        """
        if len(A) <= 2:
            return True
        stack = [A[0]]
        i = 1
        max_1 = -float('inf')
        while i < len(A):
            if not stack or A[i] >= stack[-1]:
                stack.append(A[i])
                if A[i] < max_1:
                    return False
            else:
                count = 0
                if i + 1 < len(A) and A[i + 1] <= A[i] or A[i] < max_1:
                    return False
                while stack and stack[-1] > A[i]:
                    stack.pop()
                    count += 1
                if count > 1:
                    return False
                max_1 = max(max_1, A[i - 1])
            i += 1
        return True
print(Solution().isIdealPermutation(A = [1,0,2]))
print(Solution().isIdealPermutation(A = [1,2,0]))
print(Solution().isIdealPermutation([2, 0, 1]))
print(Solution().isIdealPermutation([1, 3, 2, 0]))
print(Solution().isIdealPermutation([2, 0, 3, 1]))