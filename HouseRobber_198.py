"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        36ms
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        num_max=[0 for i in range(len(nums))]
        num_max[-1]=nums[-1]
        # num_max[-2]=nums[-2]
        l=len(nums)-1
        for i in range(1,l+1):
            if l-i+2<=l:
                a=num_max[l-i+2]
            else:
                a=0
            num_max[l-i]=max(num_max[l-i+1],a+nums[l-i])
        # print(num_max)
        return num_max[0]

print(Solution().rob([1,2]))