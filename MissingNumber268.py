"""
 Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        45ms
        """
        return sum([i for i in range(len(nums)+1)])-sum(nums)

    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        56ms
        """
        length = len(nums)
        missNum = 0
        for i in range(length):
            missNum = missNum ^ nums[i] ^ i
        return missNum ^ length

print(Solution().missingNumber([0,1,6,4,5,2]))
