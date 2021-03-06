"""
 There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        96ms
        """
        start=1
        count=1
        end=n
        while start<end:
            if count%2==1:
                start+=pow(2,count-1)
                k=(end-start)//(2**count)
                end=start+2**count*k
            else:
                end-=2**(count-1)
                k = (end - start) // (2 ** count)
                start=end-2**count*k
            count+=1
            # print(start,end)
        return start

    def lastRemaining_1(self, n):
        """
        :type n: int
        :rtype: int
        78ms
        """
        if n == 3 or n == 2:
            return 2
        elif n == 1:
            return 1
        else:
            base = 4 * self.lastRemaining_1(n // 4)
            if n % 4 == 0 or n % 4 == 1:
                return base - 2
            else:
                return base
print(Solution().lastRemaining(2))