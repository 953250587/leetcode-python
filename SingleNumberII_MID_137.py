"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution(object):
    def singleNumber(self, nums):
        # return (3 * sum(set(nums)) - sum(nums)) / 2
        # 35ms
        """
        :type nums: List[int]
        :rtype: int
        232ms
        """
        count_0_z = 0
        count_1_z = 0
        count_0_f = 0
        count_1_f = 0
        for num in nums:
            if bin(num)[-1] == '0' and bin(num)[0] == '0':
                count_0_z += 1
            elif bin(num)[-1] == '0' and bin(num)[0] == '-':
                count_0_f += 1
            elif bin(num)[-1] == '1' and bin(num)[0] == '0':
                count_1_z += 1
            else:
                count_1_f += 1
        print(count_0_z, count_1_z, count_0_f, count_1_f)
        if count_0_z%3==1 or count_1_z%3==1:
            mark=1
        else:
            mark=-1
        result=0
        nums=[abs(i) for i in nums]
        for i in range(32):
            count_0 = 0
            count_1 = 0
            for num in nums:
                # print(num)
                num >>= i
                if bin(num)[-1] == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            if count_1 % 3 == 1:
                result+=2**i
        return mark*result
print(Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,4,-2]))
