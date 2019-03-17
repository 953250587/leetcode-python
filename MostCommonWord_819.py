"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.



Note:

    1 <= paragraph.length <= 1000.
    1 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    Different words in paragraph are always separated by a space.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.

"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        51ms
        """
        import collections
        words = paragraph.split()
        wordss = []
        for word in words:
            w = ''
            for char in word:
                if char not in '!?\',;.':
                    w += char.lower()
                else:
                    wordss.append(w)
                    w = ''
            if w != '':
                wordss.append(w)
        print(wordss)
        max_word = ['', 0]
        dicts = collections.defaultdict(int)
        s = set(banned)
        for word in wordss:
            if word not in s:
                dicts[word] += 1
                if dicts[word] > max_word[1]:
                    max_word = [word, dicts[word]]
        return max_word[0]

    def mostCommonWord_1(self, paragraph, banned):
        """
        46ms
        :param paragraph:
        :param banned:
        :return:
        """
        import collections
        banset = set(banned)
        count = collections.Counter(
            word.strip("!?',;.") for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans
print(Solution().mostCommonWord("Bob hit a ball' the hit BALL flew far after it was hit.", ["hit"]))
