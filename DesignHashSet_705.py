"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""


class MyHashSet(object):
    """
     1460 ms
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = [False for _ in range(1000000)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.value[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.value[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.value[key]



        # Your MyHashSet object will be instantiated and called as such:
        # obj = MyHashSet()
        # obj.add(key)
        # obj.remove(key)
        # param_3 = obj.contains(key)


class MyHashSet_1(object):
    """
    108ms
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for i in range(1000)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        t = key % 1000
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        t = key % 1000
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        t = key % 1000
        return key in self.arr[t]

