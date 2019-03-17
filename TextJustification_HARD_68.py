"""
 Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

Corner Cases:

    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
"""
import numpy as np
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        33ms
        """
        count = 0
        start = 0
        result = []
        for i, word in enumerate(words):
            count += len(word)
            if count > maxWidth:
                result.append([start, i - 1, count - len(word) - 1])
                start = i
                count = len(word)
            count += 1
        result.append([start, i, count - 1])
        print(result)
        ans = []
        for i in result[:-1]:
            remain_blank = maxWidth - i[-1]
            need_blank = i[1] - i[0]
            s = ''
            if need_blank != 0:
                basic_blank = remain_blank // need_blank
                extra_blank = remain_blank % need_blank
                count = 0
                for k in range(i[0], i[1]):
                    s += words[k]
                    s += ' ' * (basic_blank + 1)
                    if count < extra_blank:
                        s += ' '
                    count += 1
                s += words[i[1]]
            else:
                s += words[i[0]] + ' ' * (maxWidth - i[-1])
            ans.append(s)
        s = ''
        a = result[-1]
        for k in range(a[0], a[1]):
            s += words[k]
            s += ' '
        s += words[a[1]] + ' ' * (maxWidth - a[-1])
        ans.append(s)
        print(ans)
        return ans

    def fullJustify_1(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        32ms
        """
        # nol is current total characters count of current line excluding all ' '
        # curLineWords is current count of words in current line
        # w is the next word we want to insert
        nol, res, curLineWords = 0, [], []
        for w in words:
            if (nol + len(curLineWords) + len(w) > maxWidth):
                for i in range(maxWidth - nol):
                    # rotating add ' ' to the end of words, mod of 0 is illegal so add 1 to the end to deal with only 1 word in this line situation
                    curLineWords[i % (len(curLineWords) - 1 or 1)] += ' '
                res.append(''.join(curLineWords))
                curLineWords, nol = [], 0
            # append is adding a new list, "+" is extend list like java "+" string
            curLineWords += [w]
            nol += len(w)
        # this return statement means adding remaining word to the last list, not a new list, because the if statement in for loop already guarantee curLineWords will be fitted in to maxWidth
        # This method returns the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).
        return res + [' '.join(curLineWords).ljust(maxWidth)]

words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
print(Solution().fullJustify(words, L))

words = ["This", "is", "an", "example", "of", "text", 'just', 'ifica', 'tion.']
L = 16
print(Solution().fullJustify(words, L))

words = ["a","b","c","d","e"]
L = 3
print(Solution().fullJustify(words, L))