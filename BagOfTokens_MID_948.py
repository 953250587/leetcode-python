"""
You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.



Example 1:

Input: tokens = [100], P = 50
Output: 0
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2


Note:

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000
"""


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        40 ms
        """
        if not tokens:
            return 0
        tokens = sorted(tokens)
        total = 0
        count = 0
        # 先计算如果只加不减最多可以持有代币数
        for i, token in enumerate(tokens):
            if total + token <= P:
                count += 1
                total += token
            else:
                break
        # 至少有count个
        max_val = count
        # 剩下可以用的token的起始位置
        start, end = i, len(tokens) - 1
        # 确保还有可以用的
        while start < end and count > 0:
            # 用一个代币去换最大的价值
            total -= tokens[end]
            end -= 1
            count -= 1
            # 用换来的价值再去购买其他代币
            while start <= end and total + tokens[start] <= P:
                total += tokens[start]
                start += 1
                count += 1
            max_val = max(max_val, count)

        return max_val

    def bagOfTokensScore_1(self, tokens, P):
        """
        48ms
        :param tokens:
        :param P:
        :return:
        """
        import collections
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1

        return ans


# print(Solution().bagOfTokensScore(tokens = [100], P = 50))
# print(Solution().bagOfTokensScore(tokens = [100,200], P = 150))
# print(Solution().bagOfTokensScore(tokens = [100,200,300,400], P = 200))
# print(Solution().bagOfTokensScore(tokens = [100,100,300], P = 500))
# print(Solution().bagOfTokensScore(tokens = [], P = 500))
print(Solution().bagOfTokensScore([71,55,82], 54))



