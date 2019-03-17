"""
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
"""


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        162 ms
        """
        N = len(graph)
        new_g = [set() for _ in range(N)]
        for i in range(N):
            for j in graph[i]:
                new_g[i].add(j)
                new_g[j].add(i)
        graph = new_g

        M = (1 << N)
        dp = [[-1] * N for _ in range(M)]
        # print(dp)

        q = []
        for i in range(N):
            # initial states contains all nodes and related states with only one node visited.
            dp[1 << i][i] = 0
            q.append((i, 1 << i))

        while q:
            node, state = q.pop(0)
            # print(node)
            steps = dp[state][node]
            for x in graph[node]:
                new_state = state | (1 << x)

                # Since all edges have equal distance, BFS is already optimal, so never overwrite
                if dp[new_state][x] == -1:
                    dp[new_state][x] = steps + 1
                    q.append((x, new_state))
        return min(dp[-1])


print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))
print(Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))

