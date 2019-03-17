"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        255ms
        """
        if n == 1:
            return [0]
        dicts={i:set() for i in range(n)}
        for edge in edges:
            dicts[edge[1]].add(edge[0])
            dicts[edge[0]].add(edge[1])
        lists_leaf=[]
        for i in range(n):
            if len(dicts[i])==1:
                lists_leaf.append(i)
        # print(lists_leaf)
        # print(dicts)
        lists_leaf_copy=set()
        mark = [0 for i in range(n)]
        while len(dicts.keys())>2:
            for i in lists_leaf:
                m = list(dicts[i])[0]
                dicts[m].remove(i)
                if len(dicts[m])==1:
                   lists_leaf_copy.add(m)
            #     print(dicts)
            # print(lists_leaf_copy)
            for i in lists_leaf:
                del dicts[i]
            lists_leaf=list(lists_leaf_copy)
            lists_leaf_copy = set()
        return lists_leaf

    def findMinHeightTrees_1(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        109ms
        """

        if n == 1: return [0]
        adj = [set() for i in range(n)]

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: new_leaves.append(j)
            leaves = new_leaves
        return leaves



# n = 12
# edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4],[10,9],[9,3],[6,4],[8,4],[7,6],[11,10]]
# print(Solution().findMinHeightTrees(n,edges))

n = 4
edges = [[1,0],[1,2],[1,3]]
print(Solution().findMinHeightTrees(n,edges))