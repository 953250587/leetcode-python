"""
 You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        超时，java可以过！！！！
        """
        self.s=S
        self.nums = nums
        self.result = {}

        if nums==[]:
            return 0
        def dfs(position, count):
            if (position, count) in self.result.keys():
                return self.result[(position, count)]
            if position == len(self.nums) - 1:
                a = 0
                if count + self.nums[position] == self.s:
                    a += 1
                if count - self.nums[position] == self.s:
                    a += 1
                return a
            if position < len(self.nums) - 1:
                a = dfs(position + 1, count + self.nums[position])
                b = dfs(position + 1, count - self.nums[position])
                self.result[(position, count)] = a + b
                return a + b

        return dfs(0, 0)

    def findTargetSumWays_1(self, nums, S):
        """
        412ms
        :param nums:
        :param S:
        :return:
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

    def findTargetSumWays_2(self, nums, S):

        if len(nums) == 0:
            return 0

        totalSum = sum(nums)

        if totalSum < S or (totalSum - S) % 2 == 1:
            return 0

        target = (totalSum - S) // 2
        dp = [0 for x in range(target + 1)]
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[target]
print(Solution().findTargetSumWays([1], 1))
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
print(Solution().findTargetSumWays([27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0], 10))