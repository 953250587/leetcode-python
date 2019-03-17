"""
 Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        276ms
        """
        if nums == []:
            return []
        m = max(nums)
        l =len(nums)
        a = nums.index(m)
        c = nums[a:] + nums[0:a]
        # print(c, a)
        stack = []
        result = [m] * len(nums)
        count = 0
        for i in c:
            while len(stack) > 0 and stack[-1][0] < i:
                d = stack.pop()
                result[d[1]] = i
            d = (count + a) % l
            if i == m:
                result[d] = -1
            else:
                stack.append((i, d))
            count += 1
        return result

    def nextGreaterElements_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        第一次只找之后的，第二次找之前的
        255ms
        """
        res, n, s = [-1] * len(nums), len(nums), []
        for i, num in enumerate(nums):
            while s and nums[s[-1]] < num:
                res[s.pop()] = num
            s.append(i)

        for i, num in enumerate(nums):
            while len(s) > 1 and nums[s[-1]] < num:
                res[s.pop()] = num
        return res
print(Solution().nextGreaterElements([1, 2, 1]))
print(Solution().nextGreaterElements([2, 2, 2, 2, 2]))
print(Solution().nextGreaterElements([2, 3, 4, 4, 4, 2, 4, 4, 1]))
print(Solution().nextGreaterElements([4, 3, 2, 1]))
print(Solution().nextGreaterElements([2]))
print(Solution().nextGreaterElements([]))