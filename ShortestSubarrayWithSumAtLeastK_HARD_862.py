"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        1372 ms
        """
        import heapq
        N = len(A)
        B = [0] * (N + 1)
        h = []
        ans = N + 1
        heapq.heappush(h, (B[0], 0))
        for i in range(N):
            B[i + 1] = B[i] + A[i]
            while h and h[0][0] <= B[i + 1] - K:
                a = heapq.heappop(h)
                ans = min(ans, i + 1 - a[1])
            heapq.heappush(h, (B[i + 1], i + 1))
        if ans == N + 1:
            return -1
        else:
            return ans




    def shortestSubarray_1(self, A, K):
        """
        616 ms
        :param A:
        :param K:
        :return:
        """
        import collections
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i, v in enumerate(B):
            while d and B[d[0]] <= v - K: # 从左边开始找到满足要求的位置为止
                res = min(res, i - d.popleft())
            while d and v <= B[d[-1]]: # 只留下最近的一个
                d.pop()
            d.append(i)
        return res if res <= N else -1
print(Solution().shortestSubarray(A = [1], K = 1))
print(Solution().shortestSubarray(A = [1,2], K = 4))
print(Solution().shortestSubarray_1(A = [2,-1,2], K = 3))
print(Solution().shortestSubarray([58701,23101,6562,60667,20458,-14545,74421,54590,84780,63295,33238,-10143,-35830,-9881,67268,90746,9220,-15611,23957,29506,-33103,-14322,19079,-34950,-38551,51786,-48668,-17133,5163,15122,5463,74527,41111,-3281,73035,-28736,32910,17414,4080,-42435,66106,48271,69638,14500,37084,-9978,85748,-43017,75337,-27963,-34333,-25360,82454,87290,87019,84272,17540,60178,51154,19646,54249,-3863,38665,13101,59494,37172,-16950,-30560,-11334,27620,73388,34019,-35695,98999,79086,-28003,87339,2448,66248,81817,73620,28714,-46807,51901,-23618,-29498,35427,11159,59803,95266,20307,-3756,67993,-31414,11468,-28307,45126,77892,77226,79433],1677903))
a = [58701,23101,6562,60667,20458,-14545,74421,54590,84780,63295,33238,-10143,-35830,-9881,67268,90746,9220,-15611,23957,29506,-33103,-14322,19079,-34950,-38551,51786,-48668,-17133,5163,15122,5463,74527,41111,-3281,73035,-28736,32910,17414,4080,-42435,66106,48271,69638,14500,37084,-9978,85748,-43017,75337,-27963,-34333,-25360,82454,87290,87019,84272,17540,60178,51154,19646,54249,-3863,38665,13101,59494,37172,-16950,-30560,-11334,27620,73388,34019,-35695,98999,79086,-28003,87339,2448,66248,81817,73620,28714,-46807,51901,-23618,-29498,35427,11159,59803,95266,20307,-3756,67993,-31414,11468,-28307,45126,77892,77226,79433]
b = 1677903
# print(Solution().shortestSubarray(a, 1677903))

def find_k(k, A, K):
    s = 0
    for i, a in enumerate(A):
        if i >= k:
            s -= A[i - k]
        s += a
        if s >= K:
            return True
    return False
print(find_k(48, a, b))
print(Solution().shortestSubarray_1(a, b))