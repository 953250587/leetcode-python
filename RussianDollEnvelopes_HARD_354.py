"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n <= 0:
            return 0
        envelopes = sorted(envelopes, key=lambda a:(a[0], a[1]))
        print(envelopes)
        dp = [1] * n
        for i, envelope in enumerate(envelopes):
            for j in range(0, i):
                if envelopes[j][0] < envelope[0] and envelopes[j][1] < envelope[1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)
# print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
# print(Solution().maxEnvelopes([]))
# print(Solution().maxEnvelopes([[1,1],[1,1],[1,1]]))
print(Solution().maxEnvelopes([[10,8],[1,12],[6,15],[2,18]]))


import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        82ms
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        h=[]
        for i,e in enumerate(envelopes,0):
            j=bisect.bisect_left(h,e[1])
            if j<len(h):
                h[j]=e[1]
            else:
                h.append(e[1])
        return len(h)