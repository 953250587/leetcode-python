"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

"""
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
         297 ms
        """
        sub_A, sub_B = '', ''
        for i in range(len(A)):
            if A[i] != B[i]:
                sub_A += A[i]
                sub_B += B[i]
        if sub_A == '':
            return 0
        sub_A = tuple(sub_A)
        sub_B = tuple(sub_B)
        start = [(sub_A, sub_B)]
        used = set([(sub_A, sub_B)])
        ans = 0
        while start:
            ans += 1
            tmp = set()
            for a,b in start:
                for i in range(len(a)):
                    if a[i] == b[0]:
                        nst = list(a)
                        nst[i] = a[0]
                        j = 1
                        while j < len(nst) and nst[j] == b[j]:
                            j += 1
                        if j == len(nst):
                            return ans
                        nst = nst[j:]
                        ned = b[j:]
                        nst = tuple(nst)
                        if (nst, ned) not in used:
                            used.add((nst, ned))
                            tmp.add((nst, ned))
            start = tmp
        return ans


def kSimilarity(self, A, B):
    """
    818ms
    :param self:
    :param A:
    :param B:
    :return:
    """
    import collections
    def neighbors(S):
        for i, c in enumerate(S):
            if c != B[i]:
                break

        T = list(S)
        for j in xrange(i + 1, len(S)):
            if S[j] == B[i]:
                T[i], T[j] = T[j], T[i]
                yield "".join(T)
                T[j], T[i] = T[i], T[j]

    queue = collections.deque([A])
    seen = {A: 0}
    while queue:
        S = queue.popleft()
        if S == B: return seen[S]
        for T in neighbors(S):
            if T not in seen:
                seen[T] = seen[S] + 1
                queue.append(T)



print(Solution().kSimilarity(A = "ab", B = "ba"))
print(Solution().kSimilarity(A = "abc", B = "bca"))
print(Solution().kSimilarity(A = "abac", B = "baca"))
print(Solution().kSimilarity(A = "aabc", B = "abca"))








