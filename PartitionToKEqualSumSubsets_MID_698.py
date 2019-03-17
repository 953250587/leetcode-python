"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        46ms
        """
        a = sum(nums)
        if a % k != 0:
            return False
        one = a // k
        print(one)
        self.nums_copy = nums
        def _sum_one(start, count, l):
            print(count)
            print('ss', self.nums_copy)
            if start >= l:
                return False
            if count == self.nums[start]:
                self.nums_copy.remove(self.nums[start])
                return True
            if count > self.nums[start]:
                self.nums_copy.remove(self.nums[start])
                if _sum_one(start + 1, count - self.nums[start], l):
                    return True
                self.nums_copy.append(self.nums[start])
            return _sum_one(start + 1, count, l)
        for i in range(k):
            self.nums = sorted(self.nums_copy, reverse=True)
            print(self.nums)
            if not _sum_one(0, one, len(self.nums)):
                return False
            print(self.nums_copy)
        return True

    def canPartitionKSubsets_1(self, x, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        39ms
        """
        size = len(x)

        def partition(t, k, m, i, s):
            if k <= 1:
                return True

            for j in range(i, size):
                a, y = 1 << j, s + x[j]
                if m & a:
                    # sub-problem 1: getting closer to a parition
                    if y < t and partition(t, k, m ^ a, j + 1, y):
                        return True
                    # sub-problem 2: search other partitions
                    elif y == t and partition(t, k - 1, m ^ a, 0, 0):
                        return True
            return False

        # fast path 1
        n = sum(x)
        if n % k:
            return False
        else:
            # fast path 2
            x.sort(reverse=True)  # XXX
            if x[0] > n / k:
                return False

        return partition(n / k, k, (1 << size) - 1, 0, 0)


# print(Solution().canPartitionKSubsets(nums = [1] * 16, k = 8))
print(Solution().canPartitionKSubsets([2,6,16,13,3,4,1,1,2,12], 3))