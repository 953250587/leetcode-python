"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 6
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:

    N is an integer within the range [1, 20,000].
    The elements of A are all distinct.
    Each element of A is an integer within the range [0, N-1].

"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        106MS
        """
        used = set()
        def dfs(start):
            count = 0
            while nums[start] not in used:
                start = nums[start]
                used.add(start)
                count += 1
            return count
        self.m = 0
        for i in nums:
            self.m = max(dfs(i), self.m)
        return self.m

    def arrayNesting_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        82MS
        """
        n = len(nums)
        visited = [False] * n
        res = 0

        for i in nums:
            if visited[i]:
                continue
            visited[i] = True
            cnt = 1
            start = i
            i = nums[i]
            while i != start:
                visited[i] = True
                i = nums[i]
                cnt += 1
            res = max(cnt, res)

        return res
print(Solution().arrayNesting([5,4,0,3,1,6,2]))
