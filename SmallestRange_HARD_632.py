"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:

    The given list may contain duplicates, so ascending order means >= here.
    1 <= k <= 3500
    -105 <= value of elements <= 105.
    For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

"""


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        303ms
        """
        import bisect
        top = []
        l = len(nums)
        for i in range(l):
            bisect.insort(top, (-nums[i][0], i, 0))
        print(top)
        min_range = [float('inf'), [-1, -1]]
        while top:
            if len(top) == l:
                r_max = -top[0][0]
                r_min = -top[-1][0]
                r = r_max - r_min
                if r < min_range[0]:
                    min_range[0] = r
                    min_range[1] = [r_min, r_max]
            _, which, where = top.pop()
            if where + 1 < len(nums[which]):
                next_a = (-nums[which][where + 1], which, where + 1)
                bisect.insort(top, next_a)
            print(top, min_range)
        return min_range[-1]

    def smallestRange_1(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        101ms
        """
        k = len(nums)
        # 1. find each numer is in which window
        window_projection = {}
        for i in range(len(nums)):
            item = nums[i]
            for digit in item:
                if digit not in window_projection:
                    window_projection[digit] = []
                window_projection[digit].append(i)
        nums = sorted(window_projection.keys())
        # print(window_projection, nums)

        # 2. do a for loop to find the minSize
        # initiate
        minRange = [nums[0], nums[-1]]
        count = {}
        self.add_num(window_projection, nums[0], count)
        if len(set(window_projection[nums[0]])) == k:
            return [nums[0], nums[0]]

        # print(count)
        left = 0
        for i in range(1, len(nums)):
            # print(nums[i], count)
            self.add_num(window_projection, nums[i], count)
            while len(count) >= k:
                if (nums[i] - nums[left]) < minRange[-1] - minRange[0]:
                    minRange = [nums[left], nums[i]]
                self.delete_num(window_projection, nums[left], count)
                left += 1
        return minRange

    def delete_num(self, window_projection, number, count):
        # print('delete', number)
        for win in window_projection[number]:
            count[win] -= 1
            if count[win] == 0:
                del count[win]

    def add_num(self, window_projection, number, count):
        # print('add', number)
        for win in window_projection[number]:
            if win not in count:
                count[win] = 0
            count[win] += 1

print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))