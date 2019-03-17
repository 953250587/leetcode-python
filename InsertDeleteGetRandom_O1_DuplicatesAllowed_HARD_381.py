"""
Design a data structure that supports all following operations in average O(1) time.
Note: Duplicate elements are allowed.

    insert(val): Inserts an item val to the collection.
    remove(val): Removes an item val from the collection if present.
    getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();

"""

import random
class RandomizedCollection(object):
    """
    186ms
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts = {}
        self.mark = []



    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.mark.append(val)
        l = len(self.mark)
        if val in self.dicts:
            self.dicts[val][0] += 1
            self.dicts[val][1].add(l - 1)
            return False
        else:
            self.dicts[val] = [1, {l - 1}]
            return True


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dicts:
            self.dicts[val][0] -= 1
            pos = self.dicts[val][1].pop()
            l = len(self.mark) - 1
            a = self.mark.pop()
            if pos < l:
                self.mark[pos] = a
                self.dicts[a][1].remove(l)
                self.dicts[a][1].add(pos)

            if self.dicts[val][0] == 0:
                del self.dicts[val]
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.mark[random.randint(0, len(self.mark) - 1)]



        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
obj = RandomizedCollection()
print(obj.insert(1))
print(obj.dicts)
print(obj.mark)
print(obj.insert(1))
print(obj.dicts)
print(obj.mark)
print(obj.insert(2))
print(obj.dicts)
print(obj.mark)
print(obj.remove(3))
print(obj.dicts)
print(obj.mark)
for i in range(10):
    print(obj.getRandom())
print(obj.remove(1))
print(obj.dicts)
print(obj.mark)
for i in range(10):
    print(obj.getRandom())


# obj = RandomizedCollection()
# print(obj.insert(1))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(1))
# print(obj.dicts)
# print(obj.mark)
# print(obj.remove(1))
# print(obj.dicts)
# print(obj.mark)
# for i in range(10):
#     print(obj.getRandom())

# obj = RandomizedCollection()
# print(obj.insert(10))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(10))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(20))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(20))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(30))
# print(obj.dicts)
# print(obj.mark)
# print(obj.insert(30))
# print(obj.dicts)
# print(obj.mark)
# print('*************')
# print(obj.remove(10))
# print(obj.dicts)
# print(obj.mark)
# print(obj.remove(10))
# print(obj.dicts)
# print(obj.mark)
# print(obj.remove(30))
# print(obj.dicts)
# print(obj.mark)
# print(obj.remove(30))
# print(obj.dicts)
# print(obj.mark)
# for i in range(10):
#     print(obj.getRandom())

import collections
class RandomizedCollection(object):
    def __init__(self):
        """
        149ms
        Initialize your data structure here.
        """
        self.nums = []
        self.dic = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val not in self.dic:
            self.dic[val].add(len(self.nums) - 1)
            # print 'insert1', self.dic
            return True
        else:
            self.dic[val].add(len(self.nums) - 1)
            # print 'insert2', self.dic
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        # print 'remove', self.dic
        if val in self.dic:
            if len(self.dic[val]) >= 1:
                loc = self.dic[val].pop()
                if loc == len(self.nums) - 1:
                    self.nums.pop()
                    if len(self.dic[val]) == 0:
                        del self.dic[val]
                    # print 'after remove1', self.dic
                    return True
                self.nums[-1], self.nums[loc] = self.nums[loc], self.nums[-1]
                self.dic[self.nums[loc]].discard(len(self.nums) - 1)
                self.dic[self.nums[loc]].add(loc)
                if len(self.dic[self.nums[-1]]) == 0:
                    del self.dic[self.nums[-1]]
                self.nums.pop()
                # print 'after remove2', self.dic
                return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)


import random


class RandomizedCollection_1(object):
    def __init__(self):
        """
        159ms
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)
        self.n = list()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.d[val].append(len(self.n))
        self.n.append(val)

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.d[val]:
            return False
        loc = self.d[val].pop()
        if loc != len(self.n) - 1:
            last = self.n[-1]
            self.n[loc] = last
            self.d[last].remove(len(self.n) - 1)
            self.d[last].append(loc)
        self.n.pop()
        if not self.d[val]:
            self.d.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.n)