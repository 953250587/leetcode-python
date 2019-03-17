"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0


Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        144 ms
        """
        import collections
        # 存储对应行列的石头位置
        dicts_row = collections.defaultdict(list)
        dicts_column = collections.defaultdict(list)
        for stone in stones:
            dicts_row[stone[0]].append(stone[1])
            dicts_column[stone[1]].append(stone[0])

        # print(dicts_row)
        # print(dicts_column)
        used = set()
        def bfs(stone):
            start = set()
            start.add(stone)
            # 记录bfs搜索的个数
            count = 0
            while start:
                # print(start)
                # print(used)
                count += len(start)
                next_start = set()
                for st in start:
                    for column in dicts_row[st[0]]:
                        if (st[0], column) not in used:
                            next_start.add((st[0], column))
                            used.add((st[0], column))
                    for row in dicts_column[st[1]]:
                        if (row, st[1]) not in used:
                            next_start.add((row, st[1]))
                            used.add((row, st[1]))
                start = next_start
            return count

        result = 0
        # 对于每一个不同的bfs搜索区域，只会留下1个石头，其他都能删除
        for stone in stones:
            if (stone[0], stone[1]) not in used:
                used.add((stone[0], stone[1]))
                count = bfs((stone[0], stone[1]))
                result += count - 1
        return result


print(Solution().removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(Solution().removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(Solution().removeStones(stones = [[0,0]]))
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]))


class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        """
        116ms
        :param stones:
        :return:
        """
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})


