"""
 Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        969ms
        """
        pre_dicts = {}
        ans = set()
        for i, word in enumerate(words):
            pre_dicts[word] = i
        for word in words:
            l = len(word)
            for i in range(l):
                left = i
                right = l - i - 1
                if left < right:
                    if word[:left] == word[i + 1: i + 1 + left][::-1]:
                        b = word[i + 1 + left:][::-1]
                        if b in pre_dicts and b != word:
                            ans.add((pre_dicts[b], pre_dicts[word]))
                elif left > right:
                    if word[i - right :i] == word[i + 1: ][::-1]:
                        b = word[: i-right][::-1]
                        if b in pre_dicts and b != word:
                            ans.add((pre_dicts[word], pre_dicts[b]))
                else:
                    if word[:left] == word[i + 1:][::-1]:
                        if '' in pre_dicts and word != '':
                            ans.add((pre_dicts[''], pre_dicts[word]))
                            ans.add((pre_dicts[word], pre_dicts['']))
                left = i
                right = l - i
                if left < right:
                    if word[:left] == word[i: i + left][::-1]:
                        b = word[i + left:][::-1]
                        if b in pre_dicts and b != word:
                            ans.add((pre_dicts[b], pre_dicts[word]))
                elif left > right:
                    if word[i - right :i] == word[i: ][::-1]:
                        b = word[: i-right][::-1]
                        if b in pre_dicts and b != word:
                            ans.add((pre_dicts[word], pre_dicts[b]))
                else:
                    if word[:left] == word[i:][::-1]:
                        if '' in pre_dicts and word != '':
                            ans.add((pre_dicts[''], pre_dicts[word]))
                            ans.add((pre_dicts[word], pre_dicts['']))
        result = []
        for a in ans:
            result.append(list(a))
        return result

    def palindromePairs_1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        652ms
        """
        res = []
        m = {}
        for i, w in enumerate(words):
            m[w[::-1]] = i
        for i, w in enumerate(words):
            if '' in m and self.is_palindrome(w) and m[''] != i:
                # Handle ('' | palidrome w) here,
                # (palidrome w | '') is handled in the left branch below.
                res.append([m[''], i])
            for k in range(len(w)):
                left = w[0:k]
                right = w[k:]
                if left in m and m[left] != i and self.is_palindrome(right):
                    # left | palindrome right | reverse left found
                    # where left could be empty string
                    res.append([i, m[left]])
                if right in m and m[right] != i and self.is_palindrome(left):
                    # reverse right found | palindrome left | right
                    res.append([m[right], i])
        return res

    def is_palindrome(self, word):
        return word == word[::-1]
print(Solution().palindromePairs(words = ["bat", "tab", "cat"]))
print(Solution().palindromePairs(words = ["abcd", "dcba", "lls", "s", "sssll"]))

from collections import defaultdict


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        552ms
        """
        reverse_words = defaultdict(int)
        for i, word in enumerate(words):
            reverse_words[word[::-1]] = i

        res = []
        if '' in words:
            for i, word in enumerate(words):
                if word and word == word[::-1]:
                    res.append([reverse_words[''], i])

        for i, word in enumerate(words):
            for j in range(len(word)):
                pre = word[:j]
                suf = word[j:]
                if pre in reverse_words and suf == suf[::-1] and i != reverse_words[pre]:
                    res.append([i, reverse_words[pre]])
                if suf in reverse_words and pre == pre[::-1] and i != reverse_words[suf]:
                    res.append([reverse_words[suf], i])

        return res


