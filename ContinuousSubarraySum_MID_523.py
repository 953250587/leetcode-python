"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        1345ms
        """
        l = len(nums)
        for i in range(1, l + 1):
            dp = [0] * (l + 1)
            dp[i] = nums[i - 1]
            for j in range(i + 1, l + 1):
                dp[j] = dp[j - 1] + nums[j - 1]
                if (k != 0 and dp[j] % k == 0) or (k == 0 and dp[j] == 0):
                    return True
        return False

    def checkSubarraySum_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        55ms
        """
        pos = {0: -1}
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            if k != 0: runningSum %= k
            prev = pos.get(runningSum, None)
            if prev != None:
                if i - prev > 1: return True
            else:
                pos[runningSum] = i

        return False

    def checkSubarraySum_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        1345ms
        """
        l = len(nums)
        self.sets = set()
        for i in range(1, l + 1):
            dp = [0] * (l + 1)
            dp[i] = nums[i - 1]
            for j in range(i + 1, l + 1):
                dp[j] = dp[j - 1] + nums[j - 1]
                if (j, dp[j]) in self.sets:
                    break
                if (k != 0 and dp[j] % k == 0) or (k == 0 and dp[j] == 0):
                    return True
                self.sets.add((j, dp[j]))
        return False
nums = [1, 2, 3]
k = 6
print(Solution().checkSubarraySum_1(nums, k))
