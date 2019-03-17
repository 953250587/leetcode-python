"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
"""
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        491MS
        """
        import bisect
        k_list = []
        if k % 2 == 1:
            mid_left = k // 2
            mid_right = k // 2
        else:
            mid_left = k // 2 - 1
            mid_right = k // 2
        for num in nums[:k - 1]:
            bisect.insort(k_list, num)
        result = []
        for i,num in enumerate(nums[k - 1:]):
            bisect.insort(k_list, num)
            result.append((k_list[mid_left] + k_list[mid_right]) / 2)
            k_list.remove(nums[i])
        return result
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

from bisect import *


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        126MS
        """
        win = sorted(nums[:k])
        isodd = k % 2
        med = []

        for i, n in enumerate(nums[k:], k):
            idx = k // 2
            if isodd:
                val = win[idx] / 1.
            else:
                val = (win[idx] + win[idx - 1]) / 2.
            med.append(val)
            print('before', win)
            pos = bisect_left(win, nums[i - k])
            print('pos', pos)
            win.pop(pos) # 指定位置弹出
            print('after', win)
            insort(win, nums[i])
        idx = k // 2
        if isodd:
            val = win[idx] / 1.
        else:
            val = (win[idx] + win[idx - 1]) / 2.
        med.append(val)
        return med

print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))