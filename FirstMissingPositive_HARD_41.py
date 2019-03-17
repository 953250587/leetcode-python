"""
 Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        35ms
        """
        l = len(nums)
        start = 0
        while start < l:
            temp = nums[start]
            if temp <= 0 or temp > l:
                start += 1
            else:
                if temp == start + 1:
                    start += 1
                else:
                    if nums[temp - 1] != temp:
                        nums[start], nums[temp - 1] = nums[temp - 1], nums[start]
                    else:
                        nums[start] = -1
                        start += 1
        print(nums)
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return l + 1

    def firstMissingPositive_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        39ms
        """
        n = len(nums)
        f = [False for i in range(0, n + 2)]
        for i in range(0, n):
            if ((nums[i] > 0) and (nums[i] <= n)): f[nums[i]] = True
        i = 1
        while (f[i]):
            i = i + 1
        return i
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([3,4,2,1]))
print(Solution().firstMissingPositive([3,3,4,1]))