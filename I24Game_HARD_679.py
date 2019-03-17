"""
 You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: [1, 2, 1, 2]
Output: False

Note:

    The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

"""


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1282 ms
        """
        dicts = {}
        def dfs(Set):
            key = tuple(sorted(Set))
            if key in dicts:
                return dicts[key]
            lists = Set.copy()
            if len(lists) == 2:
                pro = set()
                a, b = str(lists[0]), str(lists[1])
                for symbol in '+-*':
                    pro.add(eval(a + symbol + b))
                    pro.add(eval(b + symbol + a))
                if lists[1] != 0:
                    pro.add(eval(a + '/' + b))
                if lists[0] != 0:
                    pro.add(eval(b + '/' + a))
                dicts[key] = pro
                return pro
            pro = set()
            for i in lists:
                Set.remove(i)
                new_set = Set.copy()
                new_list = dfs(new_set)
                Set.append(i)
                a = str(i)
                for pos in new_list:
                    b = str(pos)
                    for symbol in '+-*':
                        pro.add(eval(a + symbol + b))
                        pro.add(eval(a + symbol + b))
                    if pos != 0:
                        pro.add(eval(a + '/' + b))
                    if i != 0:
                        pro.add(eval(b + '/' + a))
            dicts[key] = pro
            return pro
        pro = dfs(nums)

        nums = sorted(nums)
        for i in range(3):
            for j in range(i + 1, 4):
                a = dicts[(nums[i], nums[j])]
                nums_c = nums.copy()
                nums_c.remove(nums[i])
                nums_c.remove(nums[j])
                b = dicts[tuple(nums_c)]

                for I in a:
                    # print(I)
                    if 24 + I in b:
                        return True
                    if 24 - I in b:
                        return True
                    if I != 0 and 24 * I in b:
                        return True
                    if  I != 0 and 24 / I in b:
                        return True

        for key in dicts:
            print(key, dicts[key])
        for i in pro:
            if abs(i - 24) < 0.00001:
                return True
        return False

    def judgePoint24_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hs = {}
        return self.helper(nums, hs)

    def helper(self, nums, hs):
        # print "debug", nums
        if len(nums) == 1:
            if 23.9 <= nums[0] <= 24.1:
                return True
            else:
                return False

        nums = sorted(nums)
        if "".join(str(nums) + ",") in hs:
            return False

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                if self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [a + b], hs) == True:
                    return True
                if self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [a * b], hs) == True:
                    return True
                if b != 0 and self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [float(a) / b], hs) == True:
                    return True
                if self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [a - b], hs) == True:
                    return True
                if a != 0 and self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [float(b) / a], hs) == True:
                    return True
                if self.helper(nums[:i] + nums[i + 1:j] + nums[j + 1:] + [b - a], hs) == True:
                    return True

        hs["".join(str(nums) + ",")] = True
        return False
# print(Solution().judgePoint24([4, 1, 8, 7]))
print(Solution().judgePoint24([1, 2, 1, 2]))
# print(Solution().judgePoint24([3, 3, 8, 8]))
# print(Solution().judgePoint24([1,3,2,6]))
print(Solution().judgePoint24([1,9,1,2]))