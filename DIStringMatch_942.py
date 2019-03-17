"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]


Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        100 ms
        """
        l = len(S)
        used = [i for i in range(l + 1)]
        result = []
        if S[0] == 'I':
            result.append(0)
            used = used[1:]
        else:
            result.append(l)
            used.pop()
        start, end, new_start, new_end = 0, l, 0, l
        while start < end:
            temp = S[start]
            count = 0
            # 计算连续的个数
            while start < end and S[start] == temp:
                start += 1
                count += 1
            # 如果是递增，则从可以用的末尾按顺序取出来
            if temp == 'I':
                result.extend(used[new_end - count:new_end])
                new_end -= count
            # 如果是递减，则从可用的开头取出来倒叙放入
            else:
                result.extend(used[new_start:new_start + count][::-1])
                new_start += count
        return result

    def diStringMatch_1(self, S):
        """
        :type S: str
        :rtype: List[int]
        124ms
        """
        ans = []
        lo, hi = 0, len(S)
        for i in S:
            if i == 'I':
                ans.append(lo)
                lo = lo + 1
            else:
                ans.append(hi)
                hi = hi - 1
        ans = ans + [lo]
        return ans


print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
print(Solution().diStringMatch("D"))
print(Solution().diStringMatch("I"))