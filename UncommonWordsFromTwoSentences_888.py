"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        24 ms
        """
        import collections
        dict_a = collections.Counter(A.split())
        dict_b = collections.Counter(B.split())
        a = set(A.split())
        b = set(B.split())
        c = a.union(b)
        d = a.intersection(b)
        # print(d)
        # # a.union(b)
        # print(c)
        return [i for i in c.difference(d) if dict_a[i] == 1 or dict_b[i] == 1]

    def uncommonFromSentences_1(self, A, B):
        """
        20ms
        :param A:
        :param B:
        :return:
        """
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        # Alternatively:
        # count = collections.Counter(A.split())
        # count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]
print(Solution().uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour"))
print(Solution().uncommonFromSentences(A = "apple apple", B = "banana"))