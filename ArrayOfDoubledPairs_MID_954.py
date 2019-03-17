"""
Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.



Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false


Note:

0 <= A.length <= 30000
A.length is even
"""


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        400 ms
        """
        import collections
        # 安绝对值大小排序
        A = sorted(A, key=lambda a:abs(a))
        # 纪录每个数字出现的次数
        count_A = collections.Counter(A)
        for a in A:
            # 先判断当前数字是否已经被使用完
            if count_A[a] >= 1:
                count_A[a] -= 1
                # 未使用完判断和它匹配的数字是否还存在
                flag = count_A.get(a * 2, 0)
                if flag >= 1:
                    count_A[a * 2] -= 1
                # 不存在说明无解
                else:
                    return False
        return True

    def canReorderDoubled_1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        120ms
        """
        from collections import defaultdict
        cts = defaultdict(int)
        for v in A:
            cts[v] += 1
        keys = cts.keys()
        for k in keys:
            if k % 2 == 1:
                if cts[2 * k] < cts[k]:
                    return False
                cts[2 * k] -= cts[k]
                del cts[k]
                if cts[2 * k] == 0:
                    del cts[2 * k]
        negs = sorted([-k for k in keys if cts[k] > 0 and k < 0])
        pos = sorted([k for k in keys if cts[k] > 0 and k > 0])
        zeros = cts[0]
        if zeros % 2 == 1:
            return False
        keys = [-k for k in negs] + pos
        for k in keys:
            if cts[k] == 0:
                continue
            if cts[2 * k] < cts[k]:
                return False
            cts[2 * k] -= cts[k]
            del cts[k]
        return True


print(Solution().canReorderDoubled([3,1,3,6]))
print(Solution().canReorderDoubled([2,1,2,6]))
print(Solution().canReorderDoubled([4,-2,2,-4]))
print(Solution().canReorderDoubled([1,2,4,16,8,4]))
