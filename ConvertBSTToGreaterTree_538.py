"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        132ms
        """
        if root==None:
            return root
        def smallconverBST(root,sum):
            if root.right != None:
                sum=smallconverBST(root.right,sum)
            tmp = root.val
            root.val += sum
            sum += tmp
            if root.left != None:
                sum=smallconverBST(root.left, sum)
            return sum

        sum=0
        smallconverBST(root,sum)
        return root

def visit(root):
    if root.right != None:
        visit(root.right)
    print(root.val)
    if root.left!=None:
        visit(root.left)

root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(13)

visit(root)
visit(Solution().convertBST(root))

