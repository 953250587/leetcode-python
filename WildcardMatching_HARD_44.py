"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
* 可以理解为前一题的.*的含义
"""
import numpy as np
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        2055ms
        """
        import collections
        self.s = s
        self.p = p
        self.l_p = len(p)
        self.l_s = len(s)
        self.dict = collections.defaultdict(bool)

        def dfs(start_s, start_p, c):
            # print(start_s, start_p, c)
            # print(self.dict)
            if (start_s, start_p) in self.dict:
                return self.dict[(start_s, start_p)]
            if start_s >= self.l_s and start_p >= self.l_p:
                return True
            elif start_p >= self.l_p or start_s > self.l_s:
                return False
            char_p = self.p[start_p]
            if char_p == '*':
                if dfs(start_s, start_p + 1, c + 1):
                    return True
                if dfs(start_s + 1, start_p, c + 1):
                    return True
                if dfs(start_s + 1, start_p + 1, c + 1):
                    return True
                self.dict[(start_s, start_p)] = False
                return False
            else:
                if start_s >= self.l_s or self.s[start_s] != char_p and char_p != '?':
                    self.dict[(start_s, start_p)] = False
                    return False
                return dfs(start_s + 1, start_p + 1, c + 1)

        return dfs(0, 0, 0)

    def isMatch_1(self, s, p):
        """
        1416ms
        :param s:
        :param p:
        :return:
        """
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(1, len(p) + 1):
            table[i][0] = table[i - 1][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '?')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    # * == 0个 ，* == 1个
                    table[i][j] = table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    # * == 2个
                    table[i][j] |= table[i][j - 1]
        # print(np.array(table))
        return table[-1][-1]

    def isMatch_2(self, s, p):
        """
        1416ms
        :param s:
        :param p:
        :return:
        232ms
        """
        start = 0
        l = min(len(s), len(p))
        while start < l and p[start] != '*':
            if s[start] != p[start] and p[start] != '?':
                return False
            else:
                start += 1
        p = p[start:]
        s = s[start:]
        end = -1
        l = min(len(s), len(p))
        while end >= -l and p[end] != '*':
            if s[end] != p[end] and p[end] != '?':
                return False
            else:
                end -= 1
        p = p[:len(p) + end + 1]
        s = s[:len(s) + end + 1]
        # print(p, s)
        if len(p) <= 0 and len(s) > 0:
            return False
        else:
            p_list = p.split('*')
            # print(p_list)
            start = 0
            while start < len(p_list) and p_list[start] == '':
                start += 1
            if start >= len(p_list):
                return True
            s_list = p_list[start]
            # print(s_list)
            i = 0
            while i < len(s):
                char = s[i]
                if char == s_list[0] or s_list[0] == '?':
                    flag = True
                    for k in range(len(s_list)):
                        if i + k >= len(s) or (s[i + k] != s_list[k] and s_list[k] != '?'):
                            flag = False
                            break
                    if flag:
                        i += len(s_list)
                        start += 1
                        while start < len(p_list) and p_list[start] == '':
                            start += 1
                        if start < len(p_list):
                            s_list = p_list[start]
                        else:
                            return True
                    else:
                        i += 1
                else:
                    i += 1
            return False

    def isMatch_3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        89ms
        """
        curr_s = 0
        curr_p = 0

        s_star = None
        p_star = None
        while curr_s < len(s):
            if curr_p < len(p):
                if p[curr_p] == s[curr_s] or p[curr_p] == '?':
                    curr_s += 1
                    curr_p += 1
                elif p[curr_p] == '*':
                    s_star = curr_s
                    p_star = curr_p
                    curr_p += 1
                else:
                    if s_star is None:
                        return False

                    s_star += 1
                    curr_s = s_star
                    curr_p = p_star + 1
            else:
                if s_star is None:
                    return False

                s_star += 1
                curr_s = s_star
                curr_p = p_star + 1

        while curr_p < len(p):
            if p[curr_p] != '*':
                return False

            curr_p += 1

        return True

    def isMatch_4(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        94ms
        """
        m, n = len(s), len(p)
        s_cur = p_cur = 0
        s_match = p_match = -1
        while s_cur < m:
            if p_cur < n and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < n and p[p_cur] == '*':
                p_cur += 1
                s_match, p_match = s_cur, p_cur
            elif p_match != -1:
                s_cur, p_cur = s_match + 1, p_match
                s_match = s_cur
            else:
                return False
        return False if p[p_cur:].rstrip('*') else True




print(Solution().isMatch_2('aa', 'a'))
print(Solution().isMatch_2('aa', 'aa'))
print(Solution().isMatch_2('aaa', 'aa'))

print(Solution().isMatch_2('aaa', 'a*'))
print(Solution().isMatch_2('aa', '?*'))
print(Solution().isMatch_2('ab', '?*'))

print(Solution().isMatch_2('ab', '?*c'))
print(Solution().isMatch_2('a', 'ab*'))
print(Solution().isMatch_2("aab", "c*a*b"))
print(Solution().isMatch_2("ab","*a"))

print(Solution().isMatch_2("aaaa","***a"))
print(Solution().isMatch_2("aab", "*a?b**"))
print(Solution().isMatch_2("aab", "*"))
print(Solution().isMatch_2("aab", "*aab*"))
print(Solution().isMatch_2('a', ''))
print(Solution().isMatch_2("mississippi","m*si*"))
print(Solution().isMatch_2("abc","*abc?*"))
print(Solution().isMatch_2("c","*?*"))
print(Solution().isMatch_2("mississippi","m*issi*iss*"))
print('*'.split('*'))

