"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        35ms
        """
        # if citations==[] or sum(citations)==0:
        #     return 0
        citations=sorted(citations)
        count=0
        # temp=citations[-1]
        for i in citations[::-1]:
            if count>=i:
                return count
            count+=1
            # if count>=i:
            #     return i
        return len(citations)

    def hIndex_1(self, citations):
        # 39ms
        n = len(citations)
        citeCount = [0] * (n + 1)
        for c in citations:
            if c >= n:
                # 记录下所有大于列表长度的个数
                citeCount[n] += 1
            else:
                # 否则对应位置+1
                citeCount[c] += 1

        i = n - 1
        while i >= 0:
            # 判断大于i+1的元素的个数，是不会超过数组长度
            citeCount[i] += citeCount[i + 1]
            if citeCount[i + 1] >= i + 1:
                return i + 1
            i -= 1
        return 0

    def hIndex_3(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) / 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        # 如果citations[mid] < n - mid，mid+1=l，则说明l是citations[l] >= n - mid
        # 如果citations[mid] >= n - mid，r=mid-1,此时l=mid，则说明l是citations[l] >= n - mid
        return n - l
print(Solution().hIndex([0,0,0,0]))
