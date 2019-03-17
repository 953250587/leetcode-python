"""
 Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        32ms
        """
        self.dicts={}
        count=0
        for i in equations:
            if i[0] not in self.dicts.keys():
                self.dicts[i[0]]=[(i[1],values[count])]
            else:
                self.dicts[i[0]].append((i[1],values[count]))
            if i[1] not in self.dicts.keys():
                self.dicts[i[1]] = [(i[0],1/values[count])]
            else:
                self.dicts[i[1]].append((i[0],1/values[count]))
            count+=1
        print(self.dicts)
        self.sets=set()

        self.flag=False
        def dfs(start_a,end_b):
            c=1
            self.sets.add(start_a)
            if start_a not in self.dicts.keys():
                return -1.0
            if start_a==end_b:
                return 1.0
            for i in self.dicts[start_a]:
                if i[0]==end_b:
                    self.flag=True
                    return i[1]
                if i[0] not in self.sets:
                    a=dfs(i[0],end_b)
                    if self.flag:
                        c *= i[1]*a
                        return c
            return -1.0

        result=[]
        for q in queries:
            self.flag = False
            self.sets=set()
            result.append(dfs(q[0],q[1]))
        return result

    def calcEquation_1(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        36ms
        """
        if len(equations) == 0 or len(values) == 0 or queries == 0:
            return []

        relation = {}
        for v in range(len(values)):
            e = equations[v]
            relation[e[0]] = relation.get(e[0], [])
            relation[e[0]].append([e[1], values[v]])

            if values[v] != 0:
                relation[e[1]] = relation.get(e[1], [])
                relation[e[1]].append([e[0], 1 / values[v]])

        # print relation
        result = []

        for q in queries:
            if q[0] not in relation.keys() or q[1] not in relation.keys():
                result.append(-1.0)

            else:
                result.append(self.dfs(relation, q[0], q[1], 1.0, []))

        return result

    def dfs(self, relation, up, down, multi, visited):

        # print "up: ",up,"  down: ",down, "  multi: ",multi

        if up == down:
            return 1.0

        visited.append(up)
        for d in relation[up]:
            if down == d[0]:
                return multi * d[1]

            if d[0] in visited:
                continue

            temp = self.dfs(relation, d[0], down, multi * d[1], visited)
            if temp != -1.0:
                return temp

        return -1.0


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(Solution().calcEquation(equations,values,queries))

equations = [ ["a", "b"], ["a", "c"],['a','d'],['b','h'],['h','c'],['h','m'],['b','g'],
              ['c','d'],['d','e'],['d','f']]
values = [1.0,2.0,3.0,1.0,2.0,12.0,3.0,1.5,2.0,4.0]
queries = [ ["f", "a"], ["b", "a"], ["a", "h"], ["a", "e"], ["b", "m"] ]
print(Solution().calcEquation(equations,values,queries))