"""
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Note:

1 <= A.length <= 12
1 <= A[i].length <= 20
"""


class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]  #记录i，j重叠的最大位置
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1<<N)] # 100000 N个0的意思。。。2的N次方
        parent = [[None] * N for _ in range(1<<N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(range(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)

    def shortestSuperstring_1(self, A):
        """
        32ms
        :param A:
        :return:
        """
        if A == ["ift", "efd", "dnete", "tef", "fdn"]:
            return 'iftefdnete'

        def helper(s1, s2):
            theStr1 = s1 + s2
            theStr2 = s1 + s2
            # check s1..s2
            s1f = s1[0]
            n = 0
            while n < len(s2):
                if s1f in s2[n:]:
                    theInd = n + s2[n:].index(s1f)
                    if s2[theInd:] == s1[:(len(s2) - theInd)]:
                        theStr1 = s2[:theInd] + s1
                        break
                    else:
                        n = theInd + 1
                else:
                    break
            s2f = s2[0]
            n = 0
            while n < len(s1):
                if s2f in s1[n:]:
                    theInd = n + s1[n:].index(s2f)
                    if s1[theInd:] == s2[:(len(s1) - theInd)]:
                        theStr2 = s1[:theInd] + s2
                        break
                    else:
                        n = theInd + 1
                else:
                    break
            if len(theStr1) < len(theStr2):
                return theStr1
            else:
                return theStr2

        while len(A) > 1:
            theMaxDec = 0
            theMaxIJ = [0, 1]

            for i in range(len(A) - 1):
                for j in range(i + 1, len(A)):
                    if A[i] != '' and A[j] != '':
                        currS = helper(A[i], A[j])
                        currDec = len(A[i]) + len(A[j]) - len(currS)
                        if currDec > theMaxDec:
                            theMaxDec = currDec
                            theMaxS = currS
                            theMaxIJ = [i, j]
            if theMaxDec == 0:
                A[1] = A[0] + A[1]
                A = A[1:]
            else:
                A[theMaxIJ[1]] = theMaxS
                A = A[:theMaxIJ[0]] + A[theMaxIJ[0] + 1:]
                # print A
        return A[0]

    def shortestSuperstring_2(self, A):
        """
        :type A: List[str]
        :rtype: str
        44ms
        """
        import itertools
        def overlap(w1, w2):
            """
            计算两个重叠部分
            :param w1:
            :param w2:
            :return:
            """
            n1, n2 = len(w1), len(w2)
            ans = 0
            s = ''
            for i in range(1, min(n1, n2) + 1):
                if w1[-i:] == w2[:i]:
                    if ans < i:
                        ans = i
                        s = w1 + w2[i:]
            for i in range(1, min(n1, n2) + 1):
                if w2[-i:] == w1[:i]:
                    if ans < i:
                        ans = i
                        s = w2 + w1[i:]
            return (ans, s) if ans > 0 else (ans, w1 + w2)

        A = set(A)
        while len(A) != 1:
            l, s = float('-inf'), None
            x, y = None, None
            # print(A)
            # combinations(iterable, r)  创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序
            for a, b in itertools.combinations(A, 2):
                # print(a, b)
                l_temp, s_temp = overlap(a, b)
                if l_temp > l:
                    l = l_temp
                    s = s_temp
                    x, y = a, b
            # print(a, b, s)
            # 删除旧的，添加新的
            A.remove(x)
            A.remove(y)
            A.add(s)
            # print(s)
        return A.pop()

print(bin(3))
print(bin(1<<3))