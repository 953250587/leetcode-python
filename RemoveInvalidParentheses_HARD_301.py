"""
 Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""

import numpy as np
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        755ms
        """
        def isVail(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            if count == 0:
                return True
        self.result = set()
        def bfs(s, l):
            while not self.result and s:
                sets = s
                s = set()
                for i in range(l):
                    for s_partion in sets:
                        if s_partion[i] == '(' or s_partion[i] == ')':
                            c = s_partion[0:i] + s_partion[i + 1:]
                            if isVail(c):
                                self.result.add(c)
                            else:
                                s.add(c)
                l -= 1
        if isVail(s):
            return [s]
        sets = set()
        sets.add(s)
        l = len(s)
        bfs(sets, l)
        return list(self.result) if self.result else [s]

    def removeInvalidParentheses_1(self, s):
        """
        :type s: str
        :rtype: List[str]
        39ms
        """
        valid = []
        self.remove(s, valid, 0, 0, '(', ')')
        return valid

    def remove(self, s, valid, last_i, last_j, left, right):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == left:
                stack += 1
            elif s[i] == right:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == right and (j == last_j or s[j - 1] != right):
                    self.remove(s[:j] + s[j + 1:], valid, i, j, left, right)
            return
        r = s[::-1]
        if left == '(':
            self.remove(r, valid, 0, 0, ')', '(')
        else:
            valid.append(r)


print(Solution().removeInvalidParentheses("(a)()))()"))
print(Solution().removeInvalidParentheses("(a)())()"))
print(Solution().removeInvalidParentheses("()())()"))
print(Solution().removeInvalidParentheses(")("))
print(Solution().removeInvalidParentheses(')))))))))))))))'))
print(Solution().removeInvalidParentheses('n'))
print(Solution().removeInvalidParentheses('nfasgasgag)('))
print(Solution().removeInvalidParentheses('()'))