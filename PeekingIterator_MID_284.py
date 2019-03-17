"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.i=0
        self.list=nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.i<len(self.list):
            return True
        else:
            return False

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.i+=1
        return self.list[self.i-1]

class PeekingIterator(object):
    # 39ms
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=iterator
        self.flag = True
        self.nums=[]
        while self.iterator.hasNext():
            self.nums.append(self.iterator.next())
        self.iterator_2=Iterator(self.nums)
        self.iterator = Iterator(self.nums)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.flag:
            self.a=self.iterator_2.next()
            self.flag=False
        return self.a

    def next(self):
        """
        :rtype: int
        """
        if self.flag:
            self.iterator_2.next()
        else:
            self.flag=True
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext()


class PeekingIterator_1(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nxt = None
        self.iterator = iterator
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        ans = self.nxt
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
        else:
            self.nxt = None
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nxt: return True
        return False

nums=[1,2,3,4]
iter = PeekingIterator(Iterator(nums))
print(iter.hasNext())
print(iter.peek())
print(iter.peek())
print(iter.next())
print(iter.next())
print(iter.peek())
print(iter.peek())
print(iter.next())
print(iter.hasNext())
print(iter.peek())
print(iter.hasNext())
print(iter.next())
print(iter.hasNext())