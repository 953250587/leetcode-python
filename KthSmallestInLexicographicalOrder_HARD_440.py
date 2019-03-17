"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10
"""
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        43ms
        """

        self.sets = set()
        for i in range(1, 10):
            self.sets.add(int('1' * i))
        def dfs(pos, n, k):
            # print(pos, n, k)
            if k <= 0:
                return ''
            if pos == 0:
                START = 1
            else:
                START = 0
            if n < 10:
                return str(k - (1 - START))
            s = str(n)
            l = len(s)
            dicts = {}
            for i in range(START, 10):
                start = int(s[0])
                if i < start:
                    dicts[i] = int('1' * l)
                else:
                    dicts[i] = int('1' * (l - 1) if l - 1 > 0 else 0)
            count = 1
            for char in s[1:]:
                count += int(char) * 10 ** (l - 2)
                l -= 1
            dicts[int(s[0])] += count
            print(dicts, k, n)

            for i in range(START, 10):
                a = dicts[i]
                k -= a
                if k <= 0:
                    # print('ggggg', i)
                    k += a
                    k -= 1
                    l = len(str(a)) - 1
                    if a in self.sets:
                        return str(i) + dfs(pos + 1, int('9' * l if l > 0 else 0), k)
                    else:
                        a = int(s[1:])
                        if a == 0:
                            k -= 1
                            if k == 0:
                                return str(i) + str(a)
                            return str(i) + dfs(pos + 1, int('9' * l if l > 0 else 0), k)
                        else:
                            return str(i) + dfs(pos + 1, a, k)
        return dfs(0, n, k)

    def findKthNumber_1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        45ms
        """
        ans = 1
        k -= 1
        while k > 0:
            gap = self.findGap(n, ans, ans + 1)
            if gap <= k:
                ans += 1
                k -= gap
            else:
                ans *= 10
                k -= 1
        return ans

    def findGap(self, n, p, q): # 计算连续2个开始值之间的个数，比如p=1，q=2，先算1-2之间有1个
                                # 然后为10-20之间有10个，100-200以此类推，最大到n+1
        gap = 0
        while p <= n:
            gap += max(0, min(n + 1, q) - p)
            p *= 10
            q *= 10
        return gap

    def findKthNumber_2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        33ms
        """
        if n < 10:
            return k
        start = 1
        k -= 1
        while k > 0:
            first = start
            last = first + 1
            step = 0
            while first <= n:
                step += min(n + 1, last) - first
                first = first * 10
                last = last * 10
            print(start, step, k)
            if step <= k:
                k -= step
                start += 1
            else:
                k -= 1
                start *= 10
        return start



# print(Solution().findKthNumber(2234, 100))
# print(Solution().findKthNumber(13, 4))
# print(Solution().findKthNumber(113, 4))
# print(Solution().findKthNumber(1, 1))
# print(Solution().findKthNumber(8, 5))
# print(Solution().findKthNumber(100, 10))
# print(Solution().findKthNumber(10000, 1))
# print(Solution().findKthNumber(10000, 10))
print(Solution().findKthNumber(10, 2))

import math


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        48ms
        """

        def getSize(node, max_v):
            right_bound = node + 1
            rval = 0
            while node <= max_v:
                rval += min(max_v + 1, right_bound) - node
                right_bound, node = right_bound * 10, node * 10
            return rval

        prefix = 1
        while k > 0:
            size = getSize(prefix, n)

            if size < k:
                k -= size
                prefix += 1
            else:
                k -= 1
                if k > 0:
                    prefix *= 10

        return prefix