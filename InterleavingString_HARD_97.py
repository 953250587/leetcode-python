"""
 Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        32ms
        """
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.l1 = len(s1)
        self.l2 = len(s2)
        self.l3 = len(s3)
        self.dict_s3 = {}
        # self.dp = [[False] * self.l2 for _ in range(self.l1)]
        # self.dp[0][0] = True
        if self.l1 + self.l2 != self.l3:
            return False
        def dfs(i, j, count):
            if (i, j) in self.dict_s3:
                return False
            print(i, j)
            # print(self.s3[ i + j + 1])
            # if i + j not in self.dict_s3:
            #     self.dict_s3[i + j] = sorted(self.s3[:i + j])
            # if sorted(self.s1[:i] + self.s2[:j]) != sorted(self.s3[:i + j]):
            #     return False
            if i + j >= self.l3:
                return True
            if i < self.l1:
                if self.s1[i] == self.s3[i + j]:
                    if dfs(i + 1, j, count + 1):
                        return True
            if j < self.l2:
                if self.s2[j] == self.s3[i + j]:
                    if dfs(i, j + 1, count + 1):
                        return True
            self.dict_s3[(i, j)] = False
            return False
        return dfs(0, 0, 0)

    def isInterleave_1(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        36ms
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False

        q, visited = [(0, 0)], set((0, 0))
        for x, y in q:
            if x + y == n3:
                return True
            if x + 1 <= n1 and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                q.append((x + 1, y))
                visited.add((x + 1, y))
            if y + 1 <= n2 and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                q.append((x, y + 1))
                visited.add((x, y + 1))
        return False
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# print(Solution().isInterleave(s1, s2, s3))
# s3 = "aadbbbaccc"
# print(Solution().isInterleave(s1, s2, s3))

# s1 = "abc"
# s2 = "def"
# s3 = 'abcdef'
# print(Solution().isInterleave(s1, s2, s3))

s1 = "cacbbbaaabbacbbbbabbcaccccabaaacacbcaacababbaabbaccacbaabac"
s2 = "cbcccabbbbaaacbaccbabaabbccbbbabacbaacccbbcaabaabbbcbcbab"
s3 = "ccbcccacbabbbbbbaaaaabbaaccbabbbbacbcbcbaacccbacabbaccbaaabcacbbcabaabacbbcaacaccbbacaabababaabbbaccbbcacbbacabbaacb"
print(Solution().isInterleave(s1, s2, s3))