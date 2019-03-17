"""
 Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.dict = {}
        def dfs(strs):
            if strs in self.dict:
                return self.dict[strs]
            if len(strs) == 1:
                return set(strs)
            a = set()
            for i in range(1, len(strs)):
                set1 = dfs(strs[0: i])
                set2 = dfs(strs[i: ])
                for m in list(set1):
                    for j in list(set2):
                        a.add(m + j)
                        a.add(j + m)
                        if s2 == m + j or s2 == j + m:
                            return True
            self.dict[strs] = a
            return a
        b = dfs(s1)
        # print(self.dict)
        # if s2 in b:
        #     return True
        return False

    def isScramble_1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        62ms
        """
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

    def isScramble_2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        46ms
        """
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return s1 == s2
        d, d1, d2 = {}, {}, {}
        for i, s in enumerate(s1[:-1], 1):
            d[s] = d.get(s, 0) + 1
            d1[s2[i - 1]] = d1.get(s2[i - 1], 0) + 1
            d2[s2[-i]] = d2.get(s2[-i], 0) + 1
            if d == d1 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if d == d2 and self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s1) - i]):
                return True
        return False
print(Solution().isScramble("abcdefghijklmn","efghijklmncadb"))


