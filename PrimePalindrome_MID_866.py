"""
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

For example, 12321 is a palindrome.



Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101


Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""
"""
All palindrome with even digits is multiple of 11.

We can prove as follow:

11 % 11 = 0
1111 % 11 = 0
111111 % 11 = 0
11111111 % 11 = 0

So:
1001 % 11 = (1111 - 11 * 10) % 11 = 0
100001 % 11 = (111111 - 1111 * 10) % 11 = 0
10000001 % 11 = (11111111 - 111111 * 10) % 11 = 0

For any palindrome with even digits:
abcdeedcba % 11
= (a * 10000001 + b * 100001 * 10 + c * 1001 * 100 + d * 11 * 1000) % 11
= 0

All palindrome with even digits is multiple of 11.
So among them, 11 is the only one prime
if (8 <= N <= 11) return 11
For other, we consider only palindrome with odd dights.
"""

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        100MS
        """

        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0: return False
            return True

        if 8 <= N <= 11: return 11
        for x in range(10 ** (len(str(N)) / 2), 10 ** 5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y): return y

    def primePalindrome_1(self, N):
        """
        :type N: int
        :rtype: int
        40MS
        """
        from math import sqrt
        import copy

        lens = len(str(N))
        strN = str(N)
        collect = []
        mid = lens / 2 + 1
        evenBitPrime = {2: 101, 4: 10301, 6: 1003001, 8: 100030001}

        for bit in range(mid):
            tmp = int(strN[bit])
            collect.append(tmp)

        def checkfunc(numInt):
            high = int(sqrt(numInt))
            for i in range(2, high + 2):
                if numInt % i == 0:
                    return None
            return numInt

        def callback(numList, bit):
            if numList[bit] == 10:
                return None
            while (numList[bit] < 10):

                # consite palindrome
                numStr = ''.join(str(i) for i in numList)
                numInt = int(numStr + numStr[::-1][1:])

                # check if prime
                checkReturn = checkfunc(numInt)
                if checkReturn:

                    return checkReturn
                # next bit check
                if bit != mid - 1:
                    tmp = copy.deepcopy(numList)
                    test = callback(tmp, bit + 1)
                    if test:
                        return test
                numList[bit] += 1

        if N > 11:
            if lens % 2 == 0 and lens > 0 and N > 11:
                return evenBitPrime[lens]
            else:

                for i in range(mid - 1, -1, -1):
                    tmp = copy.deepcopy(collect)

                    if tmp[0] == 9 and i == 0:
                        return evenBitPrime[lens + 1]
                    tmp[i] += 1
                    for x in range(i + 1, mid): tmp[x] = 0

                    topReturn = callback(tmp, i)
                    if topReturn:
                        return topReturn
        elif 7 < N <= 11:
            return 11
        elif 5 < N:
            return 7
        elif 3 < N:
            return 5
        elif 2 < N:
            return 3
        else:
            return 2