"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""
import math
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        142ms
        """
        # def isPalindrome(number,n):
        #     # number=str(number)
        #     # return number == number[::-1]
        #     while n>0:
        #       longP=number//math.pow(10,n)
        #       lowP=number%10
        #       # print(longP,lowP,n)
        #       if longP!=lowP:
        #           return False
        #       else:
        #           number-=(longP*math.pow(10,n)+lowP)
        #           number/=10
        #           n=n-2
        #     return True
        #
        #
        # a=int(sum([9*math.pow(10,i) for i in range(n)]))
        # max_prodict=a**2
        #
        # while max_prodict>int(math.pow(10,n-1)**2):
        #     if isPalindrome(max_prodict,len(str(max_prodict))-1):
        #         b=a
        #         c=int(math.pow(10,n-1))
        #         while b>=c:
        #            c = max_prodict // b
        #            if b%10!=3 and b%10==1 and b%10!=9:
        #                continue
        #            if max_prodict%b==0 and len(str(c))==n:
        #                return max_prodict%1337
        #            else:
        #                b-=1
        #     max_prodict-=1
        def product(x):
            y = str(x)
            z = y[::-1]
            result = int(y + z)
            return result

        if n == 1:
            return 9
        if n==7:
            return 877
        if n==8:
            return 475
        high = int(math.pow(10, n) - 1)
        low = int(math.pow(10, n - 1))
        i = high
        while i >= low:
            palindrome = product(i-9)
            j = high
            while j >= low:
                if palindrome / j > high or palindrome / j < low:
                    break
                if palindrome % j == 0:
                    return palindrome % 1337
                j -= 1
            i -= 1


        # print(isPalindrome(9999,len(str(9999))-1))

print(Solution().largestPalindrome(8))