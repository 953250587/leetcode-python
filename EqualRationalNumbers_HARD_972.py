# -*- coding: UTF-8 -*-
"""
Given two strings S and T, each of which represents a non-negative rational number, return True if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.
In general a rational number can be represented using up to three parts: an integer part, a non-repeating part, and a repeating part. The number will be represented in one of the following three ways:
<IntegerPart> (e.g. 0, 12, 123)
<IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:
1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

Example 1:
Input: S = "0.(52)", T = "0.5(25)"
Output: true
Explanation:
Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
Example 2:
Input: S = "0.1666(6)", T = "0.166(66)"
Output: true
Example 3:
Input: S = "0.9(9)", T = "1."
Output: true
Explanation:
"0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

Note:
Each part consists only of digits.
The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
1 <= <IntegerPart>.length <= 4
0 <= <NonRepeatingPart>.length <= 4
1 <= <RepeatingPart>.length <= 4
"""


class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        36 ms
        13.2 MB
        """
        """
        错了3次,第一次没有考虑到只有整数部分的情况...说实话有想过...不过感觉不会有就没写
        第二次错在把循环和非循环搞混了...
        第三次错在把9,99,999,9999这种认为是(x + 1) % 10 == 0就可以了...
        这题还是可以的
        """
        # 解析字符串,分解为3个部分
        def _parser(inputs):
            temp = inputs.split('.')
            IntegerPart = int(temp[0])
            # 如果只有整数部分
            if len(temp) <= 1:
                return [IntegerPart, '0', '0']
            temp = temp[1].split('(')
            NonRepeatingPart = temp[0]
            # 如果没有无限循环部分
            if len(temp) > 1:
                RepeatingPart = temp[1][:-1]
            else:
                RepeatingPart = '0'
            return [IntegerPart, NonRepeatingPart, RepeatingPart]

        # 用于处理0.?*9999这样的情况
        def _solve(NonRepeatingPart, RepeatingPart):
            # 先对非重复部分进行处理,如果为空则置为'0'
            temp = int(NonRepeatingPart if NonRepeatingPart != '' else '0')
            # 如果末尾不存在无限循环数,或者为0的时候
            if int(RepeatingPart) == 0:
                # 我们只需要计算非循环的部分,强制转化为float型
                return float(temp) * (10 ** -len(NonRepeatingPart))
            # 如果末尾无限循环为9,99,999这样的时候,进一位,强制转化为float型
            if RepeatingPart in ['9', '99', '999', '9999', '99999']:
                return (float(temp) + 1) * (10 ** -len(NonRepeatingPart))
            # 否则则用非重复部分+重复部分*8,取8是因为非重复和重复部分不会超过4,8则能保证范围足够
            return NonRepeatingPart + RepeatingPart * 8

        s = _parser(S)
        # print(s)
        t = _parser(T)
        # print(t)
        need_len = max(len(s[1]) + len(s[-1]), len(t[1]) + len(t[-1]))
        s_point = _solve(s[1], s[-1])
        t_point = _solve(t[1], t[-1])
        # print(s_point, t_point)
        # 如果两者都为float型,则可以+整数部分比较大小
        if isinstance(s_point, float) and isinstance(t_point, float):
            return s[0] + s_point == t[0] + t_point
        # 如果两者都是str,则整数和小数部分分别比较,小数部分只需要取到两个小数较长的那个数的范围即可
        elif isinstance(s_point, str) and isinstance(t_point, str):
            return s[0] == t[0] and s_point[:need_len] == t_point[:need_len]
        else:
            return False

    def isRationalEqual_1(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        20 ms
        11.8 MB  100% what fuck
        """
        """
        可以...实际上就是我的第3种情况扩展,然后用python的float自动判断!!!!
        """
        def f(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])

        return f(S) == f(T)


if __name__ == '__main__':
    print(Solution().isRationalEqual(S="0.(52)", T="0.5(25)"))
    print(Solution().isRationalEqual(S="0.1666(6)", T="0.166(66)"))
    print(Solution().isRationalEqual(S="0.9(9)", T="1."))
    print(Solution().isRationalEqual(S="0.9(9)", T="1.0(0)"))
    print(Solution().isRationalEqual(S="0.9(3)", T="0.93"))
    print(Solution().isRationalEqual(S="1", T="1.03(4)"))
    print(Solution().isRationalEqual('15.(9)', '16'))
    print(Solution().isRationalEqual("519.519(519)", "519.(519)"))