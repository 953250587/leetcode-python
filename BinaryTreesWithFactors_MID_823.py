"""
Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].



Note:

    1 <= A.length <= 1000.
    2 <= A[i] <= 10 ^ 9.


"""


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        152ms
        """
        import collections, bisect
        A = sorted(A)
        a = set(A)
        dicts = collections.defaultdict(int)

        for i in range(len(A)):
            dicts[A[i]] = 1
            k = bisect.bisect_right(A, A[i] ** 0.5)
            # print(A[i], k)
            for j in range(k):
                # print(dicts)
                if A[i] % A[j] == 0 and A[i] // A[j] in a:
                    if A[i] == A[j] ** 2:
                        dicts[A[i]] += dicts[A[j]] ** 2
                        dicts[A[i]] %= 10 ** 9 + 7
                    else:
                        c = dicts[A[j]] * dicts[A[i] // A[j]]
                        c %= 10 ** 9 + 7
                        dicts[A[i]] += 2 * c
                        dicts[A[i]] %= 10 ** 9 + 7
        print(dicts)
        ans = 0
        for key in dicts:
            ans += dicts[key]
            ans %= 10 ** 9 + 7
        return ans

    def numBinarydps_1(self, A):
        """
        562ms
        :param A:
        :return:
        """
        A.sort()
        dp = {}
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] / A[j] in dp:
                    dp[A[i]] += dp[A[j]] * dp[A[i] / A[j]]
        return sum(dp.values()) % (10 ** 9 + 7)
print(Solution().numFactoredBinaryTrees(A = [2, 4]))
print(Solution().numFactoredBinaryTrees(A = [2, 4, 5, 10]))
print(Solution().numFactoredBinaryTrees([18,3,6,2]))
