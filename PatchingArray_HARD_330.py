"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        38ms
        """
        start = 0
        pos = 0
        ans = 0
        while start < n:
            if pos < len(nums) and nums[pos] <= start + 1:
                start += nums[pos]
                pos += 1
            else:
                start += 1
                start += start - 1
                ans += 1
        return ans

    def minPatches_1(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        45ms
        """
        miss, count, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                count += 1
        return count
print(Solution().minPatches(nums = [1, 3], n = 6))
print(Solution().minPatches(nums = [1, 5, 10], n = 20))
print(Solution().minPatches(nums = [1, 2, 2], n = 5))


