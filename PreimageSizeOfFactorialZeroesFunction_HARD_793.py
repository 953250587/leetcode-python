"""
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.

Note:

    K will be an integer in the range [0, 10^9].


"""
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        35MS
        """
        if K == 0:
            return 5
        def trailingZeroes(n):
            if n == 0:
                return 0
            import math
            k = int(math.log(n, 5))
            ans = 0
            for i in range(1, k + 1):
                ans += n // 5 ** i
            return ans
        # 选择合适的最大位置，通过观测可以发现K*5必然比x大（f(x) = K）
        hight, low = K * 5, 5
        # 之后就是二分查找，如果有一定为5个连续的，否则就为0
        while low <=hight:
            mid = (low + hight) // 2
            a = trailingZeroes(mid)
            if a > K:
                hight = mid - 1
            elif a < K:
                low = mid + 1
            else:
                return 5


    def preimageSizeFZF_1(self, K):
        """
        :type K: int
        :rtype: int
        33ms
        """
        # 数学题，确定有多少个数字后面带K个0
        n = 4 * K
        count = 0
        while n != 0:
            count += n / 5
            n /= 5
        n = 4 * K
        # print count
        while count < K:
            n += 1
            t = n
            while t % 5 == 0:
                count += 1
                t /= 5
        # print n
        if count > K:
            return 0
        else:
            return 5

    def preimageSizeFZF_2(self, K):
        """
        :type K: int
        :rtype: int
        31ms
        """

        def nzero(n):
            f = 5
            cnt = 0
            while f <= n:
                cnt += n // f
                f *= 5
            return cnt

        if K == 0:
            return 5

        min = 1
        max = K * 5
        while min < max:
            mid = (min + max) // 2
            if nzero(mid) < K:
                min = mid + 1
            else:
                max = mid

        if nzero(min) != K:
            return 0
        else:
            # next = (min // 5 + 1) * 5
            # return next - min
            return 5
print(Solution().preimageSizeFZF(3))
print(Solution().preimageSizeFZF(0))
print(Solution().preimageSizeFZF(5))
print(Solution().preimageSizeFZF(1000000000))


def trailingZeroes(n):
    if n == 0:
        return 0
    import math
    k = int(math.log(n, 5))
    ans = 0
    for i in range(1, k + 1):
        ans += n // 5 ** i
    return ans
print(trailingZeroes(2018))
