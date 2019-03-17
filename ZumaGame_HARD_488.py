"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Note:

    You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
    The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
    The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
    Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.

"""
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        70ms
        """
        import collections
        new_board = []
        cur = board[0]
        count = 1
        for b in board[1:]:
            if cur == b:
                count += 1
            else:
                new_board.append((cur, count))
                cur = b
                count = 1
        new_board.append((cur, count))
        new_hand = collections.Counter(hand)
        print(new_hand['R'])
        print(new_board)
        self.ans = float('inf')

        def dfs(board, hand, count):
            # print(count, board, self.ans)
            l_board = len(board)
            for j in range(l_board):
                key = board[j][0]
                need_num = 3 - board[j][1]

                if need_num <= hand[key]:
                    hand[key] -= need_num
                    count += need_num
                    stack = board[0 : j]
                    leave = board[j + 1: ]
                    # if count == 1:
                    #     print(count, key, stack, leave)
                    for i in leave:
                        if stack and stack[-1][0] == i[0]:
                            a = stack.pop()
                            val = a[1] + i[1]
                            if val <= 2:
                                stack.append((i[0], val))
                        else:
                            stack.append(i)
                    if not stack:
                        self.ans = min(self.ans, count)
                        count -= need_num
                        hand[key] += need_num
                        return
                    dfs(stack, hand, count)
                    count -= need_num
                    hand[key] += need_num
            return
        dfs(new_board, new_hand, 0)
        return self.ans if self.ans < float('inf') else -1

    def findMinStep_1(self, board, hand):
        """
        49ms
        :param board:
        :param hand:
        :return:
        """
        import collections
        hm = collections.defaultdict(int)
        for b in hand:
            hm[b] += 1

        def longestConsecutive(board):
            start, s, e = 0, 0, 0
            for i in range(len(board)):
                if board[i] != board[start]:
                    start = i
                if i - start > e - s:
                    s, e = start, i
            return (s, e)

        def minStep(board):
            i, n, localMin = 0, len(board), float('inf')
            if n == 0: return 0
            start, end = longestConsecutive(board)
            if end - start > 1:
                return minStep(board[:start] + board[end + 1:])
            while i < n:
                ball, step = board[i], 1 if i < n - 1 and board[i] == board[i + 1] else 2
                if hm[ball] >= step:
                    hm[ball] -= step
                    ms = minStep(board[:i] + board[i + 3 - step:])
                    localMin = min(localMin, (step + ms) if ms != -1 else localMin)
                    hm[ball] += step
                i += 3 - step
            return localMin if localMin != float('inf') else -1

        return minStep(board)



# print(Solution().findMinStep("WWRRBBWW", "WRBRW"))
# print(Solution().findMinStep("WRRBBW", "RB"))
# print(Solution().findMinStep("G", "GGGGG"))
# print(Solution().findMinStep("RBYYBBRRB", "YRBGB"))
# print(Solution().findMinStep("GGYYBRGGRYBYGGYRRGGR","RYYBG"))
# print(Solution().findMinStep("GGYYBRGGRYBYG", "RYYBG"))
print(Solution().findMinStep("WWYYWYYWWRRYWY", "RWWWY"))

# def bfs(board, hand):
#     board_hand_list = [[board, hand]]
#     count = 0
#     while board_hand_list:
#         count += 1
#         l = len(board_hand_list)
#         num = 0
#         next_board_hand_list_set = set()
#         next_board_hand_list = []
#         while num < l:
#             board = board_hand_list[num][0]
#             hand = board_hand_list[num][1]
#             for cur_hand in ['W', 'R', 'Y', 'B', 'G']:
#                 if cur_hand in hand:
#                     hand.remove(cur_hand)
#                 else:
#                     continue
#                 l_board = len(board)
#                 for j in range(l_board + 1):
#                     stack = board[0:j]
#                     leave = [(cur_hand, 1)] + board[j:]
#                     for i in leave:
#                         if stack and stack[-1][0] == i[0]:
#                             a = stack.pop()
#                             val = a[1] + i[1]
#                             if val <= 2:
#                                stack.append((i[0], val))
#                         else:
#                             stack.append(i)
#                     if not stack:
#                         return count
#                     next_board = stack
#                     s_board = ''.join([i[0] * i[1] for i in next_board])
#                     s_hand = ''.join(hand)
#                     if (s_board, s_hand) not in next_board_hand_list_set:
#                         next_board_hand_list_set.add((s_board, s_hand))
#                         next_board_hand_list.append([next_board, hand[:]])
#                 hand.append(cur_hand)
#                 hand = sorted(hand)
#             num += 1
#         board_hand_list = next_board_hand_list
#     return -1