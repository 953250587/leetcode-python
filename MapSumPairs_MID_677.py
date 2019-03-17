"""
 Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:

Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5


"""


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        39ms
        """
        self.dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        a = self.dict
        for char in key:
            if char not in a:
                a[char] = {'val':0}
            a = a[char]
        a['val'] = val
        print(self.dict)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        a = self.dict
        for char in prefix:
            if char in a:
                a = a[char]
            else:
                return 0
        self.result = 0
        print(a)
        def _sum(root):
            self.result += root['val']
            for key in root:
                if key is not 'val':
                    _sum(root[key])
        _sum(a)
        return self.result




        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)
obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
obj.insert("appllle", 2)
print(obj.sum('ap'))


from collections import defaultdict
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        29ms
        """
        self.book=defaultdict(int)
        self.exist={}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        remain=val
        if key in self.exist:
            val-=self.exist[key]
        self.exist[key]=remain
        for i in range(len(key)):
            prefix=key[:i+1]
            self.book[prefix]+=val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.book[prefix]