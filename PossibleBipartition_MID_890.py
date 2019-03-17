"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        212 ms
        """
        import collections
        group = [set(), set()]
        used = set()

        dicts = collections.defaultdict(set)
        for dislike in dislikes:
            dicts[dislike[0]].add(dislike[1])
            dicts[dislike[1]].add(dislike[0])
        print(dicts)
        for key in range(1, N + 1):
            if key not in used:
                group[0].add(key)
                start = dicts[key]
                used.add(key)
                i = 0
                while start:
                    next_start = set()
                    # print(start, i)
                    for key in start:
                        if key not in used:
                            group[(i + 1) % 2].add(key)
                            used.add(key)
                            for k in dicts[key]:
                                next_start.add(k)
                        else:
                            if key in group[i % 2]:
                                return False
                    i += 1
                    start = next_start
        return True

    def possibleBipartition_1(self, N, dislikes):
        """
        180ms
        :param N:
        :param dislikes:
        :return:
        """
        import collections
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)
print(Solution().possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]]))
print(Solution().possibleBipartition(N = 3, dislikes = [[1,2],[1,3],[2,3]]))
print(Solution().possibleBipartition(N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]))



