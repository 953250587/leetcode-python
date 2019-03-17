"""
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".




Note:

S contains only lowercase letters.
1 <= S.length <= 2000
"""


class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        128 ms
        """
        temp = 10 ** 9 + 7
        l = len(S)
        if l <= 0:
            return 0
        import collections
        dicts = collections.defaultdict(int)
        used = set()
        dp = [0 for _ in range(l)]
        total = 0
        for i in range(len(S)):
            everytime = 0  # 记录每一次dp的结果
            # print('dp', dp)
            # 回溯之前一次相同字母出现的位置之间都能满足要求
            for before in range(dicts[S[i]], i):
                everytime += dp[before]
                everytime %= temp
            # 如果是第一次出现，则把自身也加进去
            if S[i] not in used:
                used.add(S[i])
                everytime += 1
                everytime %= temp
            dicts[S[i]] = i
            # 统计全部
            dp[i] = everytime
            total += everytime
            total %= temp
        print(dp)
        return total

    def distinctSubseqII_1(self, S):
        """
        :type S: str
        :rtype: int
        36ms
        """
        # 思路一致，不过他不是一个个统计，而是直接计算出结果！！！！！    
        dp = [1] * (1 + len(S))
        smap = {}
        smap[S[0]] = 0
        m = 10 ** 9 + 7
        dp[1] = 2
        for i in range(1, len(S)):
            ch = S[i]
            index = i + 1
            if ch not in smap:
                dp[index] = (dp[index - 1] * 2) % m
            else:
                dp[index] = ((dp[index - 1]) * 2 - dp[smap[ch]]) % m
            smap[ch] = i
        return dp[-1] - 1



print(Solution().distinctSubseqII('abc'))
print(Solution().distinctSubseqII('aba'))
print(Solution().distinctSubseqII('abaa'))
print(Solution().distinctSubseqII('ababa'))
