"""
 We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.

Example 1:

Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:

    bottom will be a string with length in range [2, 12].
    allowed will have length in range [0, 343].
    Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

"""


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        import collections
        dicts = collections.defaultdict(set)
        # self.allow = collections.defaultdict(set)
        for allow in allowed:
            dicts[allow[0:2]].add(allow[-1])
        def dfs(s, c):
            if len(s) == 1 and s + c in dicts:
                return True
            for i in dicts[s[-1] + c]:
                for j in dicts[s]:
                    dicts[s + c].add(j + i)
            for i in dicts[s[-1] + c]:
                for j in dicts[s]:
                    if dfs(j, i):
                        return True
            return False
        for i in range(1, len(bottom)):
            # print(dicts)
            if not dfs(bottom[0:i], bottom[i]):
                return False
        return True

    def pyramidTransition_1(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        85ms worry ans
        """
        allow = {}
        for a in allowed:
            if a[:2] in allow:
                allow[a[:2]].append(a[-1])
            else:
                allow[a[:2]] = [a[-1]]
        buff = []
        for l in bottom:
            ## need use set here to prevent duplicates
            buff.append(set([l]))
        while buff:
            print(buff)
            if len(buff) == 1:
                return True
            temp = []
            for i in range(1, len(buff)):
                container = set([])
                for m in buff[i - 1]:
                    for n in buff[i]:
                        if m + n in allow:
                            container = container.union(allow[m + n])
                if not container:
                    return False
                temp.append(container)
            buff = temp
            print(buff)


# print(Solution().pyramidTransition(bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]))
# print(Solution().pyramidTransition_1(bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]))
print(Solution().pyramidTransition_1("ABCD", ["ABE","BCE","BCF","CDF","EEG","FFA","GAA"]))
print(Solution().pyramidTransition_1("AAAA",["AAB","AAC","BCD","BBE","DEF"]))
# print(Solution().pyramidTransition("DB", ["BDD","ACA","CBA","BDC","AAC","DCB","ABC","DDA","CCB"]))
# print(Solution().pyramidTransition("CB", ["CDD","CBC","ACA","BDD","ADD","DCA","BAD","ADA"]))
# print(Solution().pyramidTransition("CACAC",
# ["ACB","AAC","AAB","BCD","BCC","BAA","CCD","CCA","CAD","DAD","DAC","DCD","ACD","DCA","ABA","BDA","BDC","BDB","BBA","ADD","ADC","CDB","DDA","CBB","CBC","CBA","CDA","CBD","DBA","DBC","DBD"]))
print(Solution().pyramidTransition_1("CACAC",
["ACB","AAC","AAB","BCD","BCC","BAA","CCD","CCA","CAD","DAD","DAC","DCD","ACD","DCA","ABA","BDA","BDC","BDB","BBA","ADD","ADC","CDB","DDA","CBB","CBC","CBA","CDA","CBD","DBA","DBC","DBD"]))