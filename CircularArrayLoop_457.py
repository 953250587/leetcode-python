"""
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        20 ms
        """
        for i, start in enumerate(range(len(nums))):
            # start = 0
            if isinstance(nums[start], int):
                if nums[start] > 0:
                    flag = 1
                else:
                    flag = -1
            else:
                break
            F = True

            while isinstance(nums[start], int):
                n = nums[start]
                # nums[start] = 0
                if abs(n) == len(nums) or n * flag < 0:
                    F = False
                    break
                # n = nums[start]
                nums[start] = str(i)
                start += n
                start %= len(nums)
                # print(start)
            if F and nums[start] == str(i):
                return True
        return False
print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))
print(Solution().circularArrayLoop([-1, 2]))
print(Solution().circularArrayLoop([-1,-2,-3,-4,-5]))
print(Solution().circularArrayLoop([3, 1, 2]))
print(Solution().circularArrayLoop([]))
print(Solution().circularArrayLoop([-2,1,-1,-2,-2]))