"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        1260 ms
        """
        import collections
        # 用来记录B中所有单词的情况
        total = collections.defaultdict(int)
        for b in B:
            temp = collections.Counter(b)
            # 对于每一个单词中的字母，判断个数是否大于之前统计的情况
            # 如果大就更新信息
            for key in temp:
                total[key] = max(total[key], temp[key])
        # 记录最后的结果
        result = []
        for a in A:
            temp = collections.Counter(a)
            # 判断a中是否包含所有需要的字母
            if all([temp[key] >= total[key] for key in total]):
                result.append(a)
        return result

    def wordSubsets_1(self, A, B):
        """
        260ms
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        主要差异在all可能会计算所有之后再判断，而这个算到不满足就跳出
        """
        s = set(A)
        B = set(B)
        letters_required = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in letters_required or count > letters_required[j]:
                    letters_required[j] = count

        for i in A:
            for j in letters_required:
                if i.count(j) < letters_required[j]:
                    s.remove(i)
                    break
        return list(s)


print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]))
print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]))
print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]))
print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]))
print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]))




