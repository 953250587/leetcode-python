"""
 Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        109ms
        """
        if not root:
            return []
        self.dict = {}
        result = []
        def structure2list(root):
            if root.left:
                a = structure2list(root.left)
            else:
                a = 'N'
            if root.right:
                b = structure2list(root.right)
            else:
                b = 'N'
            c = str(root.val) + ',' + a + ',' + b
            if c not in self.dict:
                self.dict[c] = [root]
            else:
                self.dict[c].append(root)
            return c

        structure2list(root)
        for key in self.dict:
            d = self.dict[key]
            if len(d) > 1:
                result.append(d[0])
        return result

    def findDuplicateSubtrees_1(self, root):
        """
        98ms
        :param root:
        :return:
        """
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None and node2 is not None:
                return False
            elif node1 is not None and node2 is None:
                return False
            return node1.val == node2.val and check(node1.left, node2.left) and check(node1.right, node2.right)

        def visit(node, dic):
            if node is None:
                return '#'
            l = visit(node.left, dic)
            r = visit(node.right, dic)
            s = str(node.val) + l + r
            dic[s] = dic.get(s, []) + [node]
            return s

        dic, ans = {}, []
        visit(root, dic)
        # print dic
        for n, nodes in dic.iteritems():
            if len(nodes) > 1:
                ans.append(nodes[0])
        return ans

    def findDuplicateSubtrees_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        85ms
        """
        self.nodes = dict()
        self.ret = []
        self.inorder(root)
        return self.ret

    def inorder(self, root):
        if not root:
            return '#'
        path = str(root.val) + self.inorder(root.left) + self.inorder(root.right)
        if path not in self.nodes:
            self.nodes[path] = 1
        else:
            if self.nodes[path] == 1:
                self.ret.append(root)
                self.nodes[path] += 1
        return path
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
print(Solution().findDuplicateSubtrees(None))
