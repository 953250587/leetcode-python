"""
 There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.

Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.

Note:

    n will be in the range [1, 4].
    k will be in the range [1, 10].
    k^n will be at most 4096.

"""
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        566ms
        """
        mark = [0] * (k ** n)
        def cal(s, k):
            ans = 0
            for i,char in enumerate(s[::-1]):
                ans += int(char) * (k ** i)
            return ans
        s = '0' * (n - 1)
        count = 0
        start_pos = 0
        while True:
            if count == len(mark):
                return s[start_pos:]
            flag = False
            for i in range(k):
                s_1 = s + str(i)
                pos = cal(s_1[-n:], k)
                if mark[pos] == 0:
                    count += 1
                    flag = True
                    mark[pos] = 1
                    break
            if flag:
                s = s_1
                continue
            else:
                for h in range(1, n):
                    pos = cal(s[start_pos + h:start_pos + h + n], k)
                    mark[pos] = 0
                    count -= 1
                start_pos += n
                s += s[start_pos - 1]
                continue

    def crackSafe_1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        86ms
        """
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n + 1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans


print(Solution().crackSafe(n = 2, k = 2))
print(Solution().crackSafe(n = 1, k = 2))
print(Solution().crackSafe(n = 4, k = 8))

# import collections
# so = Solution()
# for n in range(1, 5):
#     for k in range(1, 11):
#         if k ** n > 4096: continue
#         ans = so.crackSafe(n, k)
#         vset = set(ans[x : x + n] for x in range(len(ans) - n + 1))
#         print('k =', k, ' n =', n)
#         print(len(ans), len(vset), sorted(collections.Counter(ans).items()), '\n')