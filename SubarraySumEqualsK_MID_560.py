"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_1 = 0
        result = 0
        self.dict = {0: 1}
        for i, num in enumerate(nums):
            sum_1 += num
            if sum_1 - k in self.dict.keys():
                result += self.dict[sum_1 - k]
            if sum_1 not in self.dict.keys():
                self.dict[sum_1] = 0
            self.dict[sum_1] += 1
        print(self.dict)
        return result

    def subarraySum_1(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        122MS
        """
        import collections
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su - K]
            count[su] += 1
        return ans

    def subarraySum_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        72ms
        """
        import collections
        n = 0
        sj_nj = collections.defaultdict(int)
        sj_nj[0] = 1;
        sj = 0
        for num in nums:
            sj += num
            if sj - k in sj_nj:
                n += sj_nj[sj - k]
            sj_nj[sj] += 1

        return n

    def subarraySum_3(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            d = {}
            s = 0
            n = 0
            for i, x in enumerate(nums):
                s += x
                if s == k:
                    n += 1
                if s - k in d:
                    n += d[s - k]
                d[s] = 1 if s not in d else 1 + d[s]
            return n
nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))

nums = [1, 2, -1, 1]
k = 2
print(Solution().subarraySum(nums, k))

nums = [0, -1, 1]
k = 0
print(Solution().subarraySum(nums, k))