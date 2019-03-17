"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        48 ms
        """
        dicts = {}
        for i, char in enumerate(order):
            dicts[char] = chr(ord('a') + i)
        new_words = []
        # 替换字符，然后判断排序后的结果和原结果是否一致
        for word in words:
            lists = list(word)
            new_words.append(''.join([dicts[i] for i in lists]))
        return new_words == sorted(new_words)

    def isAlienSorted_1(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        24MS
        """
        # 本质思想一致，不过它是一个个去比较，能提早跳出
        def is_valid(a, b, alphabet):
            for i, char in enumerate(a):
                if i < len(b):
                    if alphabet[a[i]] < alphabet[b[i]]:
                        return True
                    elif alphabet[a[i]] > alphabet[b[i]]:
                        return False
                else:
                    return False

            return True

        alphabet = {}
        for i, char in enumerate(order):
            alphabet[char] = i

        for i, word in enumerate(words[:-1]):
            if is_valid(word, words[i + 1], alphabet):
                continue
            else:
                return False

        return True

print(Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))