"""
 Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        272ms
        """
        nums.sort()
        l=(len(nums)+1)//2
        nums_copy=[0 for i in range(len(nums))]
        count=0
        for i in range(l):
            nums_copy[count]=nums[l-1-i]
            count+=1
            if count<len(nums):
              nums_copy[count]=nums[-(i+1)]
              count+=1
        nums[:]=nums_copy[:]

    def wiggleSort_1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        5689 ms
        """
        def find_middle(nums):
            def swap(nums,start,end):
                pos = start
                data = nums[pos]
                for i in range(start+1, end):
                    if nums[i] < data:
                        pos += 1
                        nums[pos], nums[i] = nums[i], nums[pos]
                nums[start], nums[pos] = nums[pos], nums[start]
                # print(start,end,nums)
                return pos
            start=0
            end=len(nums)-1
            mid=(start+end)//2
            while 1:
                pos=swap(nums,start,end+1)
                if pos==mid:
                    break
                elif pos>mid:
                    end=pos-1
                else:
                    start=pos+1
            print(nums)
            if len(nums)%2==0:
                return (nums[mid]+nums[mid+1])/2
            else:
                return nums[mid]
        median=find_middle(nums)

        def newIndex(i,n):
            return (1 + 2 * i) % (n | 1)
        i=0
        left=0
        l=len(nums)
        right=l-1
        while i <= right:
            if nums[newIndex(i, l)] > median:
                nums[newIndex(left,l)],nums[newIndex(i,l)]=nums[newIndex(i,l)],nums[newIndex(left,l)]
                left+=1
                i+=1
            elif nums[newIndex(i, l)] < median:
                nums[newIndex(right, l)], nums[newIndex(i, l)] = nums[newIndex(i, l)], nums[newIndex(right, l)]
                right-=1
            else:
                i+=1
        print(nums)


nums=[1, 5, 1, 1, 6, 4]
nums=[4,5,5,6,7]
nums=[6,13,5,4,5,2,5]
Solution().wiggleSort_1(nums)
# print(nums)
