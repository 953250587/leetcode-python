"""
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (ie. the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a draw.



Example 1:

Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0


Note:

3 <= graph.length <= 50
It is guaranteed that graph[1] is non-empty.
It is guaranteed that graph[2] contains a non-zero element.
"""


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        memory = {}

        def dfs(cat_position, mouse_position, time):
            # 判断是否已经结束，老鼠赢或者猫赢
            if mouse_position == 0: #or (time == 0 and 0 in graph[mouse_position]):
                return 1
            # print(cat_position)
            if mouse_position == cat_position:# or (time == 1 and mouse_position in graph[cat_position]):
                return 2
            # 判断是否已经遇到过这种情况
            if (cat_position, mouse_position, time) in memory:
                # 如果遇到过，并且是未求解出来的，说明循环了，可以跳出这种情况
                if memory[(cat_position, mouse_position, time)] == -1:
                    return 0
                # 否则返回记录值
                return memory[(cat_position, mouse_position, time)]
            # 记录下，这种情况开始考虑
            memory[(cat_position, mouse_position, time)] = -1
            # 所有可能发生的情况
            possible = []
            # 老鼠的回合
            if time == 0:
                for next_position in graph[mouse_position]:
                    temp = dfs(cat_position, next_position, 1)
                    possible.append(temp)
                    if temp == 1:
                        break
                    # if cat_position == 7 and mouse_position == 5:
                    #     print('possible_mouse:', possible, cat_position, next_position)
                    #     print(memory)
                    # if cat_position == 9 and mouse_position == 6:
                    #     print('possible_mouse_1:', possible, cat_position, next_position)
                    #     print(memory)

                # 如果存在一种方式使得老鼠赢，则最后是老鼠赢
                if 1 in possible:
                    flag = 1
                # 如果所有情况都是猫赢，则最后是猫赢
                elif 0 not in possible:
                    flag = 2
                else:
                    flag = 0

            else:
                # 这种情况类似
                for next_position in graph[cat_position]:
                    if next_position != 0:
                        temp = dfs(next_position, mouse_position, 0)
                        possible.append(temp)
                        if temp == 2:
                            break
                        # if cat_position == 9 and mouse_position == 5:
                        #     print('possible_cat:', possible, next_position, mouse_position)
                        #     print(memory)
                        # if cat_position == 7 and mouse_position == 6:
                        #     print('possible_cat_1:', possible, next_position, mouse_position)
                        #     print(memory)

                if 2 in possible:
                    flag = 2
                elif 0 not in possible:
                    flag = 1
                else:
                    flag = 0

            # used.remove((cat_position, mouse_position, time))
            memory[(cat_position, mouse_position, time)] = flag
            # print('flag:',flag, 'cat_position, mouse_position, time',cat_position, mouse_position, time)
            return flag



        temp = dfs(cat_position=2, mouse_position=1, time=0)
        a = sorted(memory.keys(), key=lambda a:(-a[0],a[1], a[2]))
        for i in a:
            print(i, ':', memory[i])
        return temp






# graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# print(Solution().catMouseGame(graph))
#
#
# graph = [[2],[5,4],[3],[4,5],[1,5],[1,4]]
# print(Solution().catMouseGame(graph))

graph = [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]
print(Solution().catMouseGame(graph))



class Solution(object):
    def catMouseGame(self, graph):
        """
        512 ms,
        :param graph:
        :return:
        """
        import collections
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int) # 默认平局

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([]) # 只存入确定的位置
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE  # 记录所有老鼠赢的位置
                queue.append((0, i, t, MOUSE))  # 记录老鼠赢的位置到队列中
                if i > 0:
                    color[i, i, t] = CAT  # 记录所有猫赢的位置
                    queue.append((i, i, t, CAT))  # 记录猫赢的位置到队列中

        # percolate
        while queue:  # 反推
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:  # 如果是平局，则有可能是还没遍历过的情况
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c:  # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1  # 确保不重复
                        if degree[i2, j2, t2] == 0:  # 平局情况
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]