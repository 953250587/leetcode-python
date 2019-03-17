"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
         72 ms
        """
        import collections
        dicts = collections.Counter(deck)
        # print(dicts)
        m = max(dicts.values())
        for i in range(2, m + 1):
            flag = True
            for key in dicts:
                if dicts[key] % i != 0:
                    flag = False
                    break
            if flag:
                return True
        return False

    def hasGroupsSizeX_1(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        36MS
        """
        dic = {}
        # 记录卡片总体情况
        for d in deck:
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1

        x = None
        for value in dic.values():
            if value > 1:
                a, b = value, x
                while b:  # 找出两个数的最小公约数
                    a, b = b, a % b
                if a > 1:
                    x = a  # 用最小公约数代替上一个数
                else:
                    return False
            else:
                return False

        return True

print(Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))
print(Solution().hasGroupsSizeX([1]))
print(Solution().hasGroupsSizeX([1,1]))
print(Solution().hasGroupsSizeX([1,1,2,2,2,2]))
