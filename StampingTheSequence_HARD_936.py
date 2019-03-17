"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.



Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]


Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""


class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        244 ms
        """
        import collections
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in range(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in range(max(0, i - M + 1), min(N - M, i) + 1):
                if i in A[j][1]:  # This window is affected
                    A[j][1].discard(i)  # Remove it from do list of this window
                    if not A[j][1]:  # do list of this window is empty
                        ans.append(j)
                        for m in A[j][0]:  # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []

    def movesToStamp_1(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        1348 ms
        """
        import collections
        if stamp[0] != target[0] or stamp[-1] != target[-1]:
            return []
        m = len(stamp)
        n = len(target)
        dicts = collections.defaultdict(list)
        for i, key in enumerate(stamp):
            dicts[key].append(i)
        # 用来记录target对应与stamp的位置信息
        path = [0] * n
        def dfs(target_position, stamp_index):
            path[target_position] = stamp_index
            # 最后一个位置一定是stamp的最后一个
            if target_position == n - 1:
                return stamp_index == m - 1
            posibile_stamp_index = set()
            # stamp最后一个
            if stamp_index == m - 1:
                # 取交集
                posibile_stamp_index = posibile_stamp_index.union(dicts[target[target_position + 1]])
            # 连续的情况
            elif stamp[stamp_index + 1] == target[target_position + 1]:
                posibile_stamp_index.add(stamp_index + 1)
            # stamp第一个
            if stamp[0] == target[target_position + 1]:
                posibile_stamp_index.add(0)
            return any(dfs(target_position + 1, j) for j in posibile_stamp_index)

        temp = dfs(0, 0)
        # print('path:', path)
        if not temp:
            return []
        # 根据path信息来选择如何操作
        def path2res(path):
            # up是从前往后，down是从后往前
            down, up = [], []
            for i in range(len(path)):
                if path[i] == 0:
                    up.append(i)
                # 不连续的时候
                elif i and path[i] - 1 != path[i - 1]:
                    down.append(i - path[i])
            return down[::-1] + up
        return path2res(path)


print(Solution().movesToStamp_1(stamp = "abc", target = "ababc"))
print(Solution().movesToStamp_1(stamp = "abca", target = "aabcaca"))
print(Solution().movesToStamp_1(stamp = "abc", target = "abcabcbc"))
print(Solution().movesToStamp_1(stamp = "abc", target = "ababcabc"))
print(Solution().movesToStamp_1("v", "v"))
print(Solution().movesToStamp_1("v", "vvvv"))
print(Solution().movesToStamp_1("aye", "eyeye"))
print(Solution().movesToStamp_1("cab", "cabbb"))