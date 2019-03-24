# -*- coding: UTF-8 -*-
"""
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.

Example 1:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Note:
1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        32 ms
        11.7 MB
        """
        cur_x = 1
        # 去除重复的数字
        ans_list = set()
        # 保证x ** i的数值比bound小
        while cur_x <= bound:
            # 每确定一个x**i,则寻找可行的y**j
            cur_y = 1
            temp = cur_x + cur_y
            while temp <= bound:
                ans_list.add(temp)
                cur_y *= y
                temp = cur_x + cur_y
                # 如果y=1,则可以跳出循环
                if cur_y == 1:
                    break
            cur_x *= x
            # 如果x=1,则可以跳出循环
            if cur_x == 1:
                break
        return list(ans_list)

    def powerfulIntegers_1(self, x, y, bound):
        """
        24 ms
        12 MB
        :param x:
        :param y:
        :param bound:
        :return:
        """
        xs = {x ** i for i in range(20) if x ** i < bound}
        ys = {y ** i for i in range(20) if y ** i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})

if __name__ == '__main__':
    print(Solution().powerfulIntegers(1, 1, 1))
    print(Solution().powerfulIntegers(1, 1, 4))
    print(Solution().powerfulIntegers(1, 4, 9))
    print(Solution().powerfulIntegers(2, 1, 10))
    print(Solution().powerfulIntegers(x = 2, y = 3, bound = 10))
    print(Solution().powerfulIntegers(x = 3, y = 5, bound = 15))


