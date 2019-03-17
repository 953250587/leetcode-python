"""

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.

"""


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        160 ms  
        """
        if N >= K + W - 1 or K == 0:
            return 1.0
        elif K == 1:
            return N / W
        else:
            ans = 0.0
            p = [0.0 for _ in range(K)]
            p[0] = 1.0
            p[1] = 1 / W
            s = 0
            for i in range(2, K):
                s += p[i - 1]
                if i > W + 1:
                    s -= p[i - W - 1]
                elif i <= W:
                    p[i] += 1 / W
                p[i] += 1 / W * s

            start = max(0, K - W)
            end = K
            a = 0.0
            b = 0.0
            for i in range(start, end):
                a += (W - K + i + 1) / W * p[i]
                if i + W <= N:
                    c = (W - K + i + 1)
                else:
                    c = (N - K + 1)
                b += c / W * p[i]
            ans += b / a
        return ans
print(Solution().new21Game(N = 10, K = 1, W = 10))
print(Solution().new21Game(N = 6, K = 1, W = 10))
print(Solution().new21Game(N = 21, K = 17, W = 10))
print(Solution().new21Game(0, 0, 2))
print(Solution().new21Game(1, 0, 3))



