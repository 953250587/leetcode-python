"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
import random
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        66ms
        """
        l = len(nums)
        if l <= 1:
            return 0
        a = str(max(nums))
        k = len(a)
        def radixSort(A, k):
            for k in range(k):  # k轮排序
                s = [[] for i in range(10)]
                for i in A:
                    s[i // (10 ** k) % 10].append(i)
                A = [a for b in s for a in b]
            print(A)
            return A
        nums = radixSort(nums, k)
        temp = nums[0]
        max_1 = 0
        for num in nums[1:]:
            max_1 = max(max_1, num - temp)
            temp = num
        return max_1

    def maximumGap_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        49ms
        """
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = (b - a) / (len(nums) - 1)
        if (b - a) % (len(nums) - 1) > 0:
            size += 1
        bucket = [[None, None] for _ in range(len(nums))]
        for n in nums:
            b = bucket[(n - a) / size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))
A=[random.randint(1,9999) for i in range(10)]
print(A)
print(Solution().maximumGap(A))

