"""
 Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

Note:

    L, R will be integers L <= R in the range [1, 10^6].
    R - L will be at most 10000.

"""
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        1138ms
        """
        def cal(s):
            sum_1 = 0
            for char in s:
                if char == '1':
                    sum_1 += 1
            return sum_1
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23}
        ans = 0
        for i in range(L, R + 1):
            if cal(bin(i)[2:]) in prime:
                ans += 1
        return ans

    def countPrimeSetBits_1(self, L, R):
        """
        1488ms
        :param L:
        :param R:
        :return:
        """
        count = 0
        for x in range(L, R + 1):
            num = bin(x).lstrip('-0b').zfill(8)
            setBit = str(num).count("1")
            if setBit != 1 and all(setBit % i for i in range(2, setBit)):
                count += 1
        return (count)

    def countPrimeSetBits_2(self, L, R):
        """
        63ms
        :param L:
        :param R:
        :return:
        """
        def under(m):
            count = 0
            K = 0
            for n in range(19, -1, -1):
                if m & (1 << n):
                    nCk = 1
                    for k in range(n + 1):
                        if k + K in {2, 3, 5, 7, 11, 13, 17, 19}:
                            count += nCk
                        nCk = nCk * (n - k) / (k + 1)
                    K += 1
            return count

        return under(R + 1) - under(L)
print(Solution().countPrimeSetBits(L = 6, R = 10))
print(Solution().countPrimeSetBits(L = 10, R = 15))