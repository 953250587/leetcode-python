"""
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

    The string size will be in the range [1, 100].

"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        32ms
        """
        count = 0
        count_star = 0
        s = list(s)
        star = []
        for i, char in enumerate(s):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            else:
                count_star += 1
                star.append(i)
            if count < 0:
                count_star -= 1
                count += 1
                if count_star < 0:
                    return False
                else:
                    p = star.pop()
                    s[p] = '('
        print('1', s)
        if count == 0:
            return True
        count = 0
        count_star = 0
        for char in s[::-1]:
            if char == ')':
                count += 1
            elif char == '(':
                count -= 1
            else:
                count_star += 1
            if count < 0:
                count_star -= 1
                count += 1
                if count_star < 0:
                    return False
        print('2', s)
        if count == 0:
            return True

    def checkValidString_1(self, s):
        """
        :type s: str
        :rtype: bool
        29ms
        """
        stack = []
        num_star = 0
        # check from left
        for sig in s:
            if sig == "(":
                stack.append(sig)
            elif sig == ")":
                if len(stack) == 0 and num_star <= 0:
                    return False
                elif len(stack) == 0 and num_star > 0:
                    # take * as (
                    num_star -= 1
                else:
                    stack.pop()
            elif sig == "*":
                num_star += 1
        # check from right
        stack2 = []
        num_star2 = 0
        for i in range(len(s) - 1, -1, -1):
            sig = s[i]
            if sig == ")":
                stack2.append(sig)
            elif sig == "(":
                if len(stack2) == 0 and num_star2 <= 0:
                    return False
                elif len(stack2) == 0 and num_star2 > 0:
                    num_star2 -= 1
                else:
                    stack2.pop()
            elif sig == "*":
                num_star2 += 1

        if len(stack) > num_star or len(stack2) > num_star2:
            return False
        return True

    def checkValidString_2(self, s):
        """
        32ms
        :param s:
        :return:
        """
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0



print(Solution().checkValidString('()'))
print(Solution().checkValidString('(*)'))
print(Solution().checkValidString('(*)*))*)*'))
print(Solution().checkValidString("(*()"))
print(Solution().checkValidString('(**(()'))