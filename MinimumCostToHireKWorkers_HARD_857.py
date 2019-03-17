"""
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.


Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
         124 ms
        """
        import heapq
        ratio = [i / j for i, j in zip(wage, quality)]
        t = [(-i, j) for i, j in zip(quality, ratio)]
        t = sorted(t, key=lambda a:a[1])
        print(t)
        h = []
        ans = float('inf')
        acount = 0
        for i in range(K - 1):
            heapq.heappush(h, t[i])
            acount += -t[i][0]
        # print(acount)
        for i in range(K - 1, len(wage)):
            heapq.heappush(h, t[i])
            acount -= t[i][0]
            ans = min(ans, acount * t[i][1])
            acount += heapq.heappop(h)[0]
            # print(acount)
        # print(ans)
        return ans

    def mincostToHireWorkers_1(self, quality, wage, K):
        """
        327MS
        :param quality:
        :param wage:
        :param K:
        :return:
        """
        import heapq
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res
print(Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], K = 2))
print(Solution().mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3))
print(Solution().mincostToHireWorkers([3,1,10,10,1],[4,8,2,2,7],3))