# -*- coding: UTF-8 -*-
"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        1304 ms
        18 MB
        O(nlgn)
        """
        # 最傻逼的方法,计算距离排序
        points_with_distance = [(point, point[0] ** 2 + point[1] ** 2) for point in points]
        points_with_distance = sorted(points_with_distance, key=lambda a: a[1])
        return [point[0] for point in points_with_distance][:K]

    def kClosest_1(self, points, K):
        """
        1308 ms
        17.7 MB
        O(nlgk)
        :param points:
        :param K:
        :return:
        """
        # 聪明点的方法,用堆来记录最小的K个就好
        import heapq
        h = []
        for point in points:
            heapq.heappush(h, (-point[0] ** 2 - point[1] ** 2, point))
            if len(h) == K:
                break
        for point in points[K:]:
            temp = point[0] ** 2 + point[1] ** 2
            if temp <= -h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (-temp, point))
        return [point[1] for point in h]

    def kClosest_2(self, points, K):
        """

        :param points:
        :param K:
        :return:
         412 ms
         17.3 MB
        """
        # 牛逼方案,分治法,快排方案!!!我tm又忘了..
        # 特例可以先排除
        if K == len(points):
            return points
        # 先计算距离
        points_with_distance = [(point, point[0] ** 2 + point[1] ** 2) for point in points]
        # 用来记录结果
        ans = []
        # 如果剩余部分比K长,说明还没找到全部值
        while len(points_with_distance) > K:
            left = 0
            right = len(points_with_distance) - 1
            # 用于记录当前是从左往右还是从右往左
            i = 0
            # 两个指针还没碰头,我们希望左边小于某个定值,右边大于某个定值
            while left < right:
                # 如果左边大于右边,交换,并且如果之前是从左往右移动,现在改为从右往左,反之亦然
                if points_with_distance[left][1] > points_with_distance[right][1]:
                    points_with_distance[left], points_with_distance[right] = points_with_distance[right], points_with_distance[left]
                    i += 1
                if i % 2 == 0:
                    left += 1
                else:
                    right -= 1
            assert right == left
            # 如果交汇的位置刚好为K,则从0-K(不包括K)就是我们要的部分,返回即可
            if left == K:
                return ans + [point[0] for point in points_with_distance[:left]]
            # 如果不到K个,说明现在这些部分肯定是包含在K个内,去掉0-left(包括left至少有1个元素)
            # K对应减少left+1个
            elif left < K:
                ans += [point[0] for point in points_with_distance[:left + 1]]
                points_with_distance = points_with_distance[left + 1:]
                K -= left + 1
            # 否则超过K个则我们从0-left(不包括left)继续寻找
            else:
                points_with_distance = points_with_distance[:left]


if __name__ == '__main__':
    # print(Solution().kClosest_2(points = [[1,3],[-2,2]], K = 1))
    # print(Solution().kClosest_2(points = [[3,3],[5,-1],[-2,4]], K = 2))
    print(Solution().kClosest_2([[0,1], [1,0]], 2))

    import random
    t = random.randint(1, 100)
    points = []
    for i in range(t):
        f = random.randint(0, 100)
        h = random.randint(0, 100)
        points.append([f, h])

    K = random.randint(1, t)
    # print([(point, point[0] ** 2 + point[1] ** 2) for point in points], K)
    # points = [[2, 89], [18, 69], [49, 36], [4, 31]]
    # K = 3
    t = sorted(Solution().kClosest_2(points, K), key=lambda a: a[0] ** 2 + a[1] **2)
    p = sorted(Solution().kClosest_1(points, K), key=lambda a: a[0] ** 2 + a[1] ** 2)
    print(t == p)