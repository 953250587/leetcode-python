"""
 You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
题目的意思是给你一个字符串，和一个字符串的数组，需要返回一个该字符串的索引组成的数组，
返回的索引有如下性质：从每个索引开始，长度为L的字串需要精确包含字符串数组中的所有字符串（不多不少）。
L 为字符串数组中所有字符串长度之和。
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        129ms
        """

        if len(words) <= 0:
            return []
        l = len(words[0])
        l_w = len(words)
        dicts = {}
        for i in range(l):
            dicts[i] = {}
            for word in words:
                if word not in dicts[i]:
                    dicts[i][word] = 1
                else:
                    dicts[i][word] += 1
        start = 0
        count = 0
        result = []
        while start < len(s) - l_w * l + 1:
            d = start % l
            if start // l >= 1:
                count += 1
            if count == 0:
                for i in range(l_w):
                    key = s[start + l * i: start + l * (i + 1)]
                    if key in dicts[d]:
                        dicts[d][key] -= 1
            else:
                key = s[start + (l_w - 1) * l: start + l_w * l]
                if key in dicts[d]:
                    dicts[d][key] -= 1
            flag = True
            for key in dicts[d]:
                if dicts[d][key] != 0:
                    flag = False
                    break
            k = s[start : start + l]
            if k in dicts[d]:
                dicts[d][k] += 1
            if flag:
                result.append(start)
            start += 1
        return result

    def findSubstring_1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        52ms
        """
        s_len, w_len = len(s), len(words[0])
        w_len_total = len(words) * w_len
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        curr = {}
        res = []
        for start in range(w_len):
            curr = {}
            end = start
            while start + w_len_total <= s_len:
                sub = s[end:end + w_len]
                end += w_len
                if sub not in counter:
                    curr = {}
                    start = end
                else:
                    curr[sub] = curr.get(sub, 0) + 1
                    while curr[sub] > counter[sub]:
                        curr[s[start: start + w_len]] -= 1
                        start += w_len
                    if start + w_len_total == end:
                        res.append(start)
        return res

    def findSubstring_2(self, S, L):
        """
        656ms
        :param S:
        :param L:
        :return:
        """
        words = {}
        wordNum = len(L)
        for i in L:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
        wordLen = len(L[0])
        res = []
        for i in range(len(S) + 1 - wordLen * wordNum):
            curr = {}
            j = 0
            while j < wordNum:
                word = S[i + j * wordLen:i + j * wordLen + wordLen]
                if word not in words:
                    break
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if curr[word] > words[word]: break
                j += 1
            if j == wordNum: res.append(i)
        return res
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(Solution().findSubstring(s, words))

s = "foobbarfoobarhfdbarfoofoobar"
words = ["foo",'bar']
print(Solution().findSubstring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(Solution().findSubstring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(Solution().findSubstring(s, words))

s = "aaaaaaaa"
words = ["aa","aa","aa"]
print(Solution().findSubstring(s, words))

s = "ababaab"
words = ["ab","ba","ba"]
print(Solution().findSubstring(s, words))