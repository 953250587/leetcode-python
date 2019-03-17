"""
 Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:

Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:

Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        self.dicts={}
        def word2bit(word):

            table=['0' for i in range(26)]
            for char in word:
                if table[ord(char)-ord('a')] !='1':
                    table[ord(char) - ord('a')]='1'
            return  ''.join(table)

        l=len(words)
        if l<=0:
            return 0
        self.flag=True
        for i in words[0]:
            for word in words:
               string=word2bit(word)
               self.dicts[word]=string
               if i not in word:
                   self.flag=False
        if self.flag:
            return 0
        print(self.dicts)
        self.max=0

        def isSameChar(word1,word2):
            for i in range(26):
                a=int(word1[i])*int(word2[i])
                if a==1:
                    return False
            return True

        for i in range(l):
            for word in words[i+1:]:
                if isSameChar(self.dicts[words[i]],self.dicts[word]):
                    self.max=max(self.max,len(word)*len(words[i]))
        return self.max

    def maxProduct_1(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

words=["a", "aa", "aaa", "bbbb"]
words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
print(Solution().maxProduct(words))

