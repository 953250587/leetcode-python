"""
 Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:

    You may assume that all the inputs are consist of lowercase letters a-z.
    For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
    Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

"""


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        32ms
        """
        self.dicts = None

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dicts = dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        s = sorted(self.dicts, key = lambda a:len(a))
        print(s)
        l = len(word)
        for w in s:
            if len(w) > l:
                break
            if len(w) == l:
                count = 0
                for k in range(l):
                    if w[k] == word[k]:
                        count += 1
                print(count, l)
                if count == l - 1:
                    return True
        return False


        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)
obj = MagicDictionary()
obj.buildDict(["hello","hallo","leetcode"])
param_2 = obj.search('hello')
print(param_2)
param_2 = obj.search('hhllo')
print(param_2)
param_2 = obj.search('hell')
print(param_2)
param_2 = obj.search('leetcoded')
print(param_2)


class TrieNode(object):
    """
    33ms
    """
    def __init__(self):
        self.isLeaf = False
        self.child = {}


class MagicDictionary_1(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, d):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in d:
            self.insert(i)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i in word:
            if i not in cur.child:
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.isLeaf = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root, False)

    def _search(self, word, root, modified):
        if len(word) == 1:
            if modified:
                return word in root.child and root.child[word].isLeaf
            else:
                return any([c.isLeaf and k != word for k, c in root.child.iteritems()])
        for w, node in root.child.iteritems():
            if w == word[0] and self._search(word[1:], node, modified):
                return True
            elif w != word[0] and not modified and self._search(word[1:], node, True):
                return True
        return False