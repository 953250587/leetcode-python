"""
 Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

"""
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1139ms
        """
        if len(nums)<=2:
            return False
        temp=nums[0]
        count=0
        start=temp
        end=temp
        for i in nums:
            if i<=temp:
                temp=i
                count+=1
            else:
                start=temp
                break
        # if count==len(nums):
        #     return False
        for i in nums[count:]:
            if i>temp:
                temp=i
                count+=1
            else:
                end=temp
                break
        print(count,start,end)
        start_1=start
        end_1=end
        stack=[[start,end]]
        for i in nums[count:]:
            for j in stack:
                if i>j[0] and i<j[1]:
                    return True
            if start_1 >= i:
                start_1 = i
            if i > start_1:
                end_1 = i
                if stack[-1][0]>end_1:
                    stack.append([start_1, end_1])
                else:
                    while len(stack)>0:
                        a=stack.pop()
                        if a[1]>=end_1 or len(stack)==0:
                            stack.append([start_1, max(end_1,a[1])])
                            break
            print(i,stack)
        return False

    def find132pattern_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        69ms
        """
        n = len(nums)
        sta = []
        a2 = -2 ** 31
        for i in range(n - 1, -1, -1):
            if nums[i] < a2:
                return True
            if not sta or sta[-1] >= nums[i]:
                sta.append(nums[i])
            else:
                while sta and sta[-1] < nums[i]:
                    a2 = sta.pop()
                sta.append(nums[i])
        return False

    def find132pattern_2(self, nums):
        """
        66ms
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return False

        stack = [[nums[0], nums[0]]]
        minimum = nums[0]
        for num in nums[1:]:
            if num <= minimum:
                minimum = num
            else:
                while stack and num > stack[-1][0]:
                    if num < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([minimum, num])

        return False

    def find132pattern_4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        68ms
        """
        if len(nums)<=2:
            return False
        temp=nums[0]
        count=0
        start=temp
        end=temp
        for i in nums:
            if i<=temp:
                temp=i
                count+=1
            else:
                start=temp
                break
        # if count==len(nums):
        #     return False
        for i in nums[count:]:
            if i>temp:
                temp=i
                count+=1
            else:
                end=temp
                break
        stack=[[start,end]]
        minm=start
        for i in nums[count:]:
            if i<=minm:
                minm=i
            else:
                while stack and i > stack[-1][0]:
                    a = stack.pop()
                    if i < a[1]:
                        return True
                stack.append([minm, i])
            print(stack)
        return False


# nums=[0,0,-1,-2,-1,0,1,1,-3,-3,4,4,2]
# print(Solution().find132pattern(nums))
#
# nums=[0,1,2,3,4,5]
# print(Solution().find132pattern(nums))
#
# nums=[0,-1,-2,-3,-4,-5]
# print(Solution().find132pattern(nums))

nums=[8,10,4,6,1,11,3,5]
print(Solution().find132pattern_4(nums))

nums=[8,10,4,6,5]
print(Solution().find132pattern_4(nums))

nums=[3, 1, 4, 2]
print(Solution().find132pattern_4(nums))

nums=[2,3,1,2]
print(Solution().find132pattern_4(nums))