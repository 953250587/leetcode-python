"""
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.before = None
        self.next = None

class LRUCache(object):
    """
    208ms
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.capacity_list = {}
        self.cur_capacity = 0
        self.end = ListNode(None)
        self.start = self.end

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.capacity_list:
            a = self.capacity_list[key]
            self.list_change(a[1])
            print('ggggg', self.start.next)
            print('gggggg', self.end)
            return a[0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.capacity_list:
            self.capacity_list[key][0] = value
            self.list_change(self.capacity_list[key][1])
        else:
            a = ListNode(key)
            if self.cur_capacity < self.capacity:
                self.cur_capacity += 1
                self.end.next = a
                a.before = self.end
                self.end = a
            else:
                self.end.next = a
                a.before = self.end
                self.end = a
                b = self.start.next
                # print('ggg', self.start.next.val)
                # print('ggg', self.end)
                # print(b.val)
                self.start.next = self.start.next.next
                self.start.next.before = self.start
                del self.capacity_list[b.val]
            self.capacity_list[key] = [value, a]
        print(self.capacity_list)
        print('ggggg_1', self.start.next)
        print('ggggg_2', self.end)

    def list_change(self, ListNode):
        if ListNode.next == None:
            return
        ListNode.before.next = ListNode.next
        ListNode.next.before = ListNode.before
        self.end.next = ListNode
        ListNode.before = self.end
        self.end = ListNode
        self.end.next = None
        return




        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
# cache = LRUCache(2)
# print(cache.put(1, 1))
# print(cache.put(2, 2))
# print(cache.get(1))       # returns 1
# print(cache.put(3, 3))     #evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# print(cache.put(4, 4))    # evicts key 1
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4


cache = LRUCache(3)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(2, -2))# returns 1
print(cache.put(3, 3))     #evicts key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.put(4, 4))    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
print(cache.put(5, 5))
print(cache.put(2, 2))
print(cache.get(2))

import collections


class LRUCache(object):
    """
    206ms
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = dict()
        self.dq = collections.deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d: return -1
        self.dq.append(key)
        self.d[key][1] += 1
        return self.d[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.dq.append(key)

        if key not in self.d:
            self.d[key] = [value, 1]
        else:
            self.d[key] = [value, self.d[key][1] + 1]

        if len(self.d) > self.capacity:
            while True:
                k = self.dq.popleft()
                self.d[k][1] += -1
                if not self.d[k][1]:
                    del self.d[k]
                    return