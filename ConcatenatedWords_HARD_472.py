"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:

    The number of elements of the given array will not exceed 10,000
    The length sum of elements in the given array will not exceed 600,000.
    All the input string will only include lower case letters.
    The returned elements order does not matter.

"""


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        1327ms
        """
        if len(words) <= 0:
            return []
        s = set(words)
        words = sorted(words, key=lambda a:len(a))
        # print(words)
        min_len = max(len(words[0]), 1)
        result = []
        def dfs(word, count):
            # print('ggg', word, count)
            if word == '' and count >= 2:
                return True
            elif len(word) < min_len and count < 2:
                return False
            start = min_len
            while start <= len(word):
                if word[:start] in s:
                    if dfs(word[start:], count + 1):
                        s.add(word)
                        return True
                start += 1
            return False
        for word in words:
            if dfs(word, 0):
                result.append(word)
        print(s)
        return result

    def findAllConcatenatedWordsInADict_1(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        1155ms
        """
        S = set(words)
        ans = []
        for word in words:
            if not word: continue
            stack = [0]
            seen = {0}
            M = len(word)
            while stack:
                node = stack.pop()
                if node == M:
                    ans.append(word)
                    break
                for j in range(M - node + 1):
                    if (word[node:node + j] in S and
                                    node + j not in seen and
                            (node > 0 or node + j != M)):
                        stack.append(node + j)
                        seen.add(node + j)

        return ans
print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(Solution().findAllConcatenatedWordsInADict([""]))


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        332ms
        """
        r = []
        m = {w for w in words}
        for w in words:
            if dfs(m, w):
                r.append(w)
        return r


def dfs(m, w):
    if len(w) <= 1:
        return False
    for i in range(1, len(w)):
        if w[:i] in m and (w[i:] in m or dfs(m, w[i:])):
            return True
    return False
