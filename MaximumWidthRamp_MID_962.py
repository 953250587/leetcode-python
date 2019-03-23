"""
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
"""
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        636 ms
        18 MB
        """
        # O(nlgn)
        import bisect
        # 先倒序，方便后面是形递增数列
        A = A[::-1]
        # 记录当前开始值为0
        start = 0
        # 用于记录一个递增数列
        increase_list = [A[start]]
        # 用于记录递增数列的位置
        increase_index = [start]
        # 用于记录最大间隔
        max_value = 0
        # 由于倒序排列后，原问题转化为找到一个最大的A[i] <= A[j],其中i < j
        for i in range(len(A)):
            # 对于每一个大于当前值的A[i]值，都记录下来
            if A[i] > A[start]:
                increase_list.append(A[i])
                increase_index.append(i)
                start = i
            # 否则说明它可能小于之前记录的某个值，用二分查找找出对应位置然后向减
            else:
                pos = bisect.bisect_left(increase_list, A[i])
                # 记录最大位置
                max_value = max(max_value, i - increase_index[pos])
        return max_value

    def maxWidthRamp_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        600ms
        17.8m
        """
        # O(n) ~~~~
        s = []
        res = 0
        # 记录一个递减数列
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
        # 然后反序计算
        for j in range(len(A))[::-1]:
            # 如果当前的值小于记录的递减数列的值，则说明该位置已经到了极限，可以排除
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res


if __name__ == '__main__':
    print(Solution().maxWidthRamp([6,0,8,2,1,5]))
    print(Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
    print(Solution().maxWidthRamp([7,6,5,4,3,2,1]))
    print(Solution().maxWidthRamp([1, 1, 1, 1, 1, 1, 1]))




