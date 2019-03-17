"""
 You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        205ms
        """
        nums_set = set(nums)
        a = sorted(nums_set)
        l = len(a) + 1
        print(a)
        dicts = {}
        for i,val in enumerate(a):
            dicts[val] = i + 1
        print(dicts)
        lists = [0] * l
        def lowbit(x):
            return x & -x
        def add(x, num):
            while x < l:
                lists[x] += num
                x += lowbit(x)

        def get_sum(x):
            sum = 0
            while x > 0:
                sum += lists[x]
                x -= lowbit(x)
            return sum
        for num in nums:
            add(dicts[num], 1)
        result = []
        for num in nums:
            result.append(get_sum(dicts[num] - 1))
            add(dicts[num], -1)
        print(lists)
        return result


import bisect


class Solution_1(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        208ms
        """
        visited = []
        result = []
        for i in range(0, len(nums)):
            curr = nums[len(nums) - i - 1]
            #  print(visited)
            count = bisect.bisect(visited, curr)
            while count > 0 and visited[count - 1] == curr:
                count = count - 1
            bisect.insort(visited, curr)
            result.append(count)

        result.reverse()
        return result

    def countSmaller_1(self, nums):
        """
        165ms
        :param nums:
        :return:
        """
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res.append(getSum(rank[x] - 1))
            update(rank[x])
        return res[::-1]

print(Solution().countSmaller([5, 2, 6, 1]))