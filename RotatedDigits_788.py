"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:

    N  will be in range [1, 10000].


"""
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        112ms
        """
        count = 0
        for i in range(1, N + 1):
            s = str(i)
            num = 0
            for char in s:
                if char in '347':
                    num = -1
                    break
                elif char in '018':
                    num += 1
            # 判断是否有效，和是否相同
            if num != len(s) and num != -1:
                count += 1
        return count

    def rotatedDigits_1(self, N):
        """
        :type N: int
        :rtype: int
        31ms
        """
        # 一位数有2，5，6，9满足条件
        start = 4
        # 记录0位，1位满足题意的good数的个数
        list_start = [0, start]
        s = str(N)
        l = len(s) - 1
        # 扩展为2位到l位
        for i in range(1, l):
            # n位可以由（n-1位 + [0,1,2,5,6,8,9] + 以[2,5,6,9]开头的个数 * 剩下位数为[0，1，8]的随即排列）
            start = 7 * start + 4 * (3 ** i)
            list_start.append(start)
        count = 0
        # 每一位考虑过去，例如234，我们就先考虑0-99，100-199，200-209，210-219，220-229，230-234这样
        for i, char in enumerate(s):
            m = int(char)
            # 比当前位置小的全部数逐个累加，
            for j in range(m):
                # 如果是[0, 1, 8]，剩下位数自身一定要为good数，用前面记录的代入
                if j in [0, 1, 8]:
                    count += list_start[l - i]
                # 如果是[2, 5, 6, 9]，则除了剩下位数自身为good数，或则由[0，1，8]的随即排列
                elif j in [2, 5, 6, 9]:
                    count += list_start[l - i] + (3 ** (l - i))
            # 如果当前位置不能翻转，说明最大到此为止，结束
            if m in [3, 4, 7]:
                return count
            # 如果当前位置为[2, 5, 6, 9]，则我们考虑剩下位置由[0, 1, 8]组成且不大于N的个数
            elif m in [2, 5, 6, 9]:
                mark = True
                # 还是逐位考虑
                for next_i in range(i + 1, len(s)):
                    cur = int(s[next_i])
                    for k in [0, 1, 8]:
                        # 比[0, 1, 8]小说明该位可以为[0, 1, 8]，之后位可以由[0, 1, 8]随意组合，也不会大于目标值
                        if k < cur:
                            count += 3 ** (l - next_i)
                    # 如果当前位置不为[0, 1, 8]，说明所有小于目标的组合已经都完成了
                    if cur not in [0, 1, 8]:
                        mark = False
                        break
                # 如果末尾为[0, 1, 8]，我们需要+1
                if mark and (s[-1] in ['0', '1', '8']):
                    count += 1
        # 如果末尾为[2, 5, 6，9]，我们需要+1
        if s[-1] in ['2', '5', '6', '9']:
            count += 1
        return count

    def rotatedDigits_2(self, N):
        """
        32ms
        :param N:
        :return:
        """
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = map(int, str(N))
        print(N)
        for i, v in enumerate(N):
            print(i, v)
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7 ** (len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3 ** (len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))


# for i in range(1, 10000):
#     if Solution().rotatedDigits(i) != Solution().rotatedDigits_1(i):
#         print(i)
# print(Solution().rotatedDigits(99))
print(Solution().rotatedDigits_2(99))

