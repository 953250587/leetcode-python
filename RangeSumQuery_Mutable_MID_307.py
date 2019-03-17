"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

    The array is only modifiable by the update function.
    You may assume the number of calls to update and sumRange function is distributed evenly.

"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        276ms
        142ms
        """
        self.nums=nums
        self.nums_c=[0 for i in range(len(nums))]
        # def add(k,value):
        #     while k<=len(nums):
        #         self.nums_c[k-1]+=value
        #         k+=self.lowbit(k)
        #         # print(value,k)
        # for i in range(len(nums)):
        #     add(i+1,self.nums[i])
        # print(self.nums_c)
        for i in range(1, len(self.nums_c) + 1):
            idx_bit = i + (i & -i)
            if idx_bit < len(self.nums_c) + 1:
                self.nums_c[idx_bit - 1] += self.nums_c[i - 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i=i+1
        a=val - self.nums[i - 1]
        self.nums[i-1]=val
        while i <= len(nums):
            self.nums_c[i - 1] += a
            i += self.lowbit(i)
        print(self.nums_c)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def sum_all(k):
            sum_1=0
            k+=1
            while k:
                sum_1+=self.nums_c[k-1]
                k-=self.lowbit(k)
            return sum_1
        return sum_all(j)-sum_all(i-1)

    def lowbit(self,x):
        return x&-x



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)
nums=[7,2,7,2,0]
obj = NumArray(nums)
obj.update(4,6)
obj.update(0,2)
obj.update(0,9)
print(obj.sumRange(4,4))
obj.update(3,8)
print(obj.sumRange(0,4))
obj.update(4,1)
print(obj.sumRange(0,3))
print(obj.sumRange(0,4))
obj.update(0,4)


class NumArray_1(object):
    def prefixSum(self, i):
        s = 0
        i += 1
        while i:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.bit = [0] + nums
        for i in range(1, len(self.bit)):
            idx_bit = i + (i & -i)
            if idx_bit < len(self.bit):
                self.bit[idx_bit] += self.bit[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        added = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < len(self.bit):
            self.bit[i] += added
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum(j) - self.prefixSum(i - 1)