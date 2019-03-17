"""
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        56ms
        """
        if not root:
            return [[] for i in range(k)]
        node_copy = root
        count = 0
        while root:
            count += 1
            root = root.next
        print(count)
        a = count // k
        b = count % k
        print(a, b)
        result = []
        for i in range(k):
            if b > 0:
                count_a = a + 1
                result.append(node_copy)
                while count_a > 0:
                    pre_node = node_copy
                    node_copy = node_copy.next
                    count_a -= 1
                pre_node.next = None
                b -= 1
            else:
                count_a = a
                result.append(node_copy)
                while count_a > 0:
                    pre_node = node_copy
                    node_copy = node_copy.next
                    count_a -= 1
                pre_node.next = None
        return result

    def splitListToParts_1(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        c = root
        l = 0
        while c:
            l += 1
            c = c.next
        c = root
        prev = None
        a, b = divmod(l, k)
        for _ in range(b):
            # move a+1
            res.append(c)
            if prev:
                prev.next = None

            for _ in range(a + 1):
                prev = c
                c = c.next

        for _ in range(k - b):
            res.append(c)
            if prev:
                prev.next = None
            for _ in range(a):
                prev = c
                c = c.next
        return res
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
root_l = ListNode(root[0])
root_l_c = root_l
for i in root[1:]:
    root_l.next = ListNode(i)
    root_l = root_l.next
c = Solution().splitListToParts(root_l_c, k)
for i in c:
    while i:
        print(i.val)
        i = i.next
    print('/n')

root = [1, 2, 3]
k = 5
root_l = ListNode(root[0])
root_l_c = root_l
for i in root[1:]:
    root_l.next = ListNode(i)
    root_l = root_l.next
c = Solution().splitListToParts(root_l_c, k)
for i in c:
    while i:
        print(i.val)
        i = i.next
    print('/n')
print(Solution().splitListToParts(None, 3))
