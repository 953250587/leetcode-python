"""
Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

"""

import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        365ms
        """
        self.sets=set()
        self.list=[]

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            return False
        else:
            self.sets.add(val)
            self.list.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            self.sets.remove(val)
            self.list=list(self.sets)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        l=len(self.list)
        if l>=1:
           a=random.randint(0,l-1)
           return self.list[a]
        else:
            return None



        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()

a=set()
a.pop()
a.add(1)
a.add(2)
a.add(3)
a.add(-1)
a.add('a')
# a.remove(1)
print(a)
b=a.pop()
print(b)
a.add(b)
print(len(a))
print(a)
print(list(a))


class RandomizedSet_1:
    def __init__(self):
        """
        Initialize your data structure here.
        178ms
        """
        self.nums = []
        self.pos = {}  # stores the position of each number, key is the val, value is the pos

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            # then I need to update both nums and pos
            idx, last = self.pos[val], self.nums[-1]
            # copy last to nums[idx] and pop out the last element
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val, None)
            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]