"""
 A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:

Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:

Input: "1*"
Output: 9 + 9 = 18

Note:

    The length of the input string will fit in range [1, 105].
    The input string will only contain the character '*' and digits '0' - '9'.

"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '0':
            return 1
        if s[0] == '0':
            return 0
        MOD = 10 ** 9 + 7
        l = len(s)
        for i in range(1, l):
            if s[i] == '0' and (s[i - 1] not in ['1', '2', '*']):
                return 0
        lists = s.split('0')
        dicts = {}
        def dfs(i, j, s):
            if i > j:
                return 1
            if (i, j) in dicts:
                return dicts[(i, j)]
            a, b = 0, 0
            if s[i] == '1':
                a = dfs(i + 1, j, s)
                if i + 1 <= j and s[i + 1] in '0123456789':
                    b = dfs(i + 2, j, s)
                else:
                    b = 9 * dfs(i + 2, j, s) % MOD
            elif s[i] == '2':
                a = dfs(i + 1, j, s)
                if i + 1 <= j and s[i + 1] in '0123456789':
                    b = dfs(i + 2, j, s)
                else:
                    b = 6 * dfs(i + 2, j, s) % MOD
            elif s[i] == '*':
                a = 9 * dfs(i + 1, j, s) % MOD
                if i + 1 <= j and s[i + 1] in '0123456789':
                    b = 2 * dfs(i + 2, j, s) % MOD
                elif i + 1 <= j and s[i + 1] == '*':
                    b = 15 * dfs(i + 2, j, s) % MOD
            else:
                a = dfs(i + 1, j, s)
            print((i , j), a, b)
            dicts[(i, j)] = (a + b) % MOD
            return a + b
        ans = 1
        for part in lists[:-1]:
            dicts = {}
            l = len(part)
            ans *= dfs(0, l - 2, part)
            ans %= MOD
            if part[-1] == '*':
                ans *= 2
        end = lists[-1]
        l = len(end)
        ans *= dfs(0, l - 1, end)
        ans %= MOD
        # print(dfs(0, 2, '12*'))
        return ans

    def numDecodings_1(self, s):
        """
        :type s: str
        :rtype: int
        1086ms
        """
        MOD = 10 ** 9 + 7
        e0, e1, e2 = 1, 0, 0 # e0表示末尾为单个的，e1表示末尾以1为结尾，e2表示末尾为2结尾的
        for c in s:
            if c == '*':
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0

    def numDecodings_2(self, s):
        """
        :type s: str
        :rtype: int
        633ms
        """
        import collections
        dmap = collections.defaultdict(int)
        cs = '0123456789*'
        for m in cs:
            if m == '*':
                dmap[m] = 9
                for n in cs:
                    c = m + n
                    if c == '**':
                        dmap[c] = 15
                    elif n in '0123456':
                        dmap[c] = 2
                    else:
                        dmap[c] = 1
            elif m == '1':
                dmap[m] = 1
                for n in cs:
                    c = m + n
                    dmap[c] = 9 if n == '*' else 1
            elif m == '2':
                dmap[m] = 1
                for i in range(20, 27):
                    dmap[str(i)] = 1
                dmap[m + '*'] = 6
            elif m != '0':
                dmap[m] = 1

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return dmap[s]

        dp1, dp2 = dmap[s[0]], dmap[s[0]] * dmap[s[1]] + dmap[s[:2]]
        base = 10 ** 9 + 7
        print(repr(base))
        for i in range(2, len(s)):
            ans = dp1 * dmap[s[i - 1:i + 1]] + dp2 * dmap[s[i]]
            dp1, dp2 = dp2, ans % base

        return dp2
print(Solution().numDecodings_1('12**'))
print(Solution().numDecodings_1('*'))
print(Solution().numDecodings_1('1*'))
