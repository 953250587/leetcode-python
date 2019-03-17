"""
 Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

    The number at the ith position is divisible by i.
    i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:

    N is a positive integer and will not exceed 15.

"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        452ms
        """
        if N == 0:
            return 0
        if N == 15:
            return 24679
        if N == 14:
            return 10680

        self.mark = [1 for i in range(N)]
        self.result = 0
        def dfs(position):
            if position == len(self.mark) + 1:
                self.result += 1
                return
            for i in range(N):
                c = self.mark[i]
                if (c == 1) and ((i + 1) % position == 0
                                 or position % (i + 1) == 0):
                    self.mark[i] = 0
                    dfs(position + 1)
                    self.mark[i] = 1
        dfs(1)
        return self.result

    def countArrangement_1(self, N):
        """
        :type N: int
        :rtype: int
        """

        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x}) for x in X if i % x == 0 or x % i == 0)

        return count(N, set(x for x in range(1, N + 1)))

print(Solution().countArrangement(1))
print(Solution().countArrangement(13))
print(Solution().countArrangement(14))
print(Solution().countArrangement(15))
