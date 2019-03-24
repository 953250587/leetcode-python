"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9

"""


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        44 ms
        11.9 MB
        """
        # 如果N为1,则0-9都是可以的
        if N == 1:
            return [i for i in range(10)]
        ans_list = set()

        # 否则一位一位寻找
        def dpfunc(cur_N, cur_list, cur_value):
            if cur_N >= N:
                ans_list.add(int(''.join(cur_list)))
                return
            # 会不会超过9
            temp = cur_value + K
            if temp <= 9:
                cur_list.append(str(temp))
                dpfunc(cur_N + 1, cur_list, temp)
                cur_list.pop()
            # 会不会大于0
            temp = cur_value - K
            if temp >= 0:
                cur_list.append(str(temp))
                dpfunc(cur_N + 1, cur_list, temp)
                cur_list.pop()
            return

        # 第一位不能为0,所以从1开始
        for i in range(1, 10):
            dpfunc(1, [str(i)], i)
        return sorted(ans_list)

    def numsSameConsecDiff_1(self, N, K):
        """
        48ms
        12.1 MB
        :param N:
        :param K:
        :return:
        """
        cur = range(10)
        for i in range(N - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if x and 0 <= y < 10}
        return list(cur)


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(N=3, K=7))
    print(Solution().numsSameConsecDiff(N=2, K=1))
    print(Solution().numsSameConsecDiff(N=9, K=1))
