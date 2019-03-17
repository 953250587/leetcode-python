"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        46ms  空间不符合要求！！！
        """
        count_num=set()
        for i in nums:
            if i not in count_num:
                count_num.add(i)
            else:
                count_num.remove(i)
        return list(count_num)

    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        62ms  不同元素起码有一位是不一样的！！！
        """

        count_0_num=0
        count_1_num=0
        mark = -1
        for i in range(32):
            count_0 = 0
            count_1 = 0
            for num in nums:
                # print(num)
                num>>=i
                if bin(num)[-1]=='0':
                    count_0+=1
                else:
                    count_1+=1
            if count_0%2==1:
                mark=i
                break
        for num in nums:
            num_copy=num
            num >>= mark
            if bin(num)[-1] == '0':
                count_0_num ^=num_copy
            else:
                count_1_num ^= num_copy
        return [count_0_num,count_1_num]



# print(2^3^2)
print(Solution().singleNumber_1([1, 2, 1, 3, 2, 5]))