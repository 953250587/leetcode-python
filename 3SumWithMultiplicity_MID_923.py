"""
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        84 ms
        """
        s = 0
        # 统计每个数字出现次数
        mask = [0 for _ in range(101)]
        for a in A:
            mask[a] += 1
        # 记录每一次需要的数字个数
        need = [0 for _ in range(101)]
        for i in range(101):
            for j in range(i, 101):
                temp = target - i - j
                # 确保有序，且在范围内
                if j <= temp < 101:
                    need[i] += 1
                    need[j] += 1
                    need[temp] += 1
                    # 确保该种情况可行
                    if mask[i] >= need[i] and mask[j] >= need[j] and mask[temp] >= need[temp]:
                        # 3个数字相同的情况
                        if i == j == temp:
                            s += mask[i] * (mask[i] - 1) * (mask[i] - 2) // 6 % (10 ** 9 + 7)
                        # 第一二个数字相同
                        elif i == j:
                            s += mask[i] * (mask[i] - 1) // 2 * mask[temp] % (10 ** 9 + 7)
                        # 第二三个数字相同
                        elif j == temp:
                            s += mask[j] * (mask[j] - 1) // 2 * mask[i] % (10 ** 9 + 7)
                        # 全部不相同
                        else:
                            s += mask[i] * mask[j] * mask[temp] % (10 ** 9 + 7)
                        # print(need[:6], mask[:6], s)
                    # 复原情况
                    need[i] = 0
                    need[j] = 0
                    need[temp] = 0

        return s

    def threeSumMulti_1(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        32 ms
        """
        from collections import defaultdict
        count = 0

        d = defaultdict(int)
        for e in A:
            d[e] += 1

        l = sorted(d.keys())

        for i in range(len(l)):
            s = i
            e = len(l) - 1
            # 通过这种方式减小搜索范围
            while s <= e:
                tmp = l[i] + l[s] + l[e] - target
                if tmp == 0:
                    if i != s and s != e:
                        count += d[l[i]] * d[l[s]] * d[l[e]]
                    elif i == s and s != e:
                        count += (d[l[i]] * (d[l[i]] - 1) / 2) * d[l[e]]
                    elif i != s and s == e:
                        count += (d[l[s]] * (d[l[s]] - 1) / 2) * d[l[i]]
                    else:
                        count += (d[l[s]]) * (d[l[s]] - 1) * (d[l[s]] - 2) / 6
                    s += 1
                    e -= 1
                elif tmp > 0:
                    e -= 1
                else:
                    s += 1

        return (count % ((10 ** 9) + 7))

print(Solution().threeSumMulti(A = [1,1,2,2,3,3,4,4,5,5], target = 8))
print(Solution().threeSumMulti(A = [1,1,2,2,2,2], target = 5))



