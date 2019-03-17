"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""


class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
         467 ms
        """
        def isSame(S, start, s):
            for i, char in enumerate(s):
                if char != S[i + start]:
                    # print(char, i + start, S[i + start])
                    return False
            return True

        for e in range(len(S) - 1, 1, -1):
            l = len(S) - e
            # print(S[0:e])
            for i in range(e - 1, 0, -1):
                start = e
                lists = []
                if (S[i] != '0' or e - i == 1) and (S[0] != '0' or i == 1) and max(i, e - i) <= l:
                    lists.append(int(S[0:i]))
                    lists.append(int(S[i:e]))
                    c = str(lists[-1] + lists[-2])
                    flag = True
                    # print(e,i,l,lists,start,c,len(S),start + len(c))
                    while start + len(c) <= len(S):
                        if not isSame(S, start, c):
                            flag = False
                            break
                        else:
                            start += len(c)
                            c = int(c)
                            if c >= 2**31 - 1:
                                flag = False
                                break
                            lists.append(c)
                            c = str(lists[-1] + lists[-2])
                        # print('s', start)

                    if flag and start == len(S):
                        return lists
                else:
                    continue
        return []

    def splitIntoFibonacci_1(self, S):
        """
        :type S: str
        :rtype: List[int]
        615MS
        """
        limit = 2 ** 31 - 1
        for i in range(1, len(S)):
            if S[0] == "0" and i != 1:
                break
            for j in range(i + 1, len(S)):
                if S[i] == "0" and j != i + 1:
                    break
                pre = int(S[:i])
                cur = int(S[i:j])
                ans = [pre, cur]
                k = j
                while k < len(S):
                    cur, pre = pre + cur, cur
                    if cur <= limit and str(cur) == S[k:k + len(str(cur))]:
                        ans.append(cur)
                        k = k + len(str(cur))
                    else:
                        break
                if k == len(S):
                    return ans
        return []

# print(Solution().splitIntoFibonacci("123456579"))
# print(Solution().splitIntoFibonacci("11235813"))
# print(Solution().splitIntoFibonacci("112358130"))
# print(Solution().splitIntoFibonacci("0123"))
# print(Solution().splitIntoFibonacci("1101111"))
# print(Solution().splitIntoFibonacci("1011"))
# print(Solution().splitIntoFibonacci("000000000"))
print(Solution().splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))




a = [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
c = [str(i) for i in a]
s = ''.join(c)
print(s == "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")
for i in range(len(a)-2):
    if a[i] + a[i + 1] != a[i + 2]:
        print(i)

print(3163294909 <= 2**31-1)

# [36115,3738,39853,43591,83444,127035,210479,337514,547993,885507,1433500,2319007,3752507,6071514,9824021,15895535,25719556,41615091,67334647,108949738,176284385,285234123,461518508,746752631,1208271139,1955023770,3163294909]