"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    199ms
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.s = []
        def dfs_visit(root):
            if not root:
                self.s.append('null')
                return
            self.s.append(root.val)
            dfs_visit(root.left)
            dfs_visit(root.right)
        dfs_visit(root)
        print(self.s)
        strs = ''
        for i in self.s:
            strs += str(i) + ','
        return strs[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        self.count = 0
        def dfs_deser(s):
            if s[self.count] != 'null':
                root = TreeNode(int(s[self.count]))
                self.count += 1
            else:
                self.count += 1
                return None
            root.left = dfs_deser(s)
            root.right = dfs_deser(s)
            return root
        return dfs_deser(s)



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
codec = Codec()
a = codec.serialize(root)
root_1 = codec.deserialize(a)
b = codec.serialize(root_1)
print(a)
print(b)

from collections import deque


class Codec:
    """
    232ms
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # level-order trans
        q = deque()
        q.append(root)
        s = []
        while q:
            node = q.popleft()
            if node:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                s.append('N')

        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        q_s = deque(data.split(','))
        q = deque()

        if q_s:
            val = q_s.popleft()
            root = TreeNode(int(val)) if val != 'N' else None
            q.append(root)

        while q:
            node = q.popleft()
            if node:
                if q_s:
                    val = q_s.popleft()
                    node.left = TreeNode(int(val)) if val != 'N' else None
                    q.append(node.left)
                if q_s:
                    val = q_s.popleft()
                    node.right = TreeNode(int(val)) if val != 'N' else None
                    q.append(node.right)

        return root