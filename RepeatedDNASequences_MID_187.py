"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
import collections
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        out of time
        """

        class TreeNode(object):
            def __init__(self, x):
                self.val = x
                self.A = None
                self.C = None
                self.G = None
                self.T = None

        def createTree(root, i, s, count):
            if i == 10:
                return count==10
            if s[i] == 'A':
                if root.A==None:
                    newTree = TreeNode(1)
                    root.A = newTree
                else:
                    count+=1
                return createTree(root.A, i + 1, s, count)
            elif s[i] == 'C':
                if root.C==None:
                    newTree = TreeNode(1)
                    root.C = newTree
                else:
                    count += 1
                return createTree(root.C, i + 1, s, count)
            elif s[i] == 'G':
                if root.G==None:
                    newTree = TreeNode(1)
                    root.G = newTree
                else:
                    count += 1
                return createTree(root.G, i + 1, s, count)
            else:
                if root.T==None:
                    newTree = TreeNode(1)
                    root.T = newTree
                else:
                    count += 1
                return createTree(root.T, i + 1, s, count)
        s_all=set()
        root=TreeNode(0)
        for i in range(len(s)-9):
            a=s[i:i+10]
            if createTree(root,0,a,0):
                s_all.add(a)
        return list(s_all)

    def findRepeatedDnaSequences_1(self, s):
        # 232ms
        table = collections.defaultdict(int)
        for i in range(len(s) - 9):
            table[s[i: i+10]] += 1
        return map(lambda x: x[0], filter(lambda x: x[1] > 1, table.items()))

    def findRepeatedDnaSequences_2(self, s):
        # 132ms,
        r, record = set(), set()
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            # False=0,True=1,不用dict，dict太多重复，费时间，用set保证不重复
            [record, r][substring in record].add(substring)
        return list(r)

# print(Solution().findRepeatedDnaSequences_2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

r, record = set(), set()
nums=[0,1,2,3,4,1,2,10]
print(nums[True+1],nums[False])
for i in nums:
    substring = i
    [record, r][False].add(substring)
    print([record, r])