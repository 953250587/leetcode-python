"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.

"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        55ms
        """
        import bisect, collections
        k_list = []
        self.dict = collections.Counter(words)
        result = sorted(self.dict.items(), key = lambda a:(-a[1], a[0]))
        s = []
        for i in result[0: k]:
            s.append(i[0])
        return s


    def topKFrequent_1(self, words, k):
        """
        52ms
        :param words:
        :param k:
        :return:
        """
        from heapq import *
        m = {}
        for word in words:
            if word in m:
                m[word] += 1
            else:
                m[word] = 1
        h = []
        for key, val in m.iteritems():
            heappush(h, (-1 * val, key))

        ret = []
        for i in range(k):
            ret.append(heappop(h)[1])
        return ret


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))