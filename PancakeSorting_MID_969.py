# -*- coding: UTF-8 -*-
"""
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:
Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Note:
1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]
"""


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        40 ms
        11.9 MB
        """
        """
        1.每次找出当前序列中最大的数值,把1到该数值位置进行一次翻转,在对全局进行一次翻转,这样最大的数值就会移动到最后
        2.保持末尾不变,继续重复1的步骤. 2n次就可以完成,n为列表长度.
        用时应该是O(n^2)
        example:
            [3, 2, 4, 1]
        1.=>[4, 2, 3, 1]
        2.=>[1, 3, 2, 4]
        1.=>[3, 1, 2, 4]
        2.=>[2, 1, 3, 4]
        1.=>[1, 2, 3, 4] 
        """
        # 找出最大值对应的索引
        def find_max(A):
            max = [-1, -1]
            for i in range(len(A)):
                if A[i] > max[0]:
                    max = [A[i], i]
            return max[-1]

        ans_list = []
        while len(A) > 1:
            temp = find_max(A)
            # 得到的索引是从0开始的,所以需要+1
            ans_list.append(temp + 1)
            ans_list.append(len(A))
            # 构建下一次的A
            A = A[:temp][::-1] + A[temp + 1:]
            A = A[::-1]

        return ans_list

    def pancakeSort_1(self, A):
        """
        32 ms
        12 MB
        :param A:
        :return:
        """
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res


if __name__ == '__main__':
    print(Solution().pancakeSort([3,2,4,1]))
    print(Solution().pancakeSort([1,2,3]))

