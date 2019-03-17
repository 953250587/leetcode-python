"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14

Note:

    board will be a 2 x 3 array as described above.
    board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].


"""


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        91ms
        """
        import collections
        self.dicts = collections.defaultdict(set)
        # self.dicts[(1, 2, 3, 4, 5, 0)] = 0
        cur_state = board[0] + board[1]
        print(cur_state)
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    pos = [i, j]
                    break
        def bfs(cur_state, pos):
            cur_list = [(cur_state, pos)]
            print('cur', cur_state, pos)
            dics = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            count = 0
            while cur_list:
                next_list = []
                for i in cur_list:
                    if tuple(i[0]) == (1, 2, 3, 4, 5, 0):
                        return count
                    cur_state = i[0]
                    pos = i[1]
                    for dic in dics:
                        x = pos[0] + dic[0]
                        y = pos[1] + dic[1]
                        if x >= 0 and y >= 0 and x < 2 and y < 3:
                            c_cur_state = cur_state.copy()
                            c_cur_state[3 * pos[0] + pos[1]] = c_cur_state[3 * x + y]
                            c_cur_state[3 * x + y] = 0
                            key = tuple(c_cur_state)
                            if key not in self.dicts:
                                self.dicts[key] = 1
                                next_list.append((c_cur_state, [x, y]))
                cur_list = next_list
                count += 1
                # print(cur_list, self.dicts)
            return -1
        return bfs(cur_state, pos)
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
print(Solution().slidingPuzzle([[3,2,4],[1,5,0]]))
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))