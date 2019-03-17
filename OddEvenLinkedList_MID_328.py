"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        52ms
        """
        if head==None or head.next==None:
            return head
        head_1=head
        head_1_start=head
        head_2=head.next
        head_2_start = head.next
        while head_2!=None and head_2.next!=None:
           head_1.next=head_2.next
           head_1=head_1.next
           head_2.next=head_1.next
           head_2=head_2.next
        head_1.next=head_2_start
        return head_1_start

def visit(head):
    while head!=None:
        print(head.val)
        head=head.next

head=ListNode(1)
head_copy=head
lists=[1,2]
for i in lists[1:]:
    head_copy.next=ListNode(i)
    head_copy=head_copy.next
# visit(head)
visit(Solution().oddEvenList(head))

