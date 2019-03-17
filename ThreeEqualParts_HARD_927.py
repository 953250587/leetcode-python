"""
Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i+1 < j, such that:

A[0], A[1], ..., A[i] is the first part;
A[i+1], A[i+2], ..., A[j-1] is the second part, and
A[j], A[j+1], ..., A[A.length - 1] is the third part.
All three parts have equal binary value.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.



Example 1:

Input: [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: [1,1,0,1,1]
Output: [-1,-1]


Note:

3 <= A.length <= 30000
A[i] == 0 or A[i] == 1
"""


class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        64 ms
        """
        positon = []
        # 记录每一个1的位置
        for i, a in enumerate(A):
            if a == 1:
                positon.append(i)
        s = len(positon)
        # 1的个数不能被3整除说明不可能
        if s % 3 != 0 or len(A) < 3:
            return [-1, -1]
        need = s // 3
        if need == 0:
            return [0, 2]
        # 找出每一段之间的间隔
        between_1, between_2 = positon[need] - positon[0], positon[need * 2] - positon[need]
        # 间隔不一致说明不能构成3个一样的情况
        for i in range(need):
            if positon[need + i] - positon[i] != between_1 or \
                                    positon[2 * need + i] - positon[need + i] != between_2:
                return [-1, -1]
        # 记录最后一段结尾为0的个数
        end = len(A) - positon[-1] - 1
        # 判断每一段之间的0的个数是否满足要求，满足则取出对应个数加到每段的末尾
        if min(positon[need] - positon[need - 1] - 1, positon[2 * need] - positon[2 * need - 1] - 1) >= end:
            return [positon[need - 1] + end, positon[2 * need - 1] + end + 1]
        else:
            return [-1, -1]

    def threeEqualParts_1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        40ms
        """
        s = sum(A)
        if s % 3: return [-1, -1]
        if s == 0: return [0, 2] if len(A) >= 3 else [-1, -1]
        s = s // 3
        i = 0
        j = len(A)
        t = 0
        while A[i] == 0: i += 1
        while t < s:
            j -= 1
            t += A[j]
        p = i + len(A) - j
        s1 = A[i:p]
        s3 = A[j:]
        if s1 != s3:
            return [-1, -1]
        while A[p] == 0: p += 1
        k = p + len(A) - j
        s2 = A[p:k]
        return [i + len(A) - j - 1, k] if s1 == s2 else [-1, -1]


print(Solution().threeEqualParts([1,0,1,0,1]))
print(Solution().threeEqualParts([1,1,0,1,1]))
print(Solution().threeEqualParts([0,0,0,0,0]))
print(Solution().threeEqualParts([0,0]))



