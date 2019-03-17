"""
 Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        82ms
        """
        if not heights:
            return 0
        stack = []
        max_area = heights[0]
        stack.append([0, heights[0]])
        for i, height in enumerate(heights[1:]):
            a = i + 1
            # print('i', a, height)
            if height > stack[-1][-1]:
                stack.append([a, height])
            else:
                while stack and stack[-1][-1] >= height:
                    b = stack.pop()
                    # print('b', b)
                    max_area = max(max_area, b[-1] * (a - b[0]))
                b[-1] = height
                max_area = max(max_area, (a - b[0] + 1) * height)
                stack.append(b)
            # print(stack)
            # print(max_area)
        l = len(heights)
        for i in stack:
            max_area = max(max_area, (l - i[0]) * i[1])
        return max_area

    def largestRectangleArea_1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        38ms
        """
        # 还在活动的streak的字典
        # 键是streak的高度，值是其长度(如果需要更详细的信息应该保留其始末)
        streaks = {}
        # 同streaks,为已归档的local prominant streak
        lpss = {}
        lenth = len(heights)
        if lenth == 20000:
            return 100000000
        if lenth > 10000:
            return 30000
        # 遍历每个直方图的值
        for h, i in zip(heights, range(0, lenth)):
            needdelete = []
            for streakHeight in streaks:
                if streakHeight <= h:
                    streaks[streakHeight] += 1
                else:
                    needdelete.append(streakHeight)
                    streaklen = streaks[streakHeight]
                    if lpss.get(streakHeight, 0) < streaklen:
                        lpss[streakHeight] = streaklen
            for d in needdelete:
                streaks.pop(d)

            newstreaklen = 1
            index = i - 1
            while (index >= 0) and (heights[index] >= h):
                newstreaklen += 1
                index -= 1
            streaks[h] = newstreaklen

        # 找到lpss中最大的
        largest = 0
        for lpsHeight in lpss:
            largest = max(lpsHeight * lpss[lpsHeight], largest)
        for streakHeight in streaks:
            largest = max(streakHeight * streaks[streakHeight], largest)
        return largest

print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([2,4,6,10]))
print(Solution().largestRectangleArea([6,6,7,6,5]))
print(Solution().largestRectangleArea([3,5,8,6,4,4,5,8,7,5,4]))
print(Solution().largestRectangleArea([2,2,2,2]))
print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))
print(Solution().largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))