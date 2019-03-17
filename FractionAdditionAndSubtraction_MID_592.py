"""
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input:"-1/2+1/2"
Output: "0/1"

Example 2:

Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input:"1/3-1/2"
Output: "-1/6"

Example 4:

Input:"5/3+1/3"
Output: "2/1"

Note:

    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1,10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

"""
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        45ms
        """
        if expression == '':
            return ''
        stack = []
        val = ''
        if expression[0] != '-':
            expression = '+' + expression
        start = 0
        while start < len(expression):
            start += 1
            mark = start
            while start < len(expression) and expression[start] != '-' and expression[start] != '+':
                start += 1
            a = 1
            if expression[mark - 1] == '-':
                a = -1
            stack.append([expression[mark:start].split('/'), a])
        print(stack)

        d = 9 * 8 * 7 * 5
        z = 0
        for i in stack:
            z += d // int(i[0][1]) * int(i[0][0]) * i[1]
        mark = 1
        if z < 0:
            mark = -1
        ints = abs(z) // d
        leave_z = abs(z) % d

        def gcd(d, leave_z):
            a = d % leave_z
            if a == 0:
                return leave_z
            else:
                return gcd(leave_z, a)
        if leave_z != 0:
            a = gcd(d, leave_z)
            ff = d // a
            c = leave_z // a
        else:
            ff = 1
            c = leave_z
        fz = (ints * ff + c) * mark
        return str(fz) + '/' + str(ff)

    def fractionAddition_1(self, expression):
        """
        35ms
        :param expression:
        :return:
        """
        def gcd(a, b):
            if a < b: a, b = b, a
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b / gcd(a, b)

        part = ''
        fractions = []
        for c in expression:
            if c in '+-':
                if part: fractions.append(part)
                part = ''
            part += c
        if part: fractions.append(part)
        hi = [int(e.split('/')[0]) for e in fractions]
        lo = [int(e.split('/')[1]) for e in fractions]
        LO = reduce(lcm, lo)
        HI = sum(h * LO / l for h, l in zip(hi, lo))
        GCD = abs(gcd(LO, HI))
        return '%s/%s' % (HI / GCD, LO / GCD)

print(Solution().fractionAddition("-1/2+1/2+1/3"))
print(Solution().fractionAddition("1/3-1/2"))
print(Solution().fractionAddition("-1/2+1/2"))
print(Solution().fractionAddition("5/3+1/3"))
print(Solution().fractionAddition(""))