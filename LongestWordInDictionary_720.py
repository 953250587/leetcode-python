"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        232ms
        """
        words=sorted(words,key=lambda word:(len(word),word))
        print(words)
        dicts={}
        self.dicts=dicts
        result=''
        for word in words:
            dicts = self.dicts
            flag=True
            if len(word)==1:
                dicts[word]={}
            else:
                for char in word[0:-1]:
                    if char not in dicts.keys():
                        flag = False
                        break
                    dicts = dicts[char]
            if flag:
                dicts[word[-1]]={}
                if len(result)<len(word):
                    result=word
        print(self.dicts)
        return result

    def longestWord_1(self, words):
        """
        62ms
        :param words:
        :return:
        """
        words, resword, res = sorted(words), '', set()
        for word in words:
            if len(word) == 1 or word[:-1] in res:
                res.add(word)
                resword = word if resword == '' else word if len(word) > len(resword) else resword
        return resword


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(words))
words = ["w","wo","wor","worl", "world"]
print(Solution().longestWord(words))
words=["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
print(Solution().longestWord(words))
words=["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
print(Solution().longestWord(words))