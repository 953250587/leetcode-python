"""
Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge.

Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge.

Return how many nodes you can reach in at most M moves.



Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output: 13
Explanation:
The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output: 23


Note:

0 <= edges.length <= 10000
0 <= edges[i][0] < edges[i][1] < N
There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
The original graph has no parallel edges.
0 <= edges[i][2] <= 10000
0 <= M <= 10^9
1 <= N <= 3000
"""
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        268 ms
        """
        import heapq
        import collections
        used = set()
        ans = 0
        dict_node = collections.defaultdict(dict)
        for edge in edges:
            dict_node[edge[0] + 1][edge[1] + 1] = edge[2]
            dict_node[edge[1] + 1][edge[0] + 1] = edge[2]
        start = [(-M, 1)]
        s = set([i + 1 for i in range(N)])
        while start:
            cur = heapq.heappop(start)
            if cur[-1] in used:
                continue
            if cur[-1] > 0:
                used.add(cur[-1])
            if cur[-1] in s:
                ans += 1
                # print(ans, cur[-1], -cur[0], used)
            # print(used, ans)
            # for key in dict_node:
            #     print(key, dict_node[key].keys())
            for node in dict_node[cur[-1]]:
                if node not in used:
                    val = dict_node[cur[-1]][node]
                    # print(cur[-1], node, val, ans)
                    if -cur[0] - val <= 0:
                        ans -= cur[0]
                        if node > 0:
                            dict_node[node][-cur[-1]] = dict_node[node][cur[-1]] + cur[0]
                    else:
                        ans += val
                        heapq.heappush(start, (cur[0] + val + 1, node))
                    # print('ans: ', ans)

        return ans

    def reachableNodes_1(self, edges, M, N):
        """
        208ms
        :param edges:
        :param M:
        :param N:
        :return:
        """
        import collections,heapq
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].iteritems():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, M - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, M + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans
print(Solution().reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3))
print(Solution().reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4))
print(Solution().reachableNodes([[2,4,2],[3,4,5],[2,3,1],[0,2,1],[0,3,5]],14,5))
print(Solution().reachableNodes([[0,2,0],[1,3,1],[0,1,0],[1,4,0],[0,4,0],[2,4,4],[2,3,6],[0,3,8],[3,4,1],[1,2,4]],4,5))





