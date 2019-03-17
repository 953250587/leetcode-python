"""
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""


class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        import collections
        import bisect
        start = [0, 0]
        pos = 0
        s_x = collections.defaultdict(list)
        s_y = collections.defaultdict(list)
        ans = 0
        flag = False
        for obstacle in obstacles:
            if obstacle[0] == obstacle[1] == 0:
                flag = True
                continue
            bisect.insort_left(s_x[obstacle[0]], obstacle[1])
            bisect.insort_left(s_y[obstacle[1]], obstacle[0])
        for i, command in enumerate(commands):
            if command > 0:
                if pos == 1:
                    a = start[0] + command
                    b = start[1]
                    y = bisect.bisect(s_y[b], start[0])
                    if y < len(s_y[b]):
                        y = min(s_y[b][y] - 1, a)
                    else:
                        y = a
                    x = b
                elif pos == 0:
                    a = start[0]
                    b = start[1] + command
                    x = bisect.bisect(s_x[a], start[0])
                    if x < len(s_x[a]):
                        x = min(s_x[a][x] - 1, b)
                    else:
                        x = b
                    y = a
                elif pos == 3:
                    a = start[0] - command
                    b = start[1]
                    y = bisect.bisect(s_y[b], start[0])
                    if y > 0:
                        y = max(s_y[b][y - 1] + 1, a)
                    else:
                        y = a
                    x = b
                else:
                    a = start[0]
                    b = start[1] - command
                    x = bisect.bisect(s_x[a], start[0])
                    if x > 0:
                        x = max(s_x[a][x - 1] + 1, b)
                    else:
                        x = b
                    y = a
                ans = max(ans, x ** 2 + y ** 2)
                start = [y, x]
                print(start, pos)
                if flag:
                    bisect.insort_left(s_x[0], 0)
                    bisect.insort_left(s_y[0], 0)
                    flag = False
            elif command == -1:
                pos += 1
                pos %= 4
            else:
                pos -= 1
                pos %= 4


        return ans

    def robotSim_1(self, commands, obstacles):
        """
        96ms
        :param commands:
        :param obstacles:
        :return:
        """
        i = j = mx = d = 0
        move, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0), ], set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                d = (d + 1) % 4
            elif command == -1:
                d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles: # 一步一步
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx
# import bisect
# print(bisect.bisect([0,0,1,2,3], 0))
print(Solution().robotSim(commands = [4,-1,3], obstacles = []))
print(Solution().robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
print(Solution().robotSim([7,-2,-2,7,5],
[[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]))
print(Solution().robotSim([-2,-1,-2,3,7],
[[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]))