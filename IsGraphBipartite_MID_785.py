"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.



Note:

    graph will have length in range [1, 100].
    graph[i] will contain integers in range [0, graph.length - 1].
    graph[i] will not contain i or duplicate values.
    The graph is undirected: if any element j is in graph[i], then i will be in graph[j].


"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        514ms
        """
        # 用来存放两边的节点
        subsets_A = set()
        subsets_B = set()
        # 用来存放用过的节点
        used = set()
        # 从0号节点开始考虑
        for i in range(len(graph)):
            if i not in used:
                # 没使用过的节点放到A中
                subsets_A.add(i)
                # 当前的节点集合
                cur_list = [i]
                # 用来记录是放在A还是B
                count = 0
                while cur_list:
                    next_list = []
                    # 对所有与第i个节点相连的节点都只能放到对面
                    for j in cur_list:
                        used.add(j)
                        for opposite in graph[j]:
                            # 当前节点都是A中的，与之相连的只能放到B里，如果有在A里的就无法满足题目要求
                            if count % 2 == 0:
                                if opposite in subsets_A:
                                    return False
                                subsets_B.add(opposite)
                            # 当前节点都是B中的，与之相连的只能放到A里，如果有在B里的就无法满足题目要求
                            else:
                                if opposite in subsets_B:
                                    return False
                                subsets_A.add(opposite)
                            # 只记录没被使用过的节点
                            if opposite not in used:
                                next_list.append(opposite)
                    # 当前节点变化，从A->B或则从B->A
                    count += 1
                    cur_list = next_list
        return True

    def isBipartite_1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        50ms
        """
        import collections
        src, ss = 0, len(graph[0])
        for i, v in enumerate(graph):
            if len(v) > ss:
                src, ss = i, len(v)

        colors = [-1] * len(graph)
        colors[src] = 1

        q = collections.deque([src])
        while len(q) > 0:
            cur = q.popleft()
            for v in graph[cur]:
                if colors[v] == -1:
                    colors[v] = 1 - colors[cur]
                    q.append(v)
                elif colors[v] == colors[cur]:
                    return False
        return True

    def isBipartite_2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        57ms
        """

        def dfs(v, cur_color):
            # 如果v再次出现，则判断是不是是在同一边，不是同一边返回False
            if v in color:
                return color[v] == cur_color
            # 否则记录v的分在哪边
            color[v] = cur_color
            # cur_color ^ 1 用来转化A->B,或则B->A
            return all(dfs(w, cur_color ^ 1) for w in graph[v])

        color = {}
        # 如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
        return all(dfs(v, 0) for v in range(len(graph)) if v not in color)
print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))
print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))

