"""
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).  For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before addition and subtraction.
It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target.  Return the least number of operators used.



Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.


Note:

2 <= x <= 100
1 <= target <= 2 * 10^8
"""


class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        20 ms,
        11.7 MB
        """
        pos = neg = k = 0
        while target:
            target, leave = divmod(target, x)
            # 只需要考虑 +leave 的情况，之后把+leave用x-（x - leave）替换就与-x+leave本质上是一样的
            # 之后我们假设每一层都是target=（targeti * x + leavei） * x + leave的结构
            # leave可以直接使用leave * （x/x）或者x - （x - leave）* （x/x）
            # 前者需要 2 * leave个符号，后者需要（x-leave）* 2 个符号,把多余的x进位到上一层
            if k == 0:
                # 最后一层只考虑leave就可以
                pos, neg = 2 * leave, (x - leave) * 2
            else:
                # 其它层需要结合上一层的情况和当前层的leave
                # 不往上一层进位，前一个不接受下层给他的进位，后一个接受，k表示这层需要*几次x
                # 往上一层进位，前一个没有接收下层对它的进位，所以保持不变，后者进位抵消一个，所以少1
                pos, neg = min(pos + leave * k, neg + (leave + 1) * k), min(pos + (x - leave) * k, neg + (x - leave - 1) * k)
            k += 1
        # k 为进位后需要连成k次的结果
        return min(pos, neg + k) - 1

    def leastOpsExpressTarget_1(self, x, y):
        pos = neg = k = 0
        while y:
            y, cur = divmod(y, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos, neg = cur * 2, (x - cur) * 2
            k += 1
        return min(pos, k + neg) - 1


if __name__ == '__main__':
    print(Solution().leastOpsExpressTarget(3, 2))
    print(Solution().leastOpsExpressTarget(3, 19))
    print(Solution().leastOpsExpressTarget(5, 501))
    # print(Solution().leastOpsExpressTarget_1(5, 501))
    print(Solution().leastOpsExpressTarget(100, 100000000))
    print(Solution().leastOpsExpressTarget(2, 125046))


