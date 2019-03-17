"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples:

[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

"""


class MedianFinder(object):
    """
    412ms
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.l = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        import bisect
        bisect.insort_left(self.nums, num)
        self.l += 1
        print(self.nums)


    def findMedian(self):
        """
        :rtype: float
        """
        if self.l % 2 == 1:
            return self.nums[(self.l - 1) // 2]
        else:
            mid = (self.l - 1) // 2
            return (self.nums[mid] + self.nums[mid + 1]) / 2



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(-1)
print(obj.findMedian())

import heapq


class MedianFinder(object):
    """
    372ms
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.first = 0
        self.second = 0
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.count += 1

        if self.count == 1:
            self.first = num
            return

        if self.count == 2:
            self.second = num
            return

        if self.count == 3:
            min_num = min(self.first, self.second)
            max_num = max(self.first, self.second)
            heapq.heappush(self.max_heap, -1 * min_num)
            heapq.heappush(self.min_heap, max_num)

        if num < -1.0 * self.max_heap[0]:
            heapq.heappush(self.max_heap, -1.0 * num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1.0 * temp)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count == 1:
            return self.first

        if self.count == 2:
            return (self.second + self.first) / 2.0

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2.0

        elif len(self.max_heap) > len(self.min_heap):
            return -1.0 * self.max_heap[0]
        else:
            return self.min_heap[0]


class MedianFinder_1(object):
    """
    372ms
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.minHeap and self.minHeap[0] <= num:
            heapq.heappush(self.minHeap, float(num))
            if len(self.minHeap) == len(self.maxHeap) + 2:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap, -float(num))
            if len(self.maxHeap) == len(self.minHeap) + 2:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]