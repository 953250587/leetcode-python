"""
We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.



Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.


Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9

"""


class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
         24 ms
        """
        import bisect
        l = len(str(N))
        l_D = len(D)
        D = list(map(int, D))
        ans = 0
        for i in range(1, l):
            ans += l_D ** i
        for i, a in enumerate(str(N)):
            print('star: ', ans, a, i)
            pos = bisect.bisect_left(D, int(a))
            if pos < len(D) and D[pos] == int(a):
                ans += pos * l_D ** (l - i - 1)
                if l - i - 1 == 0:
                    ans += 1
            else:
                ans += pos * l_D ** (l - i - 1)
                break
        return ans

    def atMostNGivenDigitSet_1(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        24ms
        """
        nums = [int(n) for n in str(N)]
        digits = {int(d) for d in D}
        dd = ([d for d in digits if d <= nums[i]] for i in range(len(nums)))
        ddl = [len(l) for l in dd]

        d_len = len(D)
        n_len = len(nums)
        if n_len == 1:
            return ddl[0]

        a1 = sum(d_len ** i for i in range(1, n_len))  # n-1 to 1
        if ddl[0] == 0:
            return a1

        an = 0
        for i, n in enumerate(nums):
            if i == n_len - 1:
                an += ddl[i]
                break
            if n in digits:
                an += max((ddl[i] - 1), 0) * d_len ** (n_len - 1 - i)
            else:
                an += ddl[i] * d_len ** (n_len - 1 - i)
                break
        return int(a1 + an)
# print(Solution().atMostNGivenDigitSet(D = ["1","3","5","7"], N = 100))
# print(Solution().atMostNGivenDigitSet(D = ["1","4","9"], N = 1000000000))
print(Solution().atMostNGivenDigitSet(D = ["1",'3',"4","9"], N = 319))
print(Solution().atMostNGivenDigitSet(["3","4","8"], 4))
