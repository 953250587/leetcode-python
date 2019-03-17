"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.



Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation:
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
Example 2:

Input: ["xc","yb","za"]
Output: 0
Explanation:
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation:
We have to delete every column.


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        36 ms
        """
        if len(A) <= 1:
            return 0
        import collections
        ans = 0
        # 总列数
        l = len(A[0])
        cur_A = [A]
        for i in range(l):
            next_A = []  # 用于分块，相同字母的部分需要分开，之后只需要保证每一块有序即可
            for A in cur_A:
                # 用dicts记录情况
                dicts = collections.defaultdict(list)
                # 用于判断是否已经可以跳过这次循环
                flag = False
                # 对每个元素，判断是否按顺序排在前一个之后
                for k, a in enumerate(A):
                    dicts[a[i]].append(a)
                    if k == 0:
                        start = a[i]
                    else:
                        # 如果是则继续
                        if ord(start) <= ord(a[i]):
                            start = a[i]
                        # 否则就需要删除这行
                        else:
                            ans += 1
                            # 所有元素的该行都会删除，所以保持原始的cur_A不发生变化
                            next_A = cur_A
                            # 意味着其它部分可以跳过计算
                            flag = True
                            break
                # 如果这一列完全没问题，则需要删除掉只有一个的字符串，该字符串不受其它字母的影响了
                else:
                    # print(dicts)
                    for key in dicts:
                        if len(dicts[key]) == 1:
                            pass
                        else:
                            # 只添加有多个的情况
                            next_A.append(dicts[key])
                if flag:
                    break
            cur_A = next_A
        return ans

    def minDeletionSize_1(self, A):
        """
        :type A: List[str]
        :rtype: int
        24ms
        """
        index = [range(len(A))]
        res = 0
        for i in range(len(A[0])):
            # print [x[i] for x in A]
            newindx = []
            status = "success"
            for r in index:
                j = 0
                changed_index = 0
                while j < len(r) - 1:
                    if A[r[j]][i] > A[r[j + 1]][i]:
                        res += 1
                        status = "fail"
                        break
                    elif A[r[j]][i] == A[r[j + 1]][i]:
                        newr = []
                        while j < len(r) - 1 and A[r[j]][i] == A[r[j + 1]][i]:
                            newr.append(r[j])
                            j += 1
                        newr.append(r[j])
                        newindx.append(newr)
                        status = "equal"
                        changed_index = 1
                    else:
                        j += 1

                if status == "fail": break
            # print index, status, newindx
            if status == "success":
                return res
            if status == "equal":
                index = newindx
        return res

print(Solution().minDeletionSize(["ca","bb","ac"]))
print(Solution().minDeletionSize(["xc","yb","za"]))
print(Solution().minDeletionSize(["zyx","wvu","tsr"]))
print(Solution().minDeletionSize(['z', 'a']))
print(Solution().minDeletionSize(['z']))
print(Solution().minDeletionSize(["abx","agz","bgc","bfc"]))
print(Solution().minDeletionSize(["bwwdyeyfhc",
                                  "bchpphbtkh",
                                  "hmpudwfkpw",
                                  "lqeoyqkqwe",
                                  "riobghmpaa",
                                  "stbheblgao",
                                  "snlaewujlc",
                                  "tqlzolljas",
                                  "twdkexzvfx",
                                  "wacnnhjdis"]))

