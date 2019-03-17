"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        65MS
        """
        if num==1:
            return False
        cell=num//2
        k=2
        sum=1
        while k<cell:
           high=num//k
           cell=high+1
           if num%k==0:
               sum+=(high+k)
           k+=1
        return sum==num

    def checkPerfectNumber_1(self, num):
        """
        :type num: int
        :rtype: bool
        36MS
        """
        res = 0
        base = 1
        if num <= 0: return False
        if num % 10 == 6 or num % 10 == 8:
            if num == 6:
                return True
            while (res < num):
                res = res + pow(base, 3)
                base = base + 2

        return res == num
print(Solution().checkPerfectNumber(1))
