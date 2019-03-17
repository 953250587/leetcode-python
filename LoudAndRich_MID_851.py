"""
In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.



Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation:
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
Note:

1 <= quiet.length = N <= 500
0 <= quiet[i] < N, all quiet[i] are different.
0 <= richer.length <= N * (N-1) / 2
0 <= richer[i][j] < N
richer[i][0] != richer[i][1]
richer[i]'s are all different.
The observations in richer are all logically consistent.
"""


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
         219 ms
        """
        import collections
        dicts = collections.defaultdict(list)
        for rich in richer:
            dicts[rich[-1]].append(rich[0])

        ans = [-1] * len(quiet)
        def dfs(person_x):
            if dicts[person_x] == []:
                ans[person_x] = person_x
                return quiet[person_x], ans[person_x]
            a = quiet[person_x]
            a_p = person_x
            for person_y in dicts[person_x]:
                if ans[person_y] == -1:
                    b, P = dfs(person_y)
                else:
                    P = ans[person_y]
                    b = quiet[P]
                if a > b:
                    a = b
                    a_p = P
            ans[person_x] = a_p
            return a, a_p

        for i in range(len(quiet)):
            if ans[i] == -1:
                dfs(i)
        return ans

    def loudAndRich_1(self, richer, quiet):
        """
        250ms
        :param richer:
        :param quiet:
        :return:
        """
        import collections
        edges, memo, res = collections.defaultdict(list), {}, [i for i in range(len(quiet))]
        for r, p in richer: edges[p].append(r)

        def explore(i):
            if i in memo: return memo[i]
            cur_min = i
            for v in edges[i]:
                cur = explore(v)
                if quiet[cur] < quiet[cur_min]: cur_min = cur
            res[i] = memo[i] = cur_min
            return cur_min

        for i in range(len(quiet)): explore(i)
        return res

print(Solution().loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))

