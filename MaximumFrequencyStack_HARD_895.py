"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].


Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""

import collections
class FreqStack(object):

    def __init__(self):
        """
        292 ms
        """
        self.x2Num = collections.defaultdict(int)
        self.numList = collections.defaultdict(list)
        self.max = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.x2Num[x] += 1
        key = self.x2Num[x]
        self.numList[key].append(x)
        self.max = max(self.max, key)

    def pop(self):
        """
        :rtype: int
        """
        a = self.numList[self.max].pop()
        self.x2Num[a] -= 1
        if len(self.numList[self.max]) <= 0:
            self.max -= 1
        return a





        # Your FreqStack object will be instantiated and called as such:
        # obj = FreqStack()
        # obj.push(x)
        # param_2 = obj.pop()
obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
a = ["push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
b = [[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]

for i in range(len(a)):
    if a[i] == 'push':
        obj.push(b[i][0])
    else:
        print(obj.pop())