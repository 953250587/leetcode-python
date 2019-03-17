"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        72ms
        """
        nums=[i+1 for i in range(9)]
        # print(nums[-k:])
        if sum(nums[0:k])>n or sum(nums[-k:])<n:
            return []
        # nums_mark=[0 for i in range(9)]
        ans=[0 for i in range(k)]
        result=[]
        K=k
        def combinationSum2(start,k,n):
            if n<=0 or start>n:
                return
            if k==1:
                if n<=9:
                    ans[K-1]=n
                    result.append(copy.copy(ans))
                return
            for i in range(start,10):
                # print('k ',k,' i ' ,i)
                ans[K-k]=i
                combinationSum2(i + 1, k - 1, n - i)
        combinationSum2(1,k,n)
        return result


class Solution_1:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]):
            return []

        res = []
        self.sum_help(k, n, 1, [], res)
        return res

    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return

        if len(arr) > k or curr > 9:
            return

        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()

    def combinationSum3_3(self, k, n, start=1):
        return [[i] + c for i in range(start, 10) for c in self.combinationSum3(k - 1, n - i, i + 1)] if k > 1 else \
        [[], [[n]]][start <= n <= 9]
print(Solution().combinationSum3(3,15))


