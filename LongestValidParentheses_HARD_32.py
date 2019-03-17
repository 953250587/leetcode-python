"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""
import numpy as np
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        time_limit_over
        """
        max_1 = 0
        l = len(s)
        dp = [[-1] * l for _ in range(l)]
        for i in range(l):
            if s[i] == ')':
                dp[i][i] = -1
                continue
            else:
                dp[i][i] = 1
            for j in range(i + 1, l):
                if s[j] == '(':
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1] - 1
                if dp[i][j] < 0:
                    break
                if dp[i][j] == 0:
                    max_1 = max(max_1, j - i + 1)
        print(np.array(dp))
        return max_1

    def longestValidParentheses_1(self, s):
        """
        79ms
        :param s:
        :return:
        """
        stack = []
        max_1 = 0
        for i, char in enumerate(s):
            if char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                    if stack:
                        mark = stack[-1][-1]
                        max_1 = max(max_1, i - mark)
                    else:
                        max_1 = max(max_1, i + 1)
                else:
                    stack.append([char, i])
            else:
                stack.append([char, i])
        return max_1

    def longestValidParentheses_2(self, s):
        """
        :type s: str
        :rtype: int
        e.g: "()(())" [0,2,0,0,2,|"0"]
        69ms
        """
        if not s: return 0
        n = len(s)
        dp = [0] * n
        max_len = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)

    def longestValidParentheses_3(self, s):
        """
        :type s: str
        :rtype: int
        65ms
        """
        if s is None or len(s) < 2:
            return 0
        ret, start, stack, n = 0, 0, [], len(s)
        for i in range(0, n):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ret = max(ret, i - start + 1)
                    else:
                        ret = max(ret, i - stack[-1])
        return ret

print(Solution().longestValidParentheses_1("()"))
print(Solution().longestValidParentheses_1(")()())"))
print(Solution().longestValidParentheses_1(")()()(()())"))
print(Solution().longestValidParentheses_1(")()()(()()()"))