"""
 In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:

Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array
"""


class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        104ms
        """
        import collections
        l = len(edges)
        node = [0] * (l + 1)
        dict = collections.defaultdict(list)
        dicts_edge = collections.defaultdict(list)
        for edge in edges:
            dict[edge[1]].append(edge[0])
            dicts_edge[edge[0]].append(edge[1])
            node[edge[1]] = 1
        root = 1
        for i in range(1, l + 1):
            if node[i] == 0:
                root = i
        visit = []
        self.cycle_start = 0
        print('root', root)
        def dfs(start):
            if start in visit:
                self.cycle_start = start
                return True
            visit.append(start)
            for i in dicts_edge[start]:
                if dfs(i):
                    return True
            visit.pop()
            return False

        iscycle = dfs(root)
        # print(visit)
        # print('cycle_start', self.cycle_start)
        if iscycle:
            for i in range(len(visit)):
                if visit[i] == self.cycle_start:
                    self.cycle = visit[i:]
                    break
            cycle_edge = list(zip(self.cycle, self.cycle.copy()[1:] + [self.cycle[0]]))
            # print('cycle_edge', cycle_edge)
        isdup = False
        dup = 0
        a = []
        for key in dict:
            if len(dict[key]) >= 2:
                isdup = True
                dup = key
                a = [dup, dict[dup]]
                break
        # print(iscycle, isdup)
        if iscycle and isdup:
            for i in a[1]:
                if (i, dup) in cycle_edge:
                    return [i, dup]
        elif isdup:
            return [a[1][-1], dup]
        else:
            for edge in edges[::-1]:
                if tuple(edge) in cycle_edge:
                    return edge

    def findRedundantDirectedConnection_1(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        80ms
        """
        back_to = -1
        n = len(edges)
        em = [[] for _ in range(n)]
        visited = [False] * n
        in_stk = [False] * n
        in_deg = [0] * n
        out_deg = [0] * n
        cycle = set()

        def dfs(nd):
            nonlocal back_to
            if in_stk[nd]:
                back_to = nd
                return True
            if visited[nd]:
                return False
            in_stk[nd] = True
            visited[nd] = True
            for to, i in em[nd]:
                if dfs(to):
                    if back_to != -1:
                        cycle.add(nd)
                        if back_to == nd:
                            back_to = -1
                    return True
            in_stk[nd] = False
            return False

        for i, (u, v) in enumerate(edges):
            em[u - 1].append((v - 1, i))
            in_deg[v - 1] += 1
            out_deg[u - 1] += 1

        for i in range(n):
            if dfs(i):
                for (u, v) in reversed(edges):
                    if v - 1 in cycle and u - 1 in cycle and in_deg[v - 1] > 1:
                        return [u, v]
                else:
                    for (u, v) in reversed(edges):
                        if v - 1 in cycle and u - 1 in cycle and out_deg[v - 1] > 1:
                            return [u, v]

        i = in_deg.index(2)
        for (u, v) in reversed(edges):
            if v == i + 1:
                return [u, v]

    class Solution(object):
        def findRedundantDirectedConnection(self, edges):
            """
            46ms
            :param edges:
            :return:
            """
            import collections
            N = len(edges)
            parent = {}
            candidates = []
            for u, v in edges:
                if v in parent:
                    candidates.append((parent[v], v))
                    candidates.append((u, v))
                else:
                    parent[v] = u

            def orbit(node):
                seen = set()
                while node in parent and node not in seen:
                    seen.add(node)
                    node = parent[node]
                return node, seen

            root = orbit(1)[0]

            if not candidates:
                cycle = orbit(root)[1]
                for u, v in edges:
                    if u in cycle and v in cycle:
                        ans = u, v
                return ans

            children = collections.defaultdict(list)
            for v in parent:
                children[parent[v]].append(v)

            seen = [True] + [False] * N
            stack = [root]
            while stack:
                node = stack.pop()
                if not seen[node]:
                    seen[node] = True
                    stack.extend(children[node])

            return candidates[all(seen)]



print(Solution().findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))
print(Solution().findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))
print(Solution().findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))
print(Solution().findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))


