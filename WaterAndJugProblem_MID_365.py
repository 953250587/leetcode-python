"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        775ms
        """
        self.max=0
        self.min=0
        if x>y:
            self.max=x
            self.min=y
        else:
            self.max=y
            self.min=x
        if self.min==0:
            if z==self.max or z==self.min:
                return True
            else:
                return False
        if z >= 2 * max(x, y):
            return False
        if z in [0, x + y, x, y]:
            return True
        a=[i*self.min for i in range(1,self.max//self.min+2)]
        b=[self.max-a[i] for i in range(self.max//self.min)]
        print(a)
        print(b)
        if z in a or z in b:
            return True
        self.sets=set()
        self.sets_c=set()
        self.b=b[-1]
        while self.b not in self.sets_c:
            self.sets_c.add(self.b)
            self.sets.add(self.b)
            self.sets.add(self.max + (self.min - self.b))
            self.sets.add(self.max-(self.min-self.b))
            self.sets.add(self.min+self.b)
            self.sets.add(self.max+self.b)
            self.b=self.max-(self.min-self.b)
            if z in self.sets:
                return True
            if self.b>self.min:
                self.b=self.b%self.min
        self.sets=set()
        return False

    def canMeasureWater_1(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        26ms
        """
        if x + y < z:
            return False
        if (x == z or y == z) or (x + y == z):
            return True
        return z % self.GCD(x, y) == 0


    def GCD(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
print(Solution().canMeasureWater(3,5,4))
print(Solution().canMeasureWater(0,2,1))
print(Solution().canMeasureWater(0,0,0))
print(Solution().canMeasureWater(34,5,6))
print(Solution().canMeasureWater(11,13,1))
print(Solution().canMeasureWater(22003,31237,1))