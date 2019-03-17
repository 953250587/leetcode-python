"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        122ms
        """
        import heapq
        h = []
        print(lists, lists[0])
        for list in lists:
            if list:
                heapq.heappush(h, (list.val, list))
        print(h)
        root = ListNode(-1)
        root_copy = root
        while h:
            print(h)
            a = heapq.heappop(h)
            root.next = a[1]
            root = root.next
            print(a[1].val)
            b = a[1].next
            # print(b.val)
            if b:
                heapq.heappush(h, (b.val, b))
        return root_copy.next

    def mergeKLists_1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        102ms
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

root_1 = ListNode(1)
root_1.next = ListNode(2)
root_1.next.next = ListNode(4)
# a = root_1
# while a:
#     print(a.val)
#     a = a.next

root_2 = ListNode(5)
root_2.next = ListNode(6)
root_2.next.next = ListNode(7)

root_3 = ListNode(3)
root_3.next = ListNode(8)

a = Solution().mergeKLists([[]])
while a:
    print(a.val)
    a = a.next
