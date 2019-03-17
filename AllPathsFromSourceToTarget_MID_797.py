"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

    The number of nodes in the graph will be in the range [2, 15].
    You can print different paths in any order, but you should keep the order of nodes inside one path.


"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        282ms
        """
        memory = [[] for _ in range(len(graph))]
        def dfs(node):
            if node == len(graph) - 1:
                return [[node]]
            if memory[node] != []:
                return memory[node]
            for next_node in graph[node]:
                for i in dfs(next_node):
                    # print(node, i)
                    memory[node].append([node] + i)
            return memory[node]
        return dfs(0)

    def allPathsSourceTarget_1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        273ms
        """
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans
print(Solution().allPathsSourceTarget([[1,2], [3], [3], [4,5], [6], [6], []] ))
print(Solution().allPathsSourceTarget([[1,2], [], [], []] ))
print([1] + [4,2,2,3])


