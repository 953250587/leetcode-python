"""
You are installing a billboard and want it to have the largest height.  The billboard will have two steel supports, one on each side.  Each steel support must be an equal height.

You have a collection of rods which can be welded together.  For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.  If you cannot support the billboard, return 0.



Example 1:

Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


Note:

0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.
"""


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        l = len(rods)
        memory = {}
        def dfs(i, left, right):
            if i == l:
                return left if left == right else 0
            if (i, left, right) in memory:
                return memory[(i, left, right)]
            # 加到左边
            first = dfs(i + 1, left + rods[i], right)
            # 加到右边
            second = dfs(i + 1, left, right + rods[i])
            # 都不加
            third = dfs(i + 1, left, right)
            memory[(i, left, right)] = max([first, second, third])
            return memory[(i, left, right)]

        return dfs(0, 0, 0)

    def tallestBillboard_1(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        620 ms
        """
        # dp[d] mean the maximum pair of sum we can get with pair difference d
        # dp表示存在相差为d的组对，dp[d]记录其中最大组对中较小的那个数值
        dp = {0: 0}
        for x in rods:
            its = list(dp.items())
            for d, y in its:
                # 大的那个数继续增加x，所以y不会改变
                dp[d + x] = max(dp.get(x + d, 0), y)  # 找出相差为d+x的最大对情况
                # 较小的数变动，并且注意到y+x可能大于较大的那个数，所以用y + min(d, x)记录
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]


print(Solution().tallestBillboard_1([1,2,3,6]))
print(Solution().tallestBillboard_1([1,2,3,4,5,6]))
print(Solution().tallestBillboard_1([1,2]))
print(Solution().tallestBillboard_1([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))


import collections


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        def dp(A):
            lookup = collections.defaultdict(int)
            lookup[0] = 0
            for x in A:
                for d, y in lookup.items():
                    lookup[d+x] = max(lookup[d+x], y)
                    lookup[abs(d-x)] = max(lookup[abs(d-x)], y + min(d, x))
            return lookup
        # 分成左右半边，然后各自找出相差为d的组，然后合起来+d就是最后结果，贪心了一下
        left, right = dp(rods[:len(rods)//2]), dp(rods[len(rods)//2:])
        return max(left[d] + right[d] + d for d in left if d in right)