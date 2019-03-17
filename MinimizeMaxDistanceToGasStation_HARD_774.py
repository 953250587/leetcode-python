"""
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000

Note:

    stations.length will be an integer in range [10, 2000].
    stations[i] will be an integer in range [0, 10^8].
    K will be an integer in range [1, 10^6].
    Answers within 10^-6 of the true value will be accepted as correct
"""


class Solution(object):
    def minmaxGasDist(self, st, K):
        """
        1449ms
        :param st:
        :param K:
        :return:
        """
        import math
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += max(0, math.ceil((b - a) / mid) - 1)
            if count > K:
                left = mid
            else:
                right = mid
        return right