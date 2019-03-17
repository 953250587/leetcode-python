"""
A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.



Example 1:

Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.



Note: 0 <= S.length <= 10000.
"""


class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        517 ms
        """
        S = S.upper()
        l = len(S)
        dicts = {char:[[], 0] for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        for i, char in enumerate(S):
            dicts[char][0].append(i)
        ans = 0
        print(dicts)
        for i, char in enumerate(S):
            pos = dicts[char][1]
            if pos - 1 >= 0:
                left = dicts[char][0][pos - 1]
            else:
                left = -1
            if pos + 1 < len(dicts[char][0]):
                right = dicts[char][0][pos + 1]
            else:
                right = l
            min_1 = min(i - left, right - i)
            max_1 = max(i - left, right - i)
            # 对称情况
            ans += (1 + min_1) * min_1  % (1e9 + 7)
            # 左右两边不均匀的情况
            ans += (max_1 - min_1) * min_1 % (1e9 + 7)
            # 对称情况里多出的部分
            ans -= min_1 % (1e9 + 7)
            dicts[char][1] += 1
            print(ans)
        return int(ans)

    def uniqueLetterString_1(self, S):
        """
        136ms
        :param S:
        :return:
        """
        import string
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10 ** 9 + 7)
print(Solution().uniqueLetterString("ABC"))
print(Solution().uniqueLetterString("ABA"))