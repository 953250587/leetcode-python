"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans=str(numerator/denominator)
        if len(ans)<len(str(1/9)):
            return ans
        def find(ans):
            for i in range(len(ans) - 3):
                temp = ans[i:-1]
                for j in range(1, len(temp)):
                    if temp[:-j] == temp[j:]:
                        return i,j
            return 0,0
        i,j=find(ans[2:])
        if i==j==0:
            return ans
        else:
            return ans[:2+i]+'('+ans[2+i:2+i+j]+')'

    def fractionToDecimal_1(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        39ms
        找到重复出现的余数的时候就是开始重复的时候！！！！！！
        """

        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


print(str(1/17))
print(str(1/9))
print(Solution().fractionToDecimal_1(1,17))