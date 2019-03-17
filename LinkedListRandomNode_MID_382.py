"""
iven a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

"""


# Definition for singly-linked list.
import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        235ms
        """
        self.head=head
        self.rand=0

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        self.num = 0
        head_copy=self.head
        while head_copy!=None:
            self.num+=1
            a=random.uniform(0,1)
            if a<1.0/self.num:
                self.rand=head_copy.val
            head_copy=head_copy.next
        return self.rand




        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
solution = Solution(head)
for i in range(10):
    print(solution.getRandom())
print(random.uniform(0,1))