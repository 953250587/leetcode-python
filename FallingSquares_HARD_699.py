"""
On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:

Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:


After the first drop of positions[0] = [1, 2]:
_aa
_aa
-------
The maximum height of any square is 2.


After the second drop of positions[1] = [2, 3]:
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
The maximum height of any square is 5.
The larger square stays on top of the smaller square despite where its center
of gravity is, because squares are infinitely sticky on their bottom edge.


After the third drop of positions[1] = [6, 1]:
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
The maximum height of any square is still 5.

Thus, we return an answer of [2, 5, 5].


Example 2:

Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.

Note:
1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
"""
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        708 ms
        """
        import bisect
        self.max = [0]
        recom = []
        for position in positions:
            m = 0
            big = []
            part = []
            end = position[0] + position[1] - 1
            for num,i in enumerate(recom):
                if i[0] <= position[0] and i[1] >= end:
                    m = max(m, i[2])
                    big.append(num)
                elif position[0] <= i[0] <= end or position[0] <= i[1] <= end:
                    m = max(m, i[2])
                    part.append(num)
            for b in big:
                a = recom[b]
                recom.remove(a)
                if position[0] != a[0]:
                    c = (a[0], position[0] - 1, a[2])
                    bisect.insort_right(recom, c)
                if end != a[1]:
                    c = (end + 1, a[1], a[2])
                    bisect.insort_right(recom, c)
            count = 0
            for p in part:
                p -= count
                a = recom[p]
                recom.remove(a)
                if position[0] > a[0]:
                    c = (a[0], position[0] - 1, a[2])
                    bisect.insort_right(recom, c)
                # bisect.insort_right(recom, (position[0], end, position[1] + m))
                elif end < a[1]:
                    c = (end + 1, a[1], a[2])
                    bisect.insort_right(recom, c)
                else:
                    count += 1
            bisect.insort_right(recom, (position[0], end, position[1] + m))
            self.max.append(max((position[1] + m), self.max[-1]))
            print(recom)
        return self.max[1:]

    def fallingSquares_1(self, positions):
        """
        461ms
        :param positions:
        :return:
        """
        sqs = []
        res = []
        if len(positions) == 0:
            return []
        sqs.append([positions[0][0], positions[0][0] + positions[0][1] - 1, positions[0][1]])
        res.append(positions[0][1])
        max_h = res[0]
        for i in range(1, len(positions)):
            l, r, h = positions[i][0], positions[i][0] + positions[i][1] - 1, positions[i][1]
            new_h = h
            for sq in sqs:
                if not (r < sq[0] or l > sq[1]):
                    new_h = max(sq[2] + h, new_h)
            max_h = max(max_h, new_h)
            sqs.append([l, r, new_h])
            res.append(max_h)
        return res

    def fallingSquares_2(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        79ms
        """
        import bisect
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            max_h = max(max_h, high)
            res.append(max_h)
        return res
# print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(Solution().fallingSquares([[1, 2], [4, 4], [9, 3], [2, 9], [6, 1]]))







