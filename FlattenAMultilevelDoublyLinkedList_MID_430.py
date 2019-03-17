"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
Explanation for the above example:

Given the following multilevel doubly linked list:



We should return the following flattened doubly linked list:




"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        864MS
        """
        stack = []

        dummy = Node(0, None, None, None)
        dummy.next = head

        cur = head

        while cur:
            if cur.child:
                stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None

            if not cur.next and stack:
                connect = stack.pop()
                cur.next = connect
                if connect:
                    connect.prev = cur
            cur = cur.next

        return dummy.next

    def flatten_1(self, head):
        """
        :type head: Node
        :rtype: Node
        848MS
        """

        def flattenEnd(head):
            node = head
            while node.child or node.next:
                if node.child:
                    child = node.child
                    node.child = None

                    child.prev = node
                    node = flattenEnd(child)
                    node.next = child.prev.next
                    child.prev.next = child
                if node.next:
                    node.next.prev = node
                    node = node.next
            return (node)

        if head:
            flattenEnd(head)
        return (head)