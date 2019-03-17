"""
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8


Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000

"""


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
         144 ms
        """
        import heapq
        def gcd(A, B):
            if B == 0:
                return A
            return gcd(B, A % B)
        if A < B:
            A, B = B, A
        c = gcd(A, B)
        maxmin = A * B // c
        t1 = maxmin // A + maxmin // B - 1
        d = N // t1
        r = N % t1
        s = d * (maxmin )
        print(d, r, maxmin, s)
        if r == 0:
            return s % (10**9 + 7)
        h = [s + B, s + A]
        while r > 0:
            g = heapq.heappop(h)
            heapq.heappush(h, g + (A if g % A == 0 else B))
            r -= 1

        return g % (10**9 + 7)

    def nthMagicalNumber_1(self, N, A, B):
        """
        28MS
        :param N:
        :param A:
        :param B:
        :return:
        """
        from fractions import gcd
        MOD = 10 ** 9 + 7
        L = A / gcd(A, B) * B

        def magic_below_x(x):
            # How many magical numbers are <= x?
            return x / A + x / B - x / L

        lo = 0
        hi = 10 ** 15
        while lo < hi:
            mi = (lo + hi) / 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi

        return lo % MOD
# print(Solution().nthMagicalNumber(N = 1, A = 2, B = 3))
# print(Solution().nthMagicalNumber(N = 4, A = 2, B = 3))
# print(Solution().nthMagicalNumber(N = 5, A = 2, B = 4))
# print(Solution().nthMagicalNumber(N = 3, A = 6, B = 4))
# print(Solution().nthMagicalNumber(7,5,8))
# print(Solution().nthMagicalNumber(1000000000,39999,40000))
print(Solution().nthMagicalNumber(1000000000,40000,40000))
