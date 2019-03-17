"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:

    The length of the given array won't exceed 1000.
    The integers in the given array are in the range of [0, 1000].

"""
import bisect
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        2078ms
        """
        sum_1 = 0
        l = len(nums)
        nums = sorted(nums)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                k = nums[i] + nums[j]
                a = bisect.bisect_left(nums[j + 1 : ], k)
                sum_1 += a
                print(a, nums[i], nums[j], nums[j + 1 :])
        return sum_1

    def triangleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        315ms
        """
        sum_1 = 0
        l = len(nums)
        nums = sorted(nums)
        for j in range(1, l - 1):
            mark = j + 1
            for i in range(j):
                k = nums[i] + nums[j]
                while mark < l and nums[mark] < k:
                    mark += 1
                sum_1 += mark - j - 1
                print(i, j, k, mark, sum_1)

        return sum_1

    def triangleNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        285ms
        """
        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, -1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


print(Solution().triangleNumber_1([2, 3, 4, 5, 6]))
print(Solution().triangleNumber_1([2,2,3,4]))
