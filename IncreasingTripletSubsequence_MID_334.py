"""
 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        42ms
        """
        if nums == []:
            return False
        temp_count_0=nums[-1]
        temp_count_1=min(nums)
        for i in nums[:-1][::-1]:
            if i<temp_count_0:
               temp_count_1=max(temp_count_1,i)
            if i>temp_count_0:
                temp_count_0=i
            if i<temp_count_1:
                return True
        return False

    def increasingTriplet_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        35ms
        """
        import sys
        if len(nums) < 3:
            return False
        first = second = sys.maxint
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
nums=[5,4,1,3,2]
print(Solution().increasingTriplet(nums))



