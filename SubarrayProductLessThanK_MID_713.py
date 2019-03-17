"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        398ms
        """
        s = 1
        count = 0
        sum_1 = 0
        start = 0
        l = len(nums)
        for i, num in enumerate(nums):
            s *= num
            count += 1
            if s < k:
                sum_1 += count
            else:
                while start <= i and s >= k:
                    s /= nums[start]
                    start += 1
                    count -= 1
                sum_1 += count
        return sum_1

    def numSubarrayProductLessThanK_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        399ms
        """
        if k <= 1: return 0
        result, left, prod = 0, 0, 1
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            result += right - left + 1
        return result
print(Solution().numSubarrayProductLessThanK(nums = [10, 5, 2, 6], k = 100))
print(Solution().numSubarrayProductLessThanK(nums = [1, 2, 3], k = 0))