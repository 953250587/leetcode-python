"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        35ms
        """
        if nums == []:
            return []
        if len(nums) <=3:
            return max(nums)
        def rob_1(nums):
            if nums == []:
                return []
            if len(nums) == 1:
                return nums
            num_max = [0 for i in range(len(nums))]
            num_max[0] = nums[0]
            l = len(nums)
            for i in range(1, l - 1):
                if i >= 2:
                    num_max[i] = max(num_max[i - 1], num_max[i - 2] + nums[i])
                else:
                    num_max[i] = max(num_max[i - 1], nums[i])

            a = num_max[l - 3] + nums[l - 1]
            num_max[l - 1] = max(num_max[l - 2], a)
            # print(num_max)
            return num_max

        num_1_max=rob_1(nums[:-2])
        num_2_max = rob_1(nums[1:-2])
        num_3_max=rob_1(nums[0:-1])
        if num_2_max ==[]:
            a = max(num_1_max[-1], nums[-1])
            return max(a, num_3_max[-1])
        if num_1_max[-1]==num_2_max[-1]:
            return max(num_3_max[-1],num_2_max[-1]+nums[-1])
        else:
            a=max(num_1_max[-1],num_2_max[-1]+nums[-1])
            return max(a,num_3_max[-1])

    def rob_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        33ms
        """
        n = len(nums)
        if n == 0: return 0
        if n < 4: return max(nums)

        first, second = 0, 0
        for i in nums[:-1]: first, second = second, max(first + i, second)
        result = second

        first, second = 0, 0
        for i in nums[1:]: first, second = second, max(first + i, second)
        return max(result, second)


print(Solution().rob([0,0]))
# a=[1,2,3]
# print(a[:-2])