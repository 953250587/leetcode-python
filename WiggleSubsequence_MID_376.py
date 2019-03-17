"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        32ms
        """
        l = len(nums)
        if l<=1:
            return l
        temp=nums[0]
        self.mark=1
        count=1
        for i in nums[1:]:
            if i>temp:
                self.mark=1
                break
            elif i<temp:
                self.mark=-1
                break
            else:
                self.mark=0
            temp=i
            count+=1
        # print(self.mark,count)
        if self.mark==0:
            return 1
        self.num_count=2
        temp=nums[count]
        for i in range(count+1,l):
            a=(nums[i]-temp)*self.mark
            if a>0:
                temp=nums[i]
            elif a<0:
                # print(temp,nums[i],a)
                temp=nums[i]
                self.mark=-self.mark
                self.num_count+=1
        return self.num_count

    def wiggleMaxLength_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        29ms
        """
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < len(nums) and nums[i] == nums[0]:
            i += 1
        if i == len(nums):  # special case all numbers are same
            return 1
        result, last_num, want_large = 1, nums[0], nums[i] > nums[0]
        for j in range(i, len(nums)):
            if (nums[j] > last_num and want_large) or (nums[j] < last_num and not want_large):
                result += 1  # append nums[j] to subsequence
                want_large = not want_large  # flip
            last_num = nums[j]  # nums[j] is either appended to subsequence or replace subsequence[-1]

        return result
nums=[1,1,1,1,1]
nums=[1,7,4,9,2,5]
nums=[1,2,3,4,5,6,7,8,9]
nums=[1,17,5,10,13,15,10,5,16,8]
nums=[84]
print(Solution().wiggleMaxLength(nums))
