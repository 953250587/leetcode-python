"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
"""


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        24 ms
        """
        s = 1
        memory = set()
        while s <= 10 ** 9:
            a = sorted(list(str(s)))
            stt = ''.join(a)
            memory.add(stt)
            s *= 2
        if ''.join(sorted(list(str(N)))) in memory:
            return True
        else:
            return False

    def reorderedPowerOf2_1(self, N):
        """
        24ms
        :param N:
        :return:
        """
        pows = []
        for q in range(0, 31):
            pows.append(2 ** q)
        candidates = []
        dim = len(str(N))
        for item in pows:
            if len(str(item)) == dim:
                if sorted(str(item)) == sorted(str(N)):
                    return True
        return False


s = '1234'
s = list(s)
print(s)

print(Solution().reorderedPowerOf2(1))
print(Solution().reorderedPowerOf2(10))
print(Solution().reorderedPowerOf2(16))
print(Solution().reorderedPowerOf2(24))
print(Solution().reorderedPowerOf2(46))