"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

"""

import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        1159ms
        """
        self.nums=nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums=self.nums[:]
        random.shuffle(nums)
        return nums



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()
nums = [1,2,3]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        715ms
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        lis = list(self.original)
        random.shuffle(lis)
        return lis