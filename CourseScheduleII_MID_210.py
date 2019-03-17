"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        92ms
        """
        graph = [[] for _ in range(numCourses)]
        graph_inver = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
            graph_inver[y].append(x)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        def isOk():
            for i in range(numCourses):
                if not dfs(i):
                    return False
            return True

        if isOk():
            strat = []
            for i in range(len(graph_inver)):
                if len(graph_inver[i])==0:
                    strat.append(i)
            j=0
            while j<len(strat):
                strat.extend(graph[strat[j]])
                j+=1
            visit = [0 for _ in range(numCourses)]
            ans=[]
            for i in strat[::-1]:
                if visit[i]==0:
                    visit[i]=1
                    ans.append(i)
            return ans
        else:
            return []

    def findOrder_1(self, numCourses, prerequisites):
        # 85ms
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []

    def findOrder_2(self, numCourses, prerequisites):
        # 75ms
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []

    def findOrder_3(self, numCourses, prerequisites):
        # 65ms
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        print(graph)
        # 找出最基础的课程
        stack = [n for n in range(numCourses) if not graph[n]]
        print(stack)
        result = []
        # 所有基础课程的集合
        while stack:
            node = stack.pop()
            result.append(node)
            # 从以node为基础课的课程中，逐个删除node，来看是否已经达成前置条件
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    stack.append(n)
        return result if len(result) == numCourses else []
print(Solution().findOrder_3(4,[[1,0],[2,0],[3,1],[3,2]]))