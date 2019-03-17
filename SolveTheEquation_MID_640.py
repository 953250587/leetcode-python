"""
 Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: "x=x"
Output: "Infinite solutions"

Example 3:

Input: "2x=x"
Output: "x=0"

Example 4:

Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:

Input: "x=x+2"
Output: "No solution"

"""
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        45ms
        """
        e_all = equation.split('=')

        def get_info(e):
            result = []
            start = 0
            end = start
            while start < len(e):
                if e[start] in '+-':
                    t = e[end: start]
                    if len(t) > 0:
                         result.append(t)
                    end = start
                start += 1
            result.append(e[end: start])
            return result

        def calc(e):
            if e[0] not in '+-':
                e = '+' + e
            ones = get_info(e)
            print(ones)
            num_x_left = 0
            num_left = 0
            s = 1
            for one in ones:
                if len(one) == 1:
                    if one == '-':
                        s *= -1
                    else:
                        s *= 1
                elif 'x' in one:
                    c = one.split('x')[0]
                    if len(c) == 1:
                        c += '1'
                    num_x_left += s * int(c)
                    s = 1
                else:
                    num_left += s * int(one)
                    s = 1
            print(num_x_left, num_left)
            return num_left, num_x_left

        num_left, num_x_left = calc(e_all[0])
        num_right, num_x_right = calc(e_all[1])

        a = num_left - num_right
        b = num_x_right - num_x_left

        if b == 0 and a == 0:
            return "Infinite solutions"
        if b == 0 and a != 0:
            return "No solution"
        return "x=" + str(a//b)

    def solveEquation_1(self, equation):
        """
        :type equation: str
        :rtype: str
        36ms
        """
        lst = equation.split('=')
        a = [0, 0]
        b = [0, 0]
        for i in range(2):
            a[i], b[i] = self.solve(lst[i])
        if a[0] == a[1]:
            if b[0] != b[1]:
                return 'No solution'
            else:
                return 'Infinite solutions'
        else:
            return 'x=' + str((b[1] - b[0]) / (a[0] - a[1]))

    def solve(self, s):
        i, n, sign = 0, len(s), 1
        a, b = 0, 0
        num = 0
        while i < n:
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                num = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                if i + 1 == len(s):
                    b += num * sign
                elif s[i + 1] == '+' or s[i + 1] == '-':
                    b += num * sign
                elif s[i + 1] == 'x':
                    a += num * sign
                    i += 1
            else:
                a += 1 * sign
            i += 1
        return (a, b)



print(Solution().solveEquation("2x--5-3-+3x=6+x-2"))
print(Solution().solveEquation("x+5-3+x=6+x-2"))
print(Solution().solveEquation("x=x"))
print(Solution().solveEquation("2x=x"))
print(Solution().solveEquation("2x+3x-6x=x+2"))
print(Solution().solveEquation("x=x+2"))