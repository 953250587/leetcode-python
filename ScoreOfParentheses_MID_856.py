"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        33 ms
        """
        i = 0
        stack = []
        while i < len(S):
            if S[i] == '(':
                if i + 1 < len(S) and S[i + 1] == ')':
                    stack.append(1)
                    i += 1
                else:
                    stack.append('(')
            else:
                t = 0
                while stack[-1] != '(':
                    t += stack.pop()
                stack.pop()
                stack.append(2 * t)
            i += 1
        return sum(stack)

    def scoreOfParentheses_1(self, S):
        """
        34ms
        :param S:
        :return:
        """
        res = layers = 0
        for a, b in zip(S, S[1:]):
            layers += 1 if a == '(' else -1
            if a + b == '()': res += 2 ** (layers - 1)
        return res

print(Solution().scoreOfParentheses("()"))
print(Solution().scoreOfParentheses("(())"))
print(Solution().scoreOfParentheses("()()"))
print(Solution().scoreOfParentheses("(()(()))"))


