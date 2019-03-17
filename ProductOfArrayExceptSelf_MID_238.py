"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        149ms
        """
        product=1
        product_nozero = 1
        mark=0
        if len(nums)<=0:
            return []
        if len(nums)==1:
            return nums
        for num in nums:
            product*=num
            if num!=0:
                product_nozero*=num
            else:
                mark+=1
        result=[]
        if mark>=2:
            return [0 for i in range(len(nums))]
        for num in nums:
            if num!=0:
                result.append(product//num)
            else:
                result.append(product_nozero)
        return result
print(Solution().productExceptSelf([0,1,2,3,4,5]))