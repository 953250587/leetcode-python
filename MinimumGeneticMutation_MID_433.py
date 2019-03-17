"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.


Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1


Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2


Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        28ms
        """
        import heapq
        # def minMutation(self, start, end, bank):
        bank, n = set(bank) - {start}, len(start)
        q = [(0, start, bank)]
        while q:
            mut, s, pool = heapq.heappop(q)
            if s == end:
                return mut
            for new in pool:
                if sum(s[i] != new[i] for i in range(n)) == 1:
                    heapq.heappush(q, (mut + 1, new, pool - {new}))

        return -1

    def minMutation_1(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        20ms
        """

        def is_one_diff(cur, gene):
            counter = 0
            for i in range(len(cur)):
                if cur[i] != gene[i]:
                    counter += 1
                    if counter > 1:
                        return False
            return True

        def dothing(usable_genes, cur, count):
            if cur == end:
                return count
            ans = -1
            for gene in usable_genes:
                if is_one_diff(cur, gene):
                    res = dothing(usable_genes.difference({gene}), gene, count + 1)
                    if res != -1:
                        if ans == -1:
                            ans = res
                        else:
                            ans = min(ans, res)
            return ans

        return dothing(set(bank), start, 0)
