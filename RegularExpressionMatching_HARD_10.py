"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""
class Solution(object):
    def isMatch_1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        112ms
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
            elif start_p >= self.l_p:
                return False
            char_p = self.p[start_p]
            if start_p + 1 < self.l_p and self.p[start_p + 1] == '*':
                if dfs(start_s, start_p + 2, c + 1):
                    return True
                if start_s >= self.l_s or self.s[start_s] != char_p and char_p != '.':
                    self.dict[(start_s, start_p)] = False
                    return False
                if dfs(start_s + 1, start_p, c + 1):
                    return True
                if dfs(start_s + 1, start_p + 2, c + 1):
                    return True
                self.dict[(start_s, start_p)] = False
                return False
            else:
                if start_s >= self.l_s or self.s[start_s] != char_p and char_p != '.':
                    self.dict[(start_s, start_p)] = False
                    return False
                return dfs(start_s + 1, start_p + 1, c + 1)
        return dfs(0, 0, 0)

    def __init__(self):
        self.cache = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        46ms
        """
        # backtracking with cache
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

    def isMatch_2(self, s, p):
        """
        79ms
        :param s:
        :param p:
        :return:
        """
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    # * == 0个 ，* == 1个
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    # * == 2个
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]
print(Solution().isMatch('aa', 'a'))
print(Solution().isMatch('aa', 'aa'))
print(Solution().isMatch('aaa', 'aa'))
print(Solution().isMatch('aaa', 'a*'))
print(Solution().isMatch('aa', '.*'))
print(Solution().isMatch('ab', '.*'))
print(Solution().isMatch('ab', '.*c'))
print(Solution().isMatch('a', 'ab*'))
