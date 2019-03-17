"""
 There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        162ms
        """
        import heapq
        import numpy as np
        pq = []
        adj = [[] for _ in range(N + 1)]
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        print(np.array(adj))

        fin, res = set(), 0
        heapq.heappush(pq, (0, K))

        while len(pq) and len(fin) != N:
            cur = heapq.heappop(pq)
            fin.add(cur[1])
            res = cur[0]
            for child, t in adj[cur[1]]:
                if child in fin: continue
                heapq.heappush(pq, (t + cur[0], child))

        return res if len(fin) == N else -1
times= [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))
#
# times = [[1,2,1]]
# N = 2
# K = 1
# print(Solution().networkDelayTime(times, N, K))

# times= [[2,1,1],[2,3,1],[3,1,1]]
# N = 4
# K = 2
# print(Solution().networkDelayTime(times, N, K))
#
# times = [[1,2,1]]
# N = 2
# K = 2
# print(Solution().networkDelayTime(times, N, K))
#
# times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
# N = 5
# K = 5
# print(Solution().networkDelayTime(times, N, K))