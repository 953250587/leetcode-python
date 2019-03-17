"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.


"""
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        55ms
        """
        if len(nums)<=0:
            return []
        if len(nums)==1:
            return [nums[0]]

        num_1=nums[0]
        count_1=0
        num_2=nums[0]
        count_2=0
        for num in nums:
            if num!=num_1:
                num_2=num
                break
        if num_1==num_2:
            return [nums[0]]
        # print(num_1,num_2)
        result=[]
        for num in nums:
            if count_1==0 and count_2!=0 and num!=num_2:
                num_1=num
            elif count_2==0 and count_1!=0 and num!=num_1:
                num_2=num
            elif count_1==0 and count_2==0:
                num_1=num
            if num!=num_1 and num!=num_2:
                count_1-=1
                count_2-=1
            elif num==num_1:
                count_1+=1
            elif num==num_2:
                count_2+=1
            print('num',num,'sdasd',count_1,count_2)
        if nums.count(num_1)>len(nums)//3 and count_1>0:
            result.append(num_1)
        if nums.count(num_2) > len(nums) // 3 and count_2>0:
            result.append(num_2)
        return result

    def majorityElement_1(self, nums):
        length = len(nums)
        counter = collections.Counter(nums)

        if length < 3:
            return counter.keys()

        result = []

        words = counter.most_common(3)

        for i in range(0, min(3, len(counter))):
            if words[i][-1] > length / 3:
                result.append(words[i][0])
        return result

print(Solution().majorityElement([-1,1,1,1,2,1]))
