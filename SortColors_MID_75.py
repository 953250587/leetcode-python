"""
 Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        32ms
        """
        mark_0 = 0
        start = 0
        end =len(nums) - 1
        while start <= end:
            if nums[start] == 0:
                nums[start], nums[mark_0] = nums[mark_0], nums[start]
                mark_0 += 1
                start += 1
            elif nums[start] == 2:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return nums

print(Solution().sortColors([1, 0, 1, 0, 2, 1, 0, 1, 2, 2, 1, 0]))
print(Solution().sortColors([2, 1, 2]))
print(Solution().sortColors([0]))