"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        39ms
        """
        if a %1337==0:
            return 0
        start=b[0]
        for i in b[1:]:
            start=(start*10+i)%1140
        return pow(a,start)%1337
print(11415%1140)
print(Solution().superPow(456,[1,1,4,1,5]))

