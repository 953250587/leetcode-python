"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

    N will be an integer in the range [1, 30].
    K will be an integer in the range [1, 2^(N-1)].


"""


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            s = '0'
        else:
            s = '01'
            for i in range(N - 2):
                l = len(s) // 2
                half_1 = s[0: l]
                half_2 = s[l: ]
                a = half_2 + half_1
                s += a
        return int(s[K - 1])

    def kthGrammar_1(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        31ms
        """
        if N == 1:
            return 0
        where = [K]
        while K != 1:
            next_k = (where[-1] + 1) // 2
            where.append(next_k)
            K = next_k
        where.pop()
        start = 0
        for i in where[::-1]:
            if start == 0:
                if i % 2 == 0:
                    start = 1
                else:
                    start = 0
            else:
                if i % 2 == 0:
                    start = 0
                else:
                    start = 1
        return start


# print(Solution().kthGrammar(1, 1))
# print(Solution().kthGrammar(2, 1))
# print(Solution().kthGrammar(2, 2))
# print(Solution().kthGrammar(4, 5))
n = 10
for i in range(1, 2 ** (n - 1) + 1):
    if Solution().kthGrammar(n, i) != Solution().kthGrammar_1(n, i):
        print(i)


