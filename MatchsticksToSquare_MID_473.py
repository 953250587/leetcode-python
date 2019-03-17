"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:

    The length sum of the given matchsticks is in the range of 0 to 10^9.
    The length of the given matchstick array will not exceed 15.


"""
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        52ms
        """
        if nums==[]:
            return False
        a=sum(nums)
        if a%4!=0:
            return False
        b=a//4
        if max(nums)>b:
            return False
        nums=sorted(nums,reverse=True)
        self.nums=nums
        self.result=[]
        def dfs(start,total):
            if total<self.nums[-1]:
                return False
            for i in self.nums[start:]:
                start+=1
                self.result.append(i)
                if total==i:
                    return True
                else:
                    if dfs(start,total-i):
                        return True
                self.result.pop()
            return False
        for i in range(4):
            print(i)
            print(self.nums)
            if dfs(0,b):
                print(self.result)
                while self.result:
                    self.nums.remove(self.result.pop())
            else:
                return False
        return True
        # print(self.result)

    def makesquare_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        52ms
        """
        # index,start,
        nums.sort()
        nums = nums[::-1]
        index = [0] * len(nums)

        # print nums
        #
        def formValue(start, target):
            if target == 0:
                return True
            if target < 0:
                return False

            for i in range(start, len(nums)):
                if index[i] == 0 and nums[i] <= target:
                    # print "start:{}".format(start)
                    r = formValue(i + 1, target - nums[i])
                    if r:
                        index[i] = 1
                        return True
            return False

        num_sum = sum(nums)
        if num_sum % 4 != 0 or len(nums) < 4:
            return False
        target = num_sum / 4
        # print target
        for i in range(4):
            r = formValue(0, target)
            if not r:
                return False
        return True
print(Solution().makesquare([10,6,5,5,5,3,3,3,2,2,2,2]))