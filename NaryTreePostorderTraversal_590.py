"""
Given an n-ary tree, return the postorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its postorder traversal as: [5,6,3,2,4,1].


Note: Recursive solution is trivial, could you do it iteratively?


"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        124ms
        """
        start = [root]
        result = []
        while start:
            a = start.pop(0)
            if a:
                result.append(a.val)
                for i, c in enumerate(a.children[::-1]):
                    start.insert(0 + i, c)
        return result[::-1]