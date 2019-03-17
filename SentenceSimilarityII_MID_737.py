"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        489ms
        """
        import collections
        l1 = len(words1)
        l2 = len(words2)
        if l1 != l2:
            return False
        self.dict = collections.defaultdict(set)
        for pair in pairs:
            self.dict[pair[0]].add(pair[1])
            self.dict[pair[1]].add(pair[0])
        print(self.dict)


        def dfs(sets, similar_word):
            if similar_word in sets:
                return True
            for s in list(sets):
                if s not in self.sets:
                    self.sets.add(s)
                    if dfs(self.dict[s], similar_word):
                        return True
            return False

        for word in words1:
            self.dict[word].add(word)
            self.sets = set()
            temp = ''
            flag = False
            for word_2 in words2:
                temp = word_2
                if dfs(self.dict[word], word_2):
                    flag = True
                    break
            if flag:
                words2.remove(temp)
            else:
                return False
            print(words2)
        return True

    def areSentencesSimilarTwo_1(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        209ms
        """
        if len(words1) != len(words2):
            return False
        d = {}
        for i, j in pairs:
            if i not in d: d[i] = i
            if j not in d: d[j] = j
            self.union(i, j, d)

        for i, j in zip(words1, words2):
            if self.findSet(i, d) != self.findSet(j, d):
                return False
        return True

    def union(self, i, j, d):
        d[self.findSet(i, d)] = d[self.findSet(j, d)]

    def findSet(self, i, d):
        if i not in d:
            return i
        if i != d[i]:
            d[i] = self.findSet(d[i], d)  # path compression
        return d[i]

words1 = ["great", "acting", "skills"]
words2 = ["great", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"],["acting","drama"], ["skills","talent"]]
print(Solution().areSentencesSimilarTwo_1(words1, words2, pairs))

words1 = ["great"]
words2 = ["great"]
pairs = []
print(Solution().areSentencesSimilarTwo(words1, words2, pairs))