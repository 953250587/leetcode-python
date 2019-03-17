"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
         204 ms
        """
        import collections
        if len(hand) % W != 0:
            return False
        maps = collections.Counter(hand)
        print(maps)
        start = sorted(maps.keys(), reverse = True)
        while start:
            for i in range(W):
                key = start[-1] + i
                if key not in maps or maps[key] <= 0:
                    # print(i, key, start, key not in maps, maps[key])
                    return False
                else:
                    maps[key] -= 1
            while start and maps[start[-1]] <= 0:
                start.pop()
        return True

    def isNStraightHand_1(self, hand, W):
        """
        198ms
        :param hand:
        :param W:
        :return:
        """
        import collections
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(W)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
print(Solution().isNStraightHand(hand = [1,2,3,6,2,3,4,7,8,9,10,12], W = 3))
print(Solution().isNStraightHand(hand = [1,2,3,4,5], W = 4))
