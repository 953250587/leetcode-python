"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        36ms
        """
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        s = str(n)
        l = len(s)
        nums = [0] * l
        nums[1] = 1
        for i in range(2, l):
            nums[i] = (10 ** (i - 1)) + 10 * nums[i - 1]
        print(nums)
        sum_1 = 0
        for i, char in enumerate(s):
            if int(char) == 0:
                continue
            if int(char) == 1:
                if s[i + 1:] != '':
                    sum_1 += int(s[i + 1:]) + 1
                else:
                    sum_1 += 1
                sum_1 += nums[-i - 1]
            else:
                sum_1 += nums[-i - 1] * int(char) + 10 ** ((l - 1 - i))
            print(sum_1)
        return sum_1


print(Solution().countDigitOne(1))
print(Solution().countDigitOne(10))
print(Solution().countDigitOne(13))
print(Solution().countDigitOne(111))


#case 1: n=3141092, a= 31410, b=92. 计算百位上1的个数应该为 3141 *100 次.
#case 2: n=3141192, a= 31411, b=92. 计算百位上1的个数应该为 3141 *100 + (92+1) 次.
#case 3: n=3141592, a= 31415, b=92. 计算百位上1的个数应该为 (3141+1) *100 次.
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        32ms
        """
        if n<=0:
            return 0
        if n==1:
            return 1
        m=1
        result=0
        while(m<=n):
            a=n/m
            b=n%m
            result+=(a+8)/10*m
            if a%10==1:
                result+=(b+1)
            m=m*10
        return result
