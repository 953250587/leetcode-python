"""
There are G people in a gang, and a list of various crimes they could commit.

The i-th crime generates a profit[i] and requires group[i] gang members to participate.

If a gang member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least P profit, and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation:
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation:
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).


Note:

1 <= G <= 100
0 <= P <= 100
1 <= group[i] <= 100
0 <= profit[i] <= 100
1 <= group.length = profit.length <= 100
"""
class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        import collections
        l = len(profit)
        memo = collections.defaultdict(int)
        def dfs(G, P, i):
            # print(G, P, i)
            if (G, P, i) in memo:
                return memo[(G, P, i)]
            if i >= l:
                P = max(P, 0)
                memo[(G, P, i)] += 1 if P == 0 else 0
                return memo[(G, P, i)]
            if G - group[i] >= 0:
                t = max(P - profit[i], 0)
                a = dfs(G - group[i], t, i + 1)
            else:
                a = 0
            t = max(P, 0)
            b = dfs(G, t, i + 1)
            memo[(G, t, i)] = (a + b) % (10**9 + 7)
            return memo[(G, t, i)]
        return dfs(G, P, 0)

    def profitableSchemes_1(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        1800 ms
        """
        dp = [[0 for _ in range(G + 1)] for _ in range(P + 1)]
        dp[0][0] = 1
        l = len(profit)
        for k in range(l):
            for i in range(P, -1, -1):
                for j in range(G - group[k], -1, -1):
                    dp[min(i + profit[k], P)][group[k] + j] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)

# print(Solution().profitableSchemes( G = 5, P = 3, group = [2,2], profit = [2,3]))
# print(Solution().profitableSchemes( G = 10, P = 5, group = [2,3,5], profit = [6,7,8]))
# print(Solution().profitableSchemes(10,1,[11,2,5,10,4,6,7,3,9,10],[2,1,1,2,2,1,1,1,0,1]))
# print(Solution().profitableSchemes(1,1,[2,2,2,2,2],[1,2,1,1,0]))
# print(Solution().profitableSchemes(5,3,[2,2],[2,3]))
# print(Solution().profitableSchemes(1,1,[1,1,1,1,2,2,1,2,1,1],[0,1,0,0,1,1,1,0,2,2]))
print(Solution().profitableSchemes_1(100,100,
[18,58,88,52,54,13,50,66,83,61,100,54,60,80,1,19,78,54,67,20,57,46,12,6,14,43,64,81,30,60,48,53,86,71,51,23,71,87,95,69,11,12,41,36,69,89,91,10,98,31,67,85,16,83,83,14,14,71,33,5,40,61,22,19,34,70,50,21,91,77,4,36,16,38,56,23,68,51,71,38,63,52,14,47,25,57,95,35,58,32,1,39,48,33,89,9,1,95,90,78],
[96,77,37,98,66,44,18,37,47,9,38,82,74,12,71,31,80,64,15,45,85,52,70,53,94,90,90,14,98,22,33,39,18,22,10,46,6,19,25,50,33,15,63,93,35,0,76,44,37,68,35,80,70,66,4,88,66,93,49,19,25,90,21,59,17,40,46,79,5,41,2,37,27,92,0,53,57,91,75,0,42,100,16,97,83,75,57,61,73,21,63,97,75,95,84,14,98,47,0,13]))
print(Solution().profitableSchemes(100,100,
[18,58,88,52,54,13,50,66,83,61,100,54,60,80,1,19,78,54,67,20,57,46,12,6,14,43,64,81,30,60,48,53,86,71,51,23,71,87,95,69,11,12,41,36,69,89,91,10,98,31,67,85,16,83,83,14,14,71,33,5,40,61,22,19,34,70,50,21,91,77,4,36,16,38,56,23,68,51,71,38,63,52,14,47,25,57,95,35,58,32,1,39,48,33,89,9,1,95,90,78],
[96,77,37,98,66,44,18,37,47,9,38,82,74,12,71,31,80,64,15,45,85,52,70,53,94,90,90,14,98,22,33,39,18,22,10,46,6,19,25,50,33,15,63,93,35,0,76,44,37,68,35,80,70,66,4,88,66,93,49,19,25,90,21,59,17,40,46,79,5,41,2,37,27,92,0,53,57,91,75,0,42,100,16,97,83,75,57,61,73,21,63,97,75,95,84,14,98,47,0,13]))
print(Solution().profitableSchemes_1(100,100,
[24,23,7,4,26,3,7,11,1,7,1,3,5,26,26,1,13,12,2,1,7,4,1,27,13,16,26,18,6,1,1,7,16,1,6,2,5,9,19,28,1,23,2,1,3,4,4,3,22,1,1,3,5,34,2,1,22,16,8,5,3,21,1,8,14,2,1,3,8,12,40,6,4,2,2,14,1,11,9,1,7,1,1,1,6,6,4,1,1,7,8,10,20,2,14,31,1,13,1,9],
[5,2,38,25,4,17,5,1,4,0,0,8,13,0,20,0,28,1,22,7,10,32,6,37,0,11,6,11,23,20,13,13,6,2,36,1,0,9,4,5,6,14,20,1,13,6,33,0,22,1,17,12,10,1,19,13,8,1,0,17,20,9,8,6,2,2,1,4,22,11,3,2,6,0,40,0,0,7,1,0,25,5,12,7,19,4,12,7,4,4,1,15,33,14,2,1,1,61,4,5]))