"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
import random
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        48ms
        """
        A=sum(nums)
        if A%2==1:
            return False
        a=A//2
        self.nums=sorted(nums,reverse=True)

        def dfs(a,count):
            # print(a,count)
            if count>=len(self.nums):
                return False
            b=self.nums[count]
            if a - b == 0:
                return True
            if a-b<0:
                return False
            if dfs(a-b,count+1):
                return True
            else:
                return dfs(a,count+1)

        return dfs(a,0)

    def canPartition_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        865ms
        """

        sum = 0
        for num in nums:
            sum += num

        if sum % 2 == 1:
            return False

        half_sum = sum / 2
        dp = [False] * (half_sum + 1)
        dp[0] = True

        for num in nums:
            new_dp = dp[:]
            for i in range(0, len(dp)):
                if dp[i] and i + num < len(dp):
                    new_dp[i + num] = True
                    if i + num == half_sum:
                        return True
            dp = new_dp[:]

        return False
print(Solution().canPartition([1, 2, 3, 5]))
print(Solution().canPartition([1, 5, 11, 5]))
nums=[random.randint(1,100) for i in range(200)]
print(Solution().canPartition(nums))
print(Solution().canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]))
