"""
 Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:

Input: m = 3, n = 3, k = 5
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Example 2:

Input: m = 2, n = 3, k = 6
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).

Note:

    The m and n will be in the range [1, 30000].
    The k will be in the range [1, m * n]

"""


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        import bisect
        def Count(num, m, n):
            count = 0
            ans = 0
            for i in range(1, m + 1):
                a = min(num // i, n)
                count += a
                ans = max(ans, a * i)
            return count, ans

        start, end = 1, m * n
        result = []
        dicts = {}
        while start <= end:
            mid = (start + end) // 2
            c, ans = Count(mid, m, n)
            print(mid, c, ans)
            dicts[c] = ans
            result.append(c)
            if c > k:
                end = mid - 1
            elif c < k:
                start = mid + 1
            else:
                return ans
        # return ans if c >= k else ans + 1
        a = sorted(result)
        # print(a)
        pos = bisect.bisect_right(a, k)
        print(dicts)
        return dicts[a[pos]]

    def findKthNumber_1(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        1858ms
        """
        def Count(num, m, n):
            count = 0
            ans = 0
            for i in range(1, m + 1):
                a = min(num // i, n)
                count += a
                ans = max(ans, a * i)
            return count, ans

        start, end = 1, m * n
        while start < end:
            mid = (start + end) // 2
            c, ans = Count(mid, m, n)
            if c < k:
                start = mid + 1
            else:
                end = mid
        return start

    def findKthNumber_2(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        477ms
        """

        def countLessThan(x, m, n):
            assert m <= n
            count = 0
            for i in range(1, m + 1):
                if x // i < n:
                    count += x / i
                else:
                    count += n
            return count

        if m > n:
            m, n = n, m
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if countLessThan(mid, m, n) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
# print(Solution().findKthNumber(3, 3, 5))
# print(Solution().findKthNumber(2, 3, 6))
print(Solution().findKthNumber_1(45, 12, 471))
# lists = []
# import numpy as np
# for i in range(1, 12):
#     lists.extend(i * np.array([i for i in range(1, 14)]))
# print(23 in lists)
# print(sorted(lists)[400])

print(Solution().findKthNumber_1(11, 13, 57))
print(Solution().findKthNumber_1(42, 34, 401))