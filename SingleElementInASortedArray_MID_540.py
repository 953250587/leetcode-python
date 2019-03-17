"""
 Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        32ms
        """
        if len(nums) == 1:
            return nums[0]
        high = len(nums) - 1
        low = 0
        mid = (high + low) // 2

        while low <= high:
            if (mid - 1 >=0 and nums[mid] == nums[mid - 1]):
                if (mid - 1) % 2 == 1:
                    high = mid - 2
                else:
                    low = mid + 1
                mid = (low + high) // 2
            elif (mid + 1 < len(nums) and nums[mid] == nums[mid + 1]):
                if mid % 2 == 1:
                    high = mid - 1
                else:
                    low = mid + 2
                mid = (low + high) // 2
            else:
                return nums[mid]

    def singleNonDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        42ms
        """
        l, r = 0, len(nums) - 1
        while l < r - 2:
            middle = (l + r) / 2
            if middle % 2 == 0:
                if nums[middle] == nums[middle - 1]:
                    r = middle
                else:
                    l = middle
            else:
                if nums[middle] == nums[middle - 1]:
                    l = middle + 1
                else:
                    r = middle - 1

        if nums[(l + r) / 2] == nums[r]:
            return nums[l]
        else:
            return nums[r]

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
print(Solution().singleNonDuplicate([1,3,3,7,7,10,10,11,11]))
print(Solution().singleNonDuplicate([1,1,3,3,7,7,10,10,11,11,15]))
print(Solution().singleNonDuplicate([1]))