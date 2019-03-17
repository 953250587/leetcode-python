"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        179ms
        """
        str1=[]
        self.l1=l1
        while self.l1!=None:
            str1.append(self.l1.val)
            self.l1=self.l1.next
        str2 = []
        self.l2 = l2
        while self.l2 != None:
            str2.append(self.l2.val)
            self.l2 = self.l2.next
        print(str1,str2)
        if len(str1)>=len(str2):
            a=str1
            b=str2
        else:
            a=str2
            b=str1
        result=[]
        flag=False
        while len(a)>0:
            x=a.pop()
            if len(b)>0:
                y=b.pop()
            else:
                y=0
            if flag:
                ans=x+y+1
            else:
                ans=x+y
            result.append(ans%10)
            if ans//10>=1:
                flag=True
            else:
                flag=False
        if flag:
            result.append(1)
        print(result)
        head=ListNode(result[-1])
        head_copy=head
        for i in result[:-1][::-1]:
            head.next=ListNode(i)
            head=head.next
        return head_copy

    def addTwoNumbers_1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        119ms
        """
        one = 0
        first = l1
        while (first):
            one = one * 10 + first.val

            first = first.next

        two = 0
        second = l2
        while (second):
            two = two * 10 + second.val
            second = second.next
        temp = str(one + two)
        res = ListNode(0)
        tmp = res
        for c in temp:
            t = ListNode(ord(c) - ord('0'))

            res.next = t
            res = res.next

        return tmp.next
l1=[7,2,4,3]
head=ListNode(l1[0])
h_l1=head
for i in l1[1:]:
    head.next=ListNode(i)
    head=head.next

l2=[5,6,4]
head=ListNode(l2[0])
h_l2=head
for i in l2[1:]:
    head.next=ListNode(i)
    head=head.next
a=Solution().addTwoNumbers(h_l1,h_l2)
while a!=None:
    print(a.val)
    a=a.next

l1=[7]
head=ListNode(l1[0])
h_l1=head
for i in l1[1:]:
    head.next=ListNode(i)
    head=head.next

l2=[5]
head=ListNode(l2[0])
h_l2=head
for i in l2[1:]:
    head.next=ListNode(i)
    head=head.next
a=Solution().addTwoNumbers(h_l1,h_l2)
while a!=None:
    print(a.val)
    a=a.next

