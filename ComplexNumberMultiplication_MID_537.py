"""
 Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:

Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

    The input strings will not have extra blank.
    The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

"""
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        36ms
        """
        A = a.split('+')
        B = b.split('+')
        A[-1] = A[-1][0:-1]
        B[-1] = B[-1][0:-1]

        first = int(A[0]) * int(B[0])
        second = -int(A[-1]) * int(B[-1])

        thrid= int(A[0]) * int(B[-1]) + int(A[-1]) * int(B[0])

        a = first + second
        b = str(thrid) + 'i'

        return str(a) + '+' + b

    def complexNumberMultiply_1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        33ms
        """

        def parse(s):
            array = s.split('+')
            real = int(array[0])
            imag = int(array[1][:-1])
            return real, imag

        ar, ai = parse(a)
        br, bi = parse(b)
        ans_real = ar * br - ai * bi
        ans_imag = ar * bi + ai * br
        return '%d+%di' % (ans_real, ans_imag)
a = "1+1i"
b = "1+1i"
print(Solution().complexNumberMultiply(a, b))

a = "1+-1i"
b = "1+-1i"
print(Solution().complexNumberMultiply(a, b))

a = "0+-0i"
b = "1+0i"
print(Solution().complexNumberMultiply(a, b))