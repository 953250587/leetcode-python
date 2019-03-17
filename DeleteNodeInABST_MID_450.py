"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        119ms
        """
        self.root=root
        def change(root):
            if root.left!=None and root.right==None:
                return root.left
            if root.left==None and root.right!=None:
                return root.right
            if root.left!=None and root.right!=None:
                if root.right.left==None:
                    root.right.left=root.left
                    return root.right
                else:
                    s=root.right
                    copy_1=s
                    while s.left!=None:
                        copy_1=s
                        s=s.left
                    copy_1.left=None
                    s.left=root.left
                    t=s
                    while t.right!=None:
                        t=t.right
                    t.right=root.right
                    return s
            if root.left==None and root.right==None:
                return None

        def find(root,key):
            if root==None:
                return root
            if root.val>key:
                root.left=find(root.left,key)
            elif root.val<key:
                root.right=find(root.right,key)
            else:
                return change(root)
            return root
        return find(root,key)

    def deleteNode_1(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        96ms
        """

        def find(root):
            currentNode = root
            while currentNode.left:
                currentNode = currentNode.left
            return currentNode

        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            targetNode = find(root.right)
            root.val = targetNode.val
            root.right = self.deleteNode(root.right, targetNode.val)
        return root

root=TreeNode(8)
root.left=TreeNode(2)
root.right=TreeNode(10)
root.left.left= TreeNode(1)
root.left.right=TreeNode(6)
root.left.right.left=TreeNode(5)
root.left.right.right=TreeNode(7)
# root.left.right.left.left=TreeNode(5)



def visit(root):
    if root != None:
        print(root.val)
        print('left')
        visit(root.left)
        print('right')
        visit(root.right)
visit(root)
print('\n')
b=Solution().deleteNode(root,2)
visit(b)





