"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
         296 ms
        """
        stack = set()
        dicts = {}
        start = -1
        ans = 0
        for i, t in enumerate(tree):
            if len(dicts) < 2:
                if t not in dicts:
                    stack.add(t)
            else:
                if t not in dicts:
                    min_key = [-1, float('inf')]
                    for key in stack: # 找到最小的位置
                        if dicts[key] < min_key[1]:
                            min_key = [key, dicts[key]]
                    stack.remove(min_key[0])
                    start = min_key[1]
                    del dicts[min_key[0]]
                    stack.add(t)
            dicts[t] = i
            ans = max(ans, i - start)
        return ans

    def totalFruit_1(self, tree):
        """
        180ms
        :param tree:
        :return:
        """
        res = cur = count_b = a = b = 0
        for c in tree:
            cur = cur + 1 if c in (a, b) else count_b + 1
            count_b = count_b + 1 if c == b else 1
            if b != c: a, b = b, c
            res = max(res, cur)
        return res
print(Solution().totalFruit([0,1,2,2]))
print(Solution().totalFruit([1,2,3,2,2]))
print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(Solution().totalFruit([0,0,0,0]))
print(Solution().totalFruit([0,0,1,0,1]))
print(Solution().totalFruit([1,1,6,5,6,6,1,1,1,1]))