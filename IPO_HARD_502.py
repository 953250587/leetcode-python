"""
 Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:

Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Note:

    You may assume all numbers in the input are non-negative integers.
    The length of Profits array and Capital array will not exceed 50,000.
    The answer is guaranteed to fit in a 32-bit signed integer.

"""
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        160ms
        """
        import bisect
        a = zip(Capital, Profits)
        message = sorted([i for i in a], key=lambda a:a[0])
        index = sorted(Capital)
        # print(index, message)
        # pos = bisect.bisect_right(index, 2)
        # print(pos)
        start = 0
        all_profit = []
        while k > 0:
            pos = bisect.bisect_right(index, W)
            for i in range(start, pos):
                bisect.insort(all_profit, message[i][1])
            start = pos
            print(all_profit, start)
            if all_profit:
                W += all_profit.pop()
            k -= 1
        return W

    def findMaximizedCapital_1(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        110ms
        """
        Projects = sorted(zip(Profits, Capital), key=lambda x: x[0])
        num_of_project = 0
        while num_of_project < k:
            for i in range(len(Projects) - 1, -1, -1):
                if Projects[i][1] <= W:
                    W += Projects[i][0]
                    Projects.pop(i)
                    break
            num_of_project += 1
        return W

print(Solution().findMaximizedCapital(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1]))
print(Solution().findMaximizedCapital(1,0,[1,2,3],[1,1,2]))