"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.


Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]


Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        72 ms
        """
        self.root = root
        self.cur_node = [[root, 2]]
        while self.cur_node:
            cur_node = self.cur_node[0][0]
            if cur_node.left and cur_node.right:
                self.cur_node.pop(0)
                self.cur_node.append([cur_node.left, 2])
                self.cur_node.append([cur_node.right, 2])
            elif cur_node.left:
                self.cur_node[0][1] = 1
                self.cur_node.append([cur_node.left, 2])
                break
            else:
                break


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.cur_node[0][1] == 1:
            self.cur_node[0][0].right = TreeNode(v)
            temp = self.cur_node.pop(0)
            self.cur_node.append([temp[0].right, 2])
            return temp[0].val
        else:
            self.cur_node[0][0].left = TreeNode(v)
            self.cur_node[0][1] = 1
            self.cur_node.append([self.cur_node[0][0].left, 2])
            return self.cur_node[0][0].val


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root



        # Your CBTInserter object will be instantiated and called as such:
        # obj = CBTInserter(root)
        # param_1 = obj.insert(v)
        # param_2 = obj.get_root()

root = TreeNode(1)
obj = CBTInserter(root)
for v in [2, 3, 4]:
    print(obj.insert(v))

def visit(root):
    print(root.val)
    if root.left:
        visit(root.left)
    else:
        print('#')
    if root.right:
        # print('right')
        visit(root.right)
    else:
        print('#')

visit(root)


class CBTInserter(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        44ms
        """
        import collections
        self.root = root
        self.deque = collections.deque()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.deque[0]
        newnode = TreeNode(v)
        self.deque.append(newnode)
        if not node.left:
            node.left = newnode
        else:
            node.right = newnode
            self.deque.popleft()
        return node.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
