"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        175ms
        """
        c = Counter()
        for ch in s:
            c[ch] = c[ch] + 1
        # print(c)
        a=sorted(c.items(),key=lambda item:item[1],reverse=True)
        index_dict = {k[0]: i for i, k in enumerate(a)}
        # print(index_dict)
        B_ordered = sorted(s, key=lambda x: index_dict[x])
        # print(a)
        # print(B_ordered)
        return ''.join(B_ordered)

    def frequencySort_1(self, s):
        """
        :type s: str
        :rtype: str
        62ms
        """
        count = dict()
        result = ''
        sort = dict()

        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        if not s:
            return result
        for c, f in count.items():
            if f not in sort:
                sort[f] = list()
            sort[f].append(c)
        max_f = max(sort.keys())
        min_f = min(sort.keys())
        for f in range(min_f, max_f + 1):
            if f not in sort:
                continue
            c_list = sort[f]
            for c in c_list:
                result = c * f + result
        return result


print(Solution().frequencySort('23'))
print(Solution().frequencySort('cccaaa'))
print(Solution().frequencySort("tree"))