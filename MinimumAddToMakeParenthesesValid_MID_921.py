"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.



Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4


Note:

S.length <= 1000
S only consists of '(' and ')' characters.
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        28 ms
        """
        stack = []
        for char in S:
            # 遇到'('都是直接添加
            if char == '(':
                stack.append(char)
            else:
                # 如果能够和之前的'('抵消就排除一个
                if stack and stack[-1] == '(':
                    stack.pop()
                # 否则就是非法的，加进去
                else:
                    stack.append(char)
        return len(stack)

    def minAddToMakeValid_1(self, S):
        """
        :type S: str
        :rtype: int
        """
        cnt = 0  # 不能抵消的右括号个数
        balance = 0  # 左括号个数
        for c in S:
            if c == '(':
                balance += 1
            elif balance == 0:
                cnt += 1
            else:
                balance -= 1

        return cnt + balance



print(Solution().minAddToMakeValid("())"))
print(Solution().minAddToMakeValid("((("))
print(Solution().minAddToMakeValid("()"))
print(Solution().minAddToMakeValid("()))(("))
