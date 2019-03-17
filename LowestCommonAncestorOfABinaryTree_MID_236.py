"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        119ms
        """
        self.mark=0
        self.lists=[]
        if root==None:
            return None
        if p==q:
            return p

        def find_p_q(root):
            if self.mark==0:
                self.lists.append(root)
            if root == p or root == q:
                self.mark += 1
                if self.mark == 2:
                    return True
            if root.left != None:
                if find_p_q(root.left):
                    return True
            if root.right != None:
                if find_p_q(root.right):
                    return True
            if root in self.lists:
                self.lists.remove(root)
            return False
        find_p_q(root)
        return self.lists[-1]

    def lowestCommonAncestor_1(self, root, p, q):
        #135ms
        def path(root, goal):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == goal:
                            return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()

        return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)


root=TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)
root.right.left=TreeNode(0)
root.right.riht=TreeNode(8)


print(Solution().lowestCommonAncestor(root,root.left.left,root.left.right.right).val)