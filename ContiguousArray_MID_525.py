"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1862ms
        """
        if sum(nums)==len(nums)//2 and len(nums)%2==0:
            return len(nums)
        self.dicts={}
        sum_1=0
        count=1
        self.dicts[0]=[0,-1]
        for i in nums:
            if i==0:
                sum_1-=1
            else:
                sum_1+=1
            if sum_1 not in self.dicts.keys():
                self.dicts[sum_1]=[count,-1]
            else:
                self.dicts[sum_1][-1]=count
            count+=1
        print(self.dicts)
        max_1=0
        for i in self.dicts.keys():
            a=self.dicts[i]
            max_1=max(a[1]-a[0],max_1)
        return max_1

    def findMaxLength_1(self, nums):
        """
        315ms
        :param nums:
        :return:
        """
        count = 0
        max_length = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length

    def findMaxLength_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        242ms
        """
        lst = {0: -1}
        counter = 0
        cm = 0
        for i in range(len(nums)):
            counter += (nums[i] * 2 - 1)
            if counter in lst:
                a = i - lst[counter]
                if a > cm:
                    cm = a
            else:
                lst[counter] = i
        return cm



nums=[0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0]
print(Solution().findMaxLength(nums))

nums=[0,1,0]
print(Solution().findMaxLength(nums))

nums=[0,1]
print(Solution().findMaxLength(nums))

nums=[0,1,1,0,1,1,1,0]
print(Solution().findMaxLength(nums))

nums=[0,0,1,0,0,0,1,1]
print(Solution().findMaxLength(nums))

nums=[]
print(Solution().findMaxLength(nums))
