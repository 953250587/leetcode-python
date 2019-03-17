"""


    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        38ms
        """
        self.nums = nums
        def binary_sreach(start, end):
            mid = (start + end) // 2
            if start >= end:
                return self.nums[start]
            if self.nums[start] > self.nums[end]:
                if self.nums[start] > self.nums[mid]:
                    return binary_sreach(start + 1, mid)
                else:
                    return binary_sreach(mid + 1, end)
            elif self.nums[start] == self.nums[end]:
                if self.nums[start] > self.nums[mid]:
                    return binary_sreach(start + 1, mid)
                elif self.nums[mid] > self.nums[end]:
                    return binary_sreach(mid + 1, end)
                else:
                    a = binary_sreach(start + 1, mid)
                    b = binary_sreach(mid + 1, end)
                return min(a, b)
            else:
                return self.nums[start]
        return binary_sreach(0, len(nums) - 1)

    def findMin_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        39ms
        """
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) / 2
            if nums[j] < nums[mid]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                if nums[i] == nums[mid]:
                    i += 1
                    j -= 1
                else:
                    j = mid
        return nums[j]

    def findMin_2(self, nums):
        """
        39ms
        :param nums:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]
print(Solution().findMin([2,2,2,2,2]))
print(Solution().findMin([2,2,1,2,2]))
print(Solution().findMin([2,3,3,4,1,1]))

