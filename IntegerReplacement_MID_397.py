"""
 Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        38ms
        """
        sum=0
        while n>1:
            if n%2==0:
                n//=2
            elif '0' not in bin(n)[2:]:
                if n==3:
                    n-=1
                else:
                    n+=1
            else:
                count_1=bin(n+1)[2:].count('1')
                count_1_ = bin(n - 1)[2:].count('1')
                if count_1<=count_1_:
                    n+=1
                else:
                    n-=1
            sum+=1
        return sum

    def integerReplacement_1(self, n):
        """
        35ms
        :param n:
        :return:
        """
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn

print(bin(100000000))
print(Solution().integerReplacement(100000000))
print(Solution().integerReplacement(7))
