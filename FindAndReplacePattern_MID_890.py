"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.


Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        28ms
        """
        def isPattern(word, parttern):
            dict = {}
            l = len(word)
            used = set()
            for i in range(l):
                if pattern[i] in dict:
                    if dict[pattern[i]] != word[i]:
                        return False
                elif word[i] not in used:
                    dict[pattern[i]] = word[i]
                    used.add(word[i])
                else:
                    return False
            return True
        result = []
        for word in words:
            if isPattern(word, pattern):
                result.append(word)
        return result

    def findAndReplacePattern_1(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))

