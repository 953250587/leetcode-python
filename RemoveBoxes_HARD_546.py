"""
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]

Output:

23

Explanation:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)

Note: The number of boxes n would not exceed 100.

"""
class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        if len(boxes) <= 0:
            return 0
        cur = boxes[0]
        count = 1
        box_list = []
        for box in boxes[1:]:
            if box == cur:
                count += 1
            else:
                box_list.append((cur, count))
                cur = box
                count = 1
        box_list.append([cur, count])
        print(box_list)
        dicts = {}

        def dfs(box_list, count):
            l = len(box_list)
            if l == 0:
                return count
            strs = ''
            for box in box_list:
                strs += str(box[0]) + '-' + str(box[1])
                strs += ' '
            if strs in dicts:
                return dicts[strs]
            max_1 = 0
            for i in range(l):
                if i == 0:
                    num = dfs(box_list[1:], count)
                elif i == l - 1:
                    num = dfs(box_list[0: i], count)
                else:
                    stack = box_list[0: i]
                    if box_list[i + 1][0] == stack[-1][0]:
                        a = stack.pop()
                        stack.append((a[0], a[1] + box_list[i + 1][1]))
                    else:
                        stack.append(box_list[i + 1])
                    stack += box_list[i + 2:]
                    # print(stack)
                    num = dfs(stack, count)
                max_1 = max(max_1, num + box_list[i][1] ** 2)
                # print(strs, max_1)
            dicts[strs] = max_1
            return max_1
        return  dfs(box_list, 0)

    def removeBoxes_1(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        645MS
        """
        l = len(boxes)
        dp = [[[0] * l for _ in range(l)] for _ in range(l)]

        def dfs(left, right, end_num):
            if left > right:
                return 0
            if dp[left][right][end_num] == 0:
                start = right - 1
                while start >= left:
                    if boxes[start] == boxes[right]:
                        end_num += 1
                    else:
                        break
                    start -= 1
                right = start + 1
                dp[left][right][end_num] = dfs(left, start, 0) + (end_num + 1) ** 2
                for j in range(left, start + 1):
                    if boxes[j] == boxes[right]:
                        dp[left][right][end_num] = max(dp[left][right][end_num],
                                                       dfs(left, j, end_num + 1) + dfs(j + 1, start, 0))
            return dp[left][right][end_num]
        return dfs(0, l - 1, 0)

    def removeBoxes_2(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        140MS
        """
        cache = {}
        n = len(boxes)

        return self.removeBoxesCache(boxes, 0, 0, n - 1, cache)

    def removeBoxesCache(self, boxes, count, left, right, cache):
        if left == right:
            return (count + 1) * (count + 1)

        i = left
        while i + 1 <= right and boxes[i + 1] == boxes[left]:
            i += 1

        if i > left:
            return self.removeBoxesCache(boxes, count + i - left, i, right, cache)

        key = (count, left, right)

        if key not in cache:
            ret = (count + 1) ** 2 + self.removeBoxesCache(boxes, 0, left + 1, right, cache)

            i = left + 1
            while i <= right:
                if boxes[i] == boxes[left]:
                    point = self.removeBoxesCache(boxes, 0, left + 1, i - 1, cache) + self.removeBoxesCache(boxes,
                                                                                                            count + 1,
                                                                                                            i, right,
                                                                                                            cache)
                    ret = max(ret, point)
                    while i <= right and boxes[i] == boxes[left]:
                        i += 1
                else:
                    i += 1
            cache[key] = ret

        return cache[key]



print(Solution().removeBoxes_1([1, 3, 2, 2, 2, 3, 4, 3, 1]))
print(Solution().removeBoxes_1([10, 8, 5, 1, 9, 6, 6, 9, 6, 10]))
