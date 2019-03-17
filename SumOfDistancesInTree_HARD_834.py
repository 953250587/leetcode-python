"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

Note: 1 <= N <= 10000

"""


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
         572 ms
        """
        edge = [[] for _ in range(N)]
        for i in edges:
            edge[i[0]].append(i[1])
            edge[i[1]].append(i[0])
        used = set()
        dicts = {i: [0, 0, -1] for i in range(N)}

        def dfs(i, j):
            # print i
            dicts[i][2] = j
            used.add(i)
            for e in edge[i]:
                if e not in used:
                    a = dfs(e, i)
                    dicts[i][0] += a[0] + 1
                    dicts[i][1] += a[1] + a[0] + 1
            return dicts[i]

        result = [0 for i in range(N)]
        for i in range(N):
            if i not in used:
                dfs(i, -1)
        print(dicts)
        result[0] = dicts[0][1]
        next_node = edge[0]
        used = set()
        used.add(0)

        while next_node:
            pare_node = []
            for i in next_node:
                used.add(i)
                parent = dicts[i][2]
                t = dicts[parent][1] - (dicts[i][0] + dicts[i][1] + 1)
                leave = dicts[parent][0] - (dicts[i][0] + 1)
                a = dicts[i][1] + leave + t + 1
                b = dicts[i][0] + leave + 1
                dicts[i][0] = b
                dicts[i][1] = a
                result[i] = dicts[i][1]
                for node in edge[i]:
                    if node not in used:
                        pare_node.append(node)
            next_node = pare_node
        return result

    def sumOfDistancesInTree_1(self, N, edges):
        """
        451ms
        :param N:
        :param edges:
        :return:
        """
        import collections
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [0] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    dfs(i, seen)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
            count[root] += 1

        def dfs2(root=0, seen=set()):
            seen.add(root)
            for i in tree[root]:
                if i not in seen:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, seen)

        dfs()
        dfs2()
        return res
print(Solution().sumOfDistancesInTree(N = 8, edges = [[0,1],[0,2],[2,3],[2,4],[2,5],[3,6],[3,7]]))
print(Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))