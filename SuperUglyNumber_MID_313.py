"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        872ms
        """
        ugly = [1]
        # i2, i3, i5 = 0, 0, 0
        K=len(primes)
        I=[0 for k in range(K)]
        while n > 1:
            # u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            U=[primes[i]*ugly[I[i]] for i in range(K)]
            print(U)
            umin = min(U)
            for i in range(K):
                if umin==U[i]:
                    I[i]+=1
            # if umin == u2:
            #     i2 += 1
            # if umin == u3:
            #     i3 += 1
            # if umin == u5:
            #     i5 += 1
            ugly.append(umin)
            n -= 1
            print(ugly)
        return ugly[-1]
# primes = [2, 7, 13, 19]
# print(Solution().nthSuperUglyNumber(12,primes))

import heapq


class Solution_1(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        266ms
        """
        # the next ugly number will be product of a previous ugly number and a prime number
        # multiply each prime with a previous ugly and keep the min as next ugly. but there may be duplicates, like 2*7, 7*2. keep k pointers to record where each prime has its last product kept as a ugly number and skip duplicates.
        # add a list of ugly number candidate to one loop
        # use heap so we don't need to find min everytime
        # n = 4
        # primes= [2]
        idx = [0] * len(primes)
        cand = []
        for k, p in enumerate(primes):
            heapq.heappush(cand, (p, k))  # heap will keep smallest p tuple on top
        print(cand)
        ugly = [1] * n
        lastPrime = [0] * n  # record the last prime number multiplied to this ugly number.

        for i in range(1, n):
            ugly[i], k = heapq.heappop(cand)
            lastPrime[i] = k
            idx[k] += 1

            # 跳到所有因数不大于primes[k]的位置，确保不会重复
            while lastPrime[idx[k]] > k:
                print(lastPrime)
            # e.g. primes = [2,7] ugly=[1, 1*2, 2*2, 1*7, 2*2*2, 2*7], lastPrime = [0, 0, 0, 1, 0, 1]. always have the larger prime multiply smaller prime and not the other way around to avoid duplicates
                print(k, idx)
                idx[k] += 1
                print(k,idx)
                print(ugly)
            heapq.heappush(cand, (primes[k] * ugly[idx[k]], k))
            print(cand)
        return ugly[n - 1]

primes = [2, 7, 13, 19]
print(Solution_1().nthSuperUglyNumber(12,primes))
