"""
 Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point.

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

Example 1:
Input: [2, 3, 1, 4, 0]
Output: 3
Explanation:
Scores for each K are listed below:
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3

So we should choose K = 3, which has the highest score.



Example 2:
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation:  A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.

Note:

    A will have length at most 20000.
    A[i] will be in the range [0, A.length].


"""
class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        880ms
        """
        result = [0, 0]
        l = len(A)
        L = [0] * (l + 1)
        for i, a in enumerate(A):
            if i - a >= 0:
                L[i - a] += 1
        s = 0
        max_index = l - 1
        for i in range(l):
            print(L)
            a = L.pop(0)
            L.append(0)
            s -= a
            if max_index - A[i] >= 0:
                L[max_index - A[i]] += 1
                s += 1
            if s > result[0]:
                result = [s, i + 1]
        return result[1]

    def bestRotation_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        119ms
        """
        result = [0, 0]
        l = len(A)
        L = [0] * (l + 1)
        for i, a in enumerate(A):
            if i - a >= 0:
                L[i - a] += 1
        s = 0
        max_index = l - 1
        for i in range(l):
            # print(L)
            a = L[i]
            L.append(0)
            s -= a
            if max_index - A[i] >= 0:
                L[max_index - A[i] + i + 1] += 1
                s += 1
            if s > result[0]:
                result = [s, i + 1]
        return result[1]

    def bestRotation_2(self, A):
        """
        127ms
        :param A:
        :return:
        """
        N = len(A)
        change = [1] * N
        """
        (i - A[i] + N) % N is the value of K making A[i]'s index just equal to A[i].
         For example, If A[6] = 1, then K = (6 - A[6]) % 6 = 5 making A[6] to index 1 of new array.
         So when K=5, we get this point for A[6]
         Then if K is bigger when K = (i - A[i] + 1) % N, we start to lose this point, making our score -= 1
         All I have done is record the value of K for all A[i] where we will lose points.
        """
        for i in range(N): change[(i - A[i] + 1) % N] -= 1
        # 记录每次的变化
        for i in range(1, N): change[i] += change[i - 1]
        return change.index(max(change))
print(Solution().bestRotation([2, 3, 1, 4, 0]))
print(Solution().bestRotation([1, 3, 0, 2, 4]))
