"""
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input:
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation:
0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation:
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:

    If N is the length of the linked list given by head, 1 <= N <= 10000.
    The value of each node in the linked list will be in the range [0, N - 1].
    1 <= G.length <= 10000.
    G is a subset of all values in the linked list.

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        135ms
        """
        start = head
        A = []
        while start:
            A.append(start.val)
            start = start.next
        B = [0 for _ in range(len(A))]
        for i, val in enumerate(A):
            B[val] = i
        C = [-1 for _ in range(len(A))]
        for i in G:
            C[B[i]] = 1
        ans = 0
        before = -1
        for i in C:
            if i== 1 and before == -1:
                ans += 1
            before = i
        return ans

    def numComponents_1(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        139ms
        """
        # convert to hsh: val->idx for fast fidning of val
        hsh = {}
        for idx, val in enumerate(G):
            hsh[val] = idx
        # Iterate through the linked list, if node.val is in hsh
        # assign hsh[node.val] to current connected component id
        # if not, increment id
        id = 0
        while head:
            if head.val in hsh:
                hsh[head.val] = id
            else:
                id += 1
            head = head.next
        return len(set(list(hsh.values())))

l = [0,1,2,3]
head = ListNode(0)
start = head
for i in l:
    head.next = ListNode(i)
    head = head.next
head = start.next
print(Solution().numComponents(head, [0,1,3]))


l = [0,1,2,3,4]
head = ListNode(0)
start = head
for i in l:
    head.next = ListNode(i)
    head = head.next
head = start.next
print(Solution().numComponents(head, [0,3,1,4]))