"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        96 ms
        """
        start, end = 0, len(S) - 1
        # 先将开头为0和结尾为1的先排除
        while start <= end and S[start] == '0':
            start += 1
        while start <= end and S[end] == '1':
            end -= 1
        # temp= []
        count = 0
        s = S[start:end + 1].count('1')
        # 全部为0，或者全部为1的情况
        min_val = min(s, end + 1 - start - s)
        # 分段，一部分为0一部分为1
        for i in range(start, end + 1):
            if S[i] == '1':
                count += 1
            # count是左边为1的部分，end - i - (s - count)是右边为0的部分
            min_val = min(min_val, count + end - i - (s - count))
        #     temp.append([count, end - i - (s - count)])
        # print(temp)
        return min_val

    def minFlipsMonoIncr_1(self, S):
        """
        :type S: str
        :rtype: int
        64ms
        """
        if not S: return 0
        # onesCnt记录1的个数，flipCnt记录翻转个数(0->1)
        flipCnt = onesCnt = 0
        for s in S:
            if s == '0':
                if onesCnt == 0:
                    continue
                else:
                    flipCnt += 1
            else:
                onesCnt += 1
            # 需要翻转的个数比onesCnt的个数多的时候，就把前面1全部翻转成0
            if flipCnt > onesCnt:
                flipCnt = onesCnt
        return flipCnt


# print(Solution().minFlipsMonoIncr('100101100'))
print(Solution().minFlipsMonoIncr("00110"))
print(Solution().minFlipsMonoIncr("010110"))
print(Solution().minFlipsMonoIncr("00011000"))


