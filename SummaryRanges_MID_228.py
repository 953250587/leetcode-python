"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        35ms
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        temp=nums[0]
        result=[]
        str_start=str(temp)
        start=temp
        for i in nums[1:]:
            if i!=temp+1:
                if start!=temp:
                    str_end=str_start+'->'+str(temp)
                else:
                    str_end=str_start
                result.append(str_end)
                str_start=str(i)
                start=i
                temp=i
            else:
                temp+=1
        if start != temp:
            str_end = str_start + '->' + str(temp)
        else:
            str_end = str_start
        result.append(str_end)
        return result

    def summaryRanges_1(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
            print(ranges)
        return ['->'.join(map(str, r)) for r in ranges]
print(Solution().summaryRanges_1([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([0,3,5,7,9,11]))
