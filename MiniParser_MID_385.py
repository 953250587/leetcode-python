"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

    String is non-empty.
    String does not contain white spaces.
    String contains only digits 0-9, [, - ,, ].

Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.

Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        135ms
        """
        if s[0]!='[':
            return int(s)
        self.l=len(s)
        self.s=s
        self.stack=[]
        self.num=0
        self.flag=False
        self.start=1
        self.f=False
        NestedInteger_1=NestedInteger()

        def NestedInteger_add(NestedInteger_all):
            if self.start>=self.l:
                return
            if self.s[self.start]=='[':
                NestedInteger_a = NestedInteger()
                NestedInteger_all.add(NestedInteger_a)
                self.start+=1
                NestedInteger_add(NestedInteger_a)
            if self.s[self.start].isdigit() or self.s[self.start]=='-':
                if self.s[self.start] == '-':
                    self.f = True
                    self.start += 1
                self.flag = True
                while self.s[self.start].isdigit():
                    self.num=self.num*10+int(self.s[self.start])
                    self.start+=1
                if self.f:
                    self.num=-self.num
            if self.s[self.start]==',':
                if self.flag:
                    NestedInteger_all.add(self.num)
                self.f=False
                self.flag = False
                self.num=0
                self.start+=1
                NestedInteger_add(NestedInteger_all)
            elif self.s[self.start]==']':
                if self.flag:
                    NestedInteger_all.add(self.num)
                self.f = False
                self.flag = False
                self.num = 0
                self.start+=1
                return

        NestedInteger_add(NestedInteger_1)
        return NestedInteger_1



