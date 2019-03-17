"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        195ms
        """
        if t1==None:
            t1_val=0
            t1_left=None
            t1_right=None
        else:
            t1_val=t1.val
            t1_left = t1.left
            t1_right = t1.right
        if t2==None:
            t2_val=0
            t2_left = None
            t2_right = None
        else:
            t2_val=t2.val
            t2_left = t2.left
            t2_right = t2.right
        if t1==None and t2==None:
            return None
        a=TreeNode(t1_val+t2_val)
        a.left=self.mergeTrees(t1_left,t2_left)
        a.right = self.mergeTrees(t1_right, t2_right)
        return a

    # 202ms
    def mergeTrees_1(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

root=TreeNode(1)
root.left=TreeNode(3)
root.right=TreeNode(2)
root.left.left=TreeNode(5)

root_2=TreeNode(2)
root_2.left=TreeNode(1)
root_2.right=TreeNode(3)
root_2.left.right=TreeNode(4)
root_2.right.right=TreeNode(7)

def visit(root):
    if root.right != None:
        visit(root.right)
    print(root.val)
    if root.left!=None:
        visit(root.left)

print(visit(Solution().mergeTrees(root,root_2)))
