"""
 Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""
import numpy as np
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        982ms
        """
        max_1 = 1
        l =len(nums)
        if l <= 0:
            return 0
        dp = [[1, 1] for i in range(l)]
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    if (dp[j][0] + 1) > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                        max_1 = max(max_1, dp[i][0])
                    elif (dp[j][0] + 1) == dp[i][0]:
                        dp[i][1] += dp[j][1]
        print(np.array(dp), max_1)
        count = 0
        for i in dp:
            if i[0] == max_1:
                count += i[-1]
        return count

    def findNumberOfLIS_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect,collections
        if not nums:
            return 0

        pre = []  # maintain the minmal end of the IS of length j
        count = []  # maintain the possible k for a IS of length j and the count for that end
        for num in nums:
            index = bisect.bisect_left(pre, num)
            if index == len(pre):
                pre.append(num)
                count.append(collections.defaultdict(int))
            else:
                pre[index] = num
            if index == 0:
                count[index][num] += 1
            else:
                for k, v in count[index - 1].iteritems():
                    if k < num:
                        count[index][num] += v
        return sum(count[-1].values())
print(Solution().findNumberOfLIS([1,3,5,4,7,1]))
print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))
print(Solution().findNumberOfLIS([1,1,2,2,2,2,2]))
print(Solution().findNumberOfLIS([2,2,2,2,2]))