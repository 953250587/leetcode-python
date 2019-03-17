"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().



Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.


Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?

"""


# The rand7() API is already defined for you.
def rand7():
    import random
    return random.randint(1, 7)
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        340 ms
        """
        a = rand7()
        while a > 5:
            a = rand7()
        b = rand7()
        while b == 7:
            b = rand7()
        return a * 2 - b % 2

    def rand10_1(self):
        """
        :rtype: int
        332ms
        """
        x, y = rand7(), rand7()
        if x == 6 and y >= 6:
            return self.rand10()
        if x == 7:
            return self.rand10()
        return (x * 7 + y) % 10 + 1
for i in range(100):
    print(Solution().rand10())
