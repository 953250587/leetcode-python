"""
 Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1

Note:

    words has length in range [1, 15000].
    For each test case, up to words.length queries WordFilter.f may be made.
    words[i] has length in range [1, 10].
    prefix, suffix have lengths in range [0, 10].
    words[i] and prefix, suffix queries consist of lowercase letters only.

"""


class WordFilter_2(object):
    """
    648ms
    """

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie_prefix = {'weight':set()}
        self.trie_suffix = {'weight':set()}
        self.weights = {}
        for i, word in enumerate(words):
            dicts = self.trie_prefix
            dicts['weight'].add(word)
            for char in word:
                if char not in dicts:
                    dicts[char] = {'weight' : set()}
                dicts[char]['weight'].add(word)
                dicts = dicts[char]
            dicts_suf = self.trie_suffix
            dicts_suf['weight'].add(word)
            for char in word[::-1]:
                if char not in dicts_suf:
                    dicts_suf[char] = {'weight' : set()}
                dicts_suf[char]['weight'].add(word)
                dicts_suf = dicts_suf[char]
            self.weights[word] = i
        print(self.trie_prefix)
        print(self.trie_suffix)
        print(self.weights)



    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        dicts = self.trie_prefix
        for char in prefix:
            if char in dicts:
                dicts = dicts[char]
            else:
                return -1
        a = dicts['weight']
        dicts = self.trie_suffix
        for char in suffix[::-1]:
            if char in dicts:
                dicts = dicts[char]
            else:
                return -1
        b = dicts['weight']
        c = a & b
        print('a', a)
        print('b', b)
        weight = -1
        for word in c:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight




        # Your WordFilter object will be instantiated and called as such:
        # obj = WordFilter(words)
        # param_1 = obj.f(prefix,suffix)

words = ['apple']
obj = WordFilter_2(words)
print(obj.f("a", ""))
print(obj.f("b", ""))

#
# class WordFilter(object):
#
#     def __init__(self, words):
#         """
#         :type words: List[str]
#         """
#         from collections import defaultdict
#         self.trie_prefix = defaultdict(set)
#         self.trie_suffix = defaultdict(set)
#         for i, word in enumerate(words):
#             l = len(word)
#             key = ''
#             key_1 = ''
#             self.trie_prefix[key].add(i)
#             self.trie_suffix[key_1].add(i)
#             for k in range(l):
#                 key += word[k]
#                 self.trie_prefix[key].add(i)
#             for char in list(word[::-1]):
#                 key_1 += char
#                 self.trie_suffix[key_1[::-1]].add(i)
#         print(self.trie_prefix)
#         print(self.trie_suffix)
#
#     def f(self, prefix, suffix):
#         """
#         :type prefix: str
#         :type suffix: str
#         :rtype: int
#         """
#         weight = -1
#         for word in self.trie_prefix[prefix] & self.trie_suffix[suffix]:
#             if word > weight:
#                 weight = word
#         return weight

# words = ['apple']
# obj = WordFilter(words)
# print(obj.f("a", ""))
# print(obj.f("b", ""))
#
#
# class WordFilter_1(object):
#     """
#     655ms
#     """
#
#     def __init__(self, words):
#         from collections import defaultdict
#         self.prefixes = defaultdict(set)
#         self.suffixes = defaultdict(set)
#         self.weights = {}
#         for index, word in enumerate(words):
#             prefix, suffix = '', ''
#             for char in [''] + list(word):
#                 prefix += char
#                 self.prefixes[prefix].add(word)
#             for char in [''] + list(word[::-1]):
#                 suffix += char
#                 self.suffixes[suffix[::-1]].add(word)
#             self.weights[word] = index
#
#     def f(self, prefix, suffix):
#         weight = -1
#         for word in self.prefixes[prefix] & self.suffixes[suffix]:
#             if self.weights[word] > weight:
#                 weight = self.weights[word]
#         return weight


words =["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
obj = WordFilter_2(words)
print(obj.f("bccbacbcba","a"))
print(obj.f("ab","abcaccbcaa"))
print(obj.f("a","aa"))
print(obj.f("cabaaba","abaaaa"))
print(obj.f("cacc","accbbcbab"))
print(obj.f("ccbcab","bac"))
print(obj.f("bac","cba"))
print(obj.f("ac","accabaccaa"))
print(obj.f("bcbb","aa"))
print(obj.f("ccbca","cbcababac"))

# print('ok')
#
# obj = WordFilter_1(words)
# print(obj.f("bccbacbcba","a"))
# print(obj.f("ab","abcaccbcaa"))
# print(obj.f("a","aa"))
# print(obj.f("cabaaba","abaaaa"))
# print(obj.f("cacc","accbbcbab"))
# print(obj.f("ccbcab","bac"))
# print(obj.f("bac","cba"))
# print(obj.f("ac","accabaccaa"))
# print(obj.f("bcbb","aa"))
# print(obj.f("ccbca","cbcababac"))