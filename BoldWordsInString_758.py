"""
 Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

    words has length in range [0, 50].
    words[i] has length in range [1, 10].
    S has length in range [0, 500].
    All characters in words[i] and S are lowercase letters.

"""
import numpy as np
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        words = set(words)
        l = len(S)
        dp = [[False] * l for _ in range(l)]
        for i in range(l):
            for j in range(i, l):
                # print(S[i: j + 1])
                if S[i: j + 1] in words:
                    dp[i][j] = True
        print(np.array(dp))
        a = []
        for i in range(l):
            for j in range(l - 1, -1, -1):
                if dp[i][j]:
                    a.append([i, j])
                    break
        if a == []:
            return S
        start = a[0][0]
        end = a[0][1]
        result = []
        for i in a[1:]:
            if i[0] <= end + 1:
                end = max(end, i[1])
            else:
                result.append([start, end])
                start = i[0]
                end = i[1]
        result.append([start, end])
        print(result)
        ans = ''
        start = 0
        for i in result:
            ans += S[start:i[0]] + '<b>' + S[i[0]:i[1] + 1] + '</b>'
            start = i[1] + 1
        ans += S[start:]
        return ans

    def boldWords_1(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        55ms
        """
        n = len(S)
        b = [False] * n
        for w in words:
            t = S.find(w)
            l = len(w)
            while t > -1:
                for i in range(t, t + l):
                    b[i] = True
                t = S.find(w, t + 1)
        ans = ''
        i = 0
        while i < n:
            if b[i]:
                ans += r'<b>'
                while i < n and b[i]:
                    ans += S[i]
                    i += 1
                ans += r'</b>'
            else:
                ans += S[i]
                i += 1
        return ans



print(Solution().boldWords_1(words = ["ab", "bc"], S = "aabcd"))
# print(Solution().boldWords(["b","dee","a","ee","c"], "cebcecceab"))
# print(Solution().boldWords(["be","ba","ab","ba","adb"], "aaaadedcea"))