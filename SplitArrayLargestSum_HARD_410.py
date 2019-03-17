"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""

import numpy as np
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = nums[i]
            for j in range(i + 1, l):
                dp[i][j] = dp[i][j - 1] + nums[j]
        print(np.array(dp))
        self.dicts = {}
        def dfs(start, end, m):
            # print(start, end, m)
            if (start, end, m) in self.dicts:
                return self.dicts[(start, end, m)]
            if m == 1:
                return dp[start][end]
            elif start == end:
                return float('inf')
            max_1 = float('inf')
            for k in range(1, m):
                for p in range(start, end):
                    a = dfs(start, p, k)
                    b = dfs(p + 1, end, m - k)
                    max_1 = min(max_1, max(a, b))
            self.dicts[(start, end, m)] = max_1
            return max_1
        a = dfs(0, l - 1, m)
        # print(self.dicts)
        return a


    def splitArray_1(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        7185 ms
        """
        l = len(nums)
        m = min(m, l)
        dp = [[float('inf')] * l for _ in range(m)]
        dp[0][0] = nums[0]
        for i in range(1, l):
            dp[0][i] = dp[0][i - 1] + nums[i]
        for i in range(1, m):
            for j in range(i, l):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], dp[0][j] - dp[0][k]))
        print(np.array(dp))
        return dp[-1][-1]

    def splitArray_1(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        38ms
        """
        if not nums:
            return 0
        if m <= 1:
            return sum(nums)

        def valid(mid):
            count = 0
            total = 0
            for n in nums:
                total += n
                if total > mid:
                    count += 1
                    if count >= m:
                        return False
                    total = n
            return True

        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r - l) / 2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l


import random
print(Solution().splitArray_1([7,2,5,10,8], 2))
a = np.random.randint(0,100,20)
print(a)
# print(Solution().splitArray(a, 50))
print(Solution().splitArray_1(a, 50))