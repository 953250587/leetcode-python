"""
 N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:

    len(row) is even and in the range of [4, 60].
    row is guaranteed to be a permutation of 0...len(row)-1.

"""
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        53ms
        """
        l = len(row)
        # print(sets)
        dicts = {}
        ans = 0
        for i in range(l):
            if row[i] == 0:
                row[i] = 100
            elif row[i] == 1:
                row[i] = -100
            elif row[i] % 2 == 1:
                row[i] -= 1
                row[i] = -row[i]
        print(row)
        sets = set(row)
        for i in range(0, l, 2):
            dicts[row[i]] = row[i + 1]
            dicts[row[i + 1]] = row[i]
        for i in range(0, l, 2):
            if row[i] not in sets:
                continue
            else:
                s = set()
                start = row[i]
                while start not in s:
                    s.add(start)
                    sets.remove(start)
                    a = dicts[start]
                    sets.remove(a)
                    start = -a

                print(s)
                ans += len(s) - 1
        return ans
# print(Solution().minSwapsCouples(row = [0, 2, 1, 3]))
# print(Solution().minSwapsCouples(row = [3, 2, 0, 1]))
print(Solution().minSwapsCouples([1,3,2,6,4,7,8,9,0,5]))
print(Solution().minSwapsCouples([5,4,2,6,3,1,0,7]))





