"""
Implement a data structure supporting the following operations:

    Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
    Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
    GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
    GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.
"""


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        138ms
        """
        import collections
        self.dicts = {}
        self.nums = collections.defaultdict(set)
        self.max = 0
        self.min = float('inf')
        self.count = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.count += 1
        if self.count == 0:
            self.min = 1
            self.max = 1
        if key not in self.dicts:
            self.dicts[key] = 0
        self.dicts[key] += 1
        a = self.dicts[key]
        if a == 1:
            self.nums[1].add(key)
            if self.min > 1:
                self.min = 1
        else:
            self.nums[a - 1].remove(key)
            self.nums[a].add(key)
            if a - 1 == self.min and len(self.nums[a - 1]) == 0:
                self.min += 1
        if a > self.max:
            self.max = a

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.dicts:
            self.count -= 1
            self.dicts[key] -= 1
            a = self.dicts[key]
            self.nums[a + 1].remove(key)
            if a != 0:
                self.nums[a].add(key)
                if a + 1 == self.max and len(self.nums[a + 1]) == 0:
                     self.max -= 1
                if a < self.min:
                    self.min = a
            else:
                del self.dicts[key]
                if len(self.nums[a]) == 0:
                    m = float('inf')
                    for key in self.dicts:
                        m = min(m, self.dicts[key])
                    self.min = m





    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.count == 0:
            return ''
        a = self.nums[self.max].pop()
        self.nums[self.max].add(a)
        return a

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.count == 0:
            return ''
        a = self.nums[self.min].pop()
        self.nums[self.min].add(a)
        return a



        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()
# obj = AllOne()
# obj.inc('1')
# obj.inc('1')
# obj.inc('2')
# obj.inc('2')
# obj.inc('1')
# print('**********')
# print(obj.getMaxKey())
# print(obj.getMinKey())
# obj.dec('1')
# obj.dec('1')
# print('**********')
# print(obj.getMaxKey())
# print(obj.getMinKey())
# obj.dec('2')
# obj.dec('2')
# print('**********')
# print(obj.getMaxKey())
# print(obj.getMinKey())
# obj.dec('1')
# print(obj.getMaxKey())
# print(obj.getMinKey())

obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
obj.dec('b')
obj.dec('b')
print(obj.min)
print(obj.max)
print(obj.nums)
print(obj.dicts)
print('**********')
print(obj.getMinKey())
obj.dec('a')
# print(obj.min)
# print(obj.max)
# print(obj.nums)
# print(obj.dicts)
print('**********')
print(obj.getMaxKey())
print(obj.getMinKey())


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        79ms
        """
        self.d = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.d:
            self.d[key] = 1
        else:
            self.d[key] = self.d[key] + 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.d:
            if self.d[key] == 1:
                del self.d[key]
            else:
                self.d[key] = self.d[key] - 1

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        x = sorted(self.d.iteritems(), key=lambda x: x[1], reverse=True)
        if len(x) > 0:
            return x[0][0]
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        x = sorted(self.d.iteritems(), key=lambda x: x[1], reverse=False)
        if len(x) > 0:
            return x[0][0]
        else:
            return ""


import collections


class AllOne_1(object):
    def __init__(self):
        """
        98ms
        Initialize your data structure here.
        """
        self.freq = collections.defaultdict(set)
        self.cache = collections.defaultdict()
        self.max_freq = 0
        self.min_freq = 0

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.cache:
            curr_freq = self.cache[key]
            self.freq[curr_freq].remove(key)

            if len(self.freq[curr_freq]) == 0:
                del self.freq[curr_freq]

            curr_freq += 1
            self.freq[curr_freq].add(key)
            self.cache[key] = curr_freq

        else:
            self.cache[key] = 1
            self.freq[1].add(key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.cache:
            curr_freq = self.cache[key]

            self.freq[curr_freq].remove(key)

            if len(self.freq[curr_freq]) == 0:
                del self.freq[curr_freq]

            curr_freq -= 1

            if curr_freq != 0:
                self.freq[curr_freq].add(key)
                self.cache[key] = curr_freq
            else:
                del self.cache[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        
        if self.freq:
            max_freq = max(self.freq.keys())
            return list(self.freq[max_freq])[0]

        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """

        if self.freq:
            min_freq = min(self.freq.keys())
            return list(self.freq[min_freq])[0]

        return ''