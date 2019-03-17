"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        1375ms
        """

        def binary_search_bisect(lst, x):
            import bisect
            i = bisect.bisect_left(lst, x)
            j = bisect.bisect_right(lst, x)
            if i != len(lst) and lst[i] == x:
                return j-i
            return 0

        def calc(A,B):
            result=[]
            for i in A:
                for j in B:
                    result.append(i+j)
            return sorted(result)
        A_1=calc(A,B)
        B_1=calc(C,D)
        if A==[]:
            return 0
        count=0
        temp=A_1[0]
        self.a=binary_search_bisect(B_1,-temp)
        for i in A_1:
            if i==temp:
                count+=self.a
            else:
                temp=i
                self.a = binary_search_bisect(B_1, -temp)
                count+=self.a
        return count

    def fourSumCount_1(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        412ms
        """
        AB = {}
        for a in A:
            for b in B:
                if (a + b in AB):
                    AB[a + b] += 1
                else:
                    AB[a + b] = 1

        sum = 0

        for c in C:
            for d in D:
                if (-c - d in AB):
                    sum += AB[-c - d]

        return sum

A = [0,1,-1]
B=[-1,1,0]
C=[0,0,1]
D=[-1,1,1]

print(Solution().fourSumCount(A,B,C,D))

A = []
B=[]
C=[]
D=[]

print(Solution().fourSumCount(A,B,C,D))