"""
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        68ms
        """
        count = 0
        head_copy = head
        while head_copy:
            count += 1
            head_copy = head_copy.next
        num = count // k
        print(count, num)
        head_copy = head
        result = []
        while num > 0:
            k_copy = k
            while k_copy > 0:
                if k == k_copy:
                    root = ListNode(None)
                    root.next = head_copy
                    pre = head_copy
                    cur = head_copy.next
                else:
                    cur = head_copy.next
                    head_copy.next = pre
                    pre = head_copy
                head_copy = cur
                k_copy -= 1
            root.next.next = None
            result.append([pre, root.next])
            num -= 1
        result.append([head_copy, None])
        # print(len(result))
        root_result = result[0][0]
        root_result_copy = result[0][1]
        for i in result[1:]:
            root_result_copy.next = i[0]
            root_result_copy = i[1]
        return root_result

    def reverseKGroup_1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        66ms
        """

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # now we know the length of the linkedlist.
        if length < k:
            return head
        rounds = length / k
        # how many rounds of [k] nodes we should reverse.
        finalHead = ListNode(0)
        dummy = finalHead
        # each time dummy should be the tail of previous nodes (the nodes that finished reversion.)
        cur = head
        for i in range(rounds):
            nextDummy = None
            # at each round, [cur] means the start node of this round.
            for j in range(k):
                if j == 0:
                    nextDummy = cur
                nextCur = cur.next
                dummy_next = dummy.next
                dummy.next = cur
                cur.next = dummy_next
                cur = nextCur
                # nextDummy's next should be None; nextDummy is actually the first node in this round.
                # And it becomes the tail in the reversed nodes.
            dummy = nextDummy
        # if length % k == 0, cur would be None
        # else: cur would be the immutuable nodes's head.
        dummy.next = cur
        return finalHead.next
nums = [1, 2, 3, 4, 5]
k = 0
for i, num in enumerate(nums):
    if i == 0:
        root = ListNode(num)
        root_copy = root
    else:
        root.next = ListNode(num)
        root = root.next

c = Solution().reverseKGroup(root_copy, k)
# for i in c:
#     while i:
#         print(i.val)
#         i = i.next

while c:
    print(c.val)
    c = c.next



