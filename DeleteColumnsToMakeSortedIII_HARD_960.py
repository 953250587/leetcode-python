"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.



Example 1:

Input: ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
Example 2:

Input: ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
Example 3:

Input: ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        memo = {}
        l = len(A)
        count = len(A[0])

        def dfs(i, cur_state, ans):
            if i >= count:
                return ans
            if (i, cur_state) in memo:
                return memo[(i, cur_state)]
            next_state = ''.join([A[k][i] for k in range(l)])
            ans_temp = ans
            if all([ord(cur_state[k]) <= ord(next_state[k]) for k in range(l)]):
                ans_temp = dfs(i + 1, next_state, ans + 1)
            ans = max(ans_temp, dfs(i + 1, cur_state, ans))
            memo[(i, cur_state)] = ans
            return ans

        cur_state = 'a' * l
        ans = dfs(0, cur_state, 0)
        return count - ans

    def minDeletionSize_1(self, A):
        """
        :type A: List[str]
        :rtype: int
        1352 ms
        """
        count = len(A)
        l = len(A[0])
        dp = [0 for _ in range(l)]
        dp[0] = 1
        for i in range(1, l):
            for j in range(i):
                # 从之前满足条件的找出最大的后+1
                if all([A[k][j] <= A[k][i] for k in range(count)]):
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return l - max(dp)

    def minDeletionSize_2(self, A):
        """
        :type A: List[str]
        :rtype: int
        112ms
        """
        dp = [1 for _ in A[0]]
        for j in range(1, len(A[0])):
            i = j - 1
            curDp = 1
            while i >= 0:
                # print(j, i)
                # 先判断是否是最大的，如果不是则跳过这个
                if dp[i] + 1 <= curDp:
                    i -= 1
                    continue
                r = 0
                # 如果是，则判断是否满足递增要求，其余部分一致
                while r < len(A):
                    if A[r][j] < A[r][i]: break
                    r += 1
                if r != len(A):
                    i -= 1
                    continue
                curDp = dp[i] + 1
                i -= 1
            dp[j] = curDp
        # print(dp)
        return len(A[0]) - max(dp)

print(Solution().minDeletionSize_1(["babca", "bbazb"]))
print(Solution().minDeletionSize_1(["edcba"]))
print(Solution().minDeletionSize_1(["ghi", "def", "abc"]))
# import random
# import string
# def create_string(nums):
#     return ''.join(random.choice(string.ascii_lowercase) for i in range(nums))
# inp = []
# for i in range(100):
#     temp = create_string(100)
#     # print(temp)
#     inp.append(temp)
# print(Solution().minDeletionSize(inp))
print(Solution().minDeletionSize_1(["bgfdbgfdegdgdccbfhbfdbfgcfefeacghgadedahbgcdabdegdbdfgaecbahhgedcfegeaegefddchfcefceeceehdffhehcddbe","cebaedfgbfadhheaafcabfdgfbdfabagfhhgbbaefcfhhbhhbababgdcagaddgadfbhgdfegggdhfbebacbcggebabheecbddcac","dbcdfbccabbheddaaggefegbbfegfdccheadbedaaabagdgbaebcahhaeaaffdfebhahcfebfgbfedcfedgdaacdecfhccccbacg","bghgadceachegaehfbfcbddefbadfbeaehegaafhbafhgedhhbcdedceeghhhbaffgbbfebfhfffcadchaaaeddabdhhgbffefah","hhhgdcggedfaeghabbfheabcdhdbhdabhcfdegacdfabgeaddaabddeaefdaaabgedfccbechhegfbcccffhagabdcecgfdggegg","fdafaabgcffdhbchcafghhgabbhbfebegfgdhaabeababfbdbbegacbaceeaceefdfgfdhahddhbaabcfcebhffehgccedbcgggb","efbbhfgefddfhbfhdhdecabhdbhchfabddefbggdhegcgahbebcgdachhggfeedfgahgahhfgfcdchdfcbdeabedbchehbhdhfeb","egbccfhhdeafgbefdahcagbghhffgachfffddffhcbgbhbhbdgeeebededdcbdcbedcgcdfcgffhfhdaaebcgdadhhdccfcgabbf","gbghhagbafadcbacefghhbffagehbfaahgabgdagbbhbcgagafffedhedhhchbbfgcefbedhgggchbcfbffhgfdgdgebdfdgcgaf","cfhcbbhhbefaaegfgfadbfbddhgcdbgaaffbcechbgbfddbfcfgeeeabcbdbbdggefedhgfcghggebfbeeghebbbfcbefegheeea"]))



