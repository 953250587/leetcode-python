"""
 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        66ms
        """
        self.sets=set()
        self.dicts={}
        for i in nums:
            if i not in self.sets:
                self.dicts[i]=1
            else:
                self.dicts[i]+=1
            self.sets.add(i)
        a=sorted(self.dicts.items(),key=lambda item:item[1])
        result=[]
        for i in a[::-1]:
            result.append(i[0])
        return result[:k]

    def topKFrequent_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        59ms
        """
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1

        freqNum = {}
        for num in numFreq:
            freq = numFreq[num]
            if freq in freqNum:
                freqNum[freq].append(num)
            else:
                freqNum[freq] = [num]

        sortedFreqs = list(freqNum.keys())
        sortedFreqs.sort(reverse=True)

        count = 0
        result = []
        for key in sortedFreqs:
            numArray = freqNum[key]
            for num in numArray:
                if count < k:
                    result.append(num)
                    count += 1
                else:
                    return result

        return result
print(Solution().topKFrequent([1,1,1,2,2,3],2))
