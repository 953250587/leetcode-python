"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    # 102ms
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root==None:
            self.lists=[]
        else:
            self.root = root
            self.lists = []

            def find(root):
                self.lists.append(root)
                if root.left != None:
                    find(root.left)

            find(root)
        # print(self.lists)



    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.lists)>0:
            return True
        else:
            return False


    def next(self):
        """
        :rtype: int
        """
        def find(root):
            self.lists.append(root)
            if root.left!=None:
                find(root.left)
        def findnewtree():
            newtree=self.lists[-1].right
            self.lists = self.lists[:-1]
            if newtree!=None:
                find(newtree)

        # print('sss', len(self.lists))
        ans=self.lists[-1].val
        findnewtree()
        return ans


        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())
root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.left=TreeNode(0)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(2)
root.left.right.right=TreeNode(3)

i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print(v)

class BSTIterator_1(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val