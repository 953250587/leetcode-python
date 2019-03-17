"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

"""
886ms
"""
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dists = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        def insert_ch(dists, i):
            if i not in dists.keys():
                dists[i] = {}
                if 'word' not in dists.keys():
                    dists['word'] = False
            return dists[i]

        dists = self.dists
        for i in word:
            dists = insert_ch(dists, i)
        dists['word'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        dists = self.dists
        count=0

        def search_small(dists,count):
            for i in word[count:]:
                count+=1
                if i in dists.keys():
                    dists = dists[i]
                elif i == '.':
                    keys=dists.keys()
                    if len(keys)<=1:
                        # print(len(keys))
                        return False
                    for i in keys :
                        if i!='word' and search_small(dists[i], count):
                                return True
                    return False
                else:
                    return False
            if dists['word'] == True:
                return True
            else:
                return False


        return  search_small(dists, count)

        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)

import  collections
"""
169ms
"""
class WordDictionary_1(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
    
obj = WordDictionary()
obj.addWord("bad")
obj.addWord('dad')
obj.addWord('mad')
# print(obj.search('pad'))
# print(obj.search('bad'))
# print(obj.search('.ad'))
print(obj.search('....'))