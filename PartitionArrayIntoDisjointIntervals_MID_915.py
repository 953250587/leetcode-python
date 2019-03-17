"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.
"""


class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        288 ms nlgn
        """
        # 最小堆
        import heapq, collections
        # 记录左半边最大值
        left_max = A[0]
        # 用来存储右半边最小值
        h = []
        for a in A[1:]:
            heapq.heappush(h, a)
        # 记录每次跳出值
        temp = collections.defaultdict(int)
        l = len(A)
        for i in range(1, l):
            # print('left_max:', left_max, 'h[0]:', h[0])
            # 如果左半边最大值比右半边最小值小，结束
            if left_max <= h[0]:
                return i
            else:
                # 否则更新下左半边最大值
                left_max = max(A[i], left_max)
                # 记录下右半边排除了那个元素
                temp[A[i]] += 1
                # 判断h是否为空
                while h:
                    # 不为空判断该值是否已经被排除
                    if temp[h[0]] > 0:
                        # 如果被排除则弹出
                        t = heapq.heappop(h)
                        # 对应删除记录
                        temp[t] -= 1
                    # 否则当前最小值还存在
                    else:
                        break
        return l

    def partitionDisjoint_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        32ms
        """
        # 找到最小之前的一段序列，这段必定位于左侧
        l = A[:A.index(min(A))]
        if len(l) == 0:
            return 1
        # 找出这个序列的最大值
        a = max(l)
        ans = 0
        # 从后往前找到第一个比a来的小的位置，右侧的划分必定在这个位置右侧
        for i in range(len(A) - 1, -1, -1):
            if A[i] < a:
                ans = i + 1
                break
        while min(A[ans:]) < max(A[:ans]):
            ans += 1
        return ans

print(Solution().partitionDisjoint([5,0,3,8,6]))
print(Solution().partitionDisjoint([1,1,1,0,6,12]))
print(Solution().partitionDisjoint([1,1]))
