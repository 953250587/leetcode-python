"""
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        68ms
        """
        sum_1 = 0
        stack = []
        for i, h in enumerate(height):
            if not stack and h == 0:
                continue
            else:
                if not stack or stack[-1][-1] > h:
                    stack.append([i, h])
                else:
                    lists = []
                    while stack and stack[-1][-1] <= h:
                        lists.append(stack.pop())
                    if not stack:
                        max_heigh = lists[-1][-1]
                    else:
                        max_heigh = h
                    for list in lists[::-1]:
                        distance = i - list[0]
                        sum_1 += distance * (max_heigh - list[-1])
                        max_heigh = list[-1]
                    if stack:
                        stack.append([lists[-1][0], h])
                    else:
                        stack.append([i, h])
        return sum_1

    def trap_1(self, height):
        """
        :type height: List[int]
        :rtype: int
        59ms
        """
        if not height:
            return 0

        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        res = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += (right_max - height[right])
                right -= 1

        return res

    def trap_2(self, height):
        """
        :type height: List[int]
        :rtype: int
        49ms
        """
        res = 0
        l, r = 0, len(height) - 1
        maxl, maxr = 0, 0
        while l <= r:
            if maxl < maxr:
                if height[l] < maxl:
                    res += maxl - height[l]
                else:
                    maxl = height[l]
                l += 1
            else:
                if height[r] < maxr:
                    res += maxr - height[r]
                else:
                    maxr = height[r]
                r -= 1
        return res
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([6,5,4,3,5,4,7]))
print(Solution().trap([]))





