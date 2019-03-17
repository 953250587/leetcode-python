"""
 Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        186MS
        """
        import bisect
        range_sum = []
        s = 0
        for num in nums:
            s += num
            range_sum.append(s)
        ans = 0
        bi = []
        for i in range_sum:
            if i <= upper and i >= lower:
                ans += 1
            r = bisect.bisect_right(bi, i - lower)
            l = bisect.bisect_left(bi, i - upper)
            print(i, r, l, bi, ans)
            ans += r - l
            bisect.insort(bi, i)
        return ans
print(Solution().countRangeSum(nums = [-2, 5, -1], lower = -2, upper = 2))
print(Solution().countRangeSum(nums = [-2,2,-2], lower = -2, upper = 2))
# import bisect
# print(bisect.bisect_left([1,1,3,4,5,5,6], 0))
# print(bisect.bisect_right([1,1,3,4,5,5,6], 6))


